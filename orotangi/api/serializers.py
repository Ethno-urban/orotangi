from orotangi.models import Books, Notes
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = ('id', 'user', 'book', 'url', 'title', 'content',
                  'date_created', 'date_modified', 'date_deleted', 'status')
