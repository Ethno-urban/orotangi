from orotangi.models import Books, Tags, Notes
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('__all__')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('__all__')


class NoteSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Notes
        #fields = ('user', 'book', 'tags', 'url', 'title', 'content', 'date_created', 'date_modified', 'date_deleted',
        #          'status')
        fields = ('__all__')
