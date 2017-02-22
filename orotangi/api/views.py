from orotangi.api.serializers import NoteSerializer
from orotangi.api.serializers import BookSerializer, TagSerializer
from orotangi.models import Notes, Books, Tags
from rest_framework import viewsets

class NoteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Tags.objects.all()
    serializer_class = TagSerializer
