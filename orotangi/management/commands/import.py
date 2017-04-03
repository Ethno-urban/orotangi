#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
import os
import io
# django
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from logging import getLogger

from orotangi.models import Books, Notes


# create logger
logger = getLogger('orotangi.import')


class Command(BaseCommand):

    help = 'Import Evernote notes'

    def data(self, path):
        for folder, subs, files in os.walk(path):
            for file in files:
                filename, file_extension = os.path.splitext(file)
                if file_extension == '.data' or file_extension == '.bak':
                    continue
                with io.open(os.path.join(folder, file), 'r', encoding='utf-8') as src:
                    title = src.readline()[2:]
                    content = src.read()

                    yield {'title': title, 'content': content}

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int)
        parser.add_argument('path', help='Evernote path to the exported files')

    def handle(self, *args, **options):
        """
            get all the triggers that need to be handled
        """
        try:
            user = User.objects.get(id=options['user_id'])
            book_obj, book_created = Books.objects.get_or_create(
                name='Evernote',
                user=options['user_id'],
                defaults={'name': 'Evernote',
                          'user': user}
            )
            for note in self.data(options['path']):
                print(note['title'])
                obj, created = Notes.objects.get_or_create(
                    title=note['title'],
                    book=book_obj,
                    user=options['user_id'],
                    defaults={'title': note['title'],
                              'content': note['content'],
                              'status': True,
                              'user': user},
                )
        except User.DoesNotExist:
            print("user does not exist")