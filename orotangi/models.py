# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    """
        Book
    """
    book = models.CharField(max_length=80)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.book

    class Meta:
        db_table = 'oro_books'


class Tags(models.Model):

    """
        Tags
    """
    tag = models.CharField(max_length=80, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.tag

    class Meta:
        db_table = 'oro_tags'


class Notes(models.Model):

    """
        Notes
    """
    user = models.ForeignKey(User)
    book = models.ForeignKey(Books)
    tags = models.ManyToManyField(Tags, related_name='notes_tags')
    url = models.URLField(max_length=255, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)  # False when deleted

    def __str__(self):
        return "%s - %s" % (self.title, self.tag)

    class Meta:
        ordering = ('date_created', )
        db_table = 'oro_notes'
