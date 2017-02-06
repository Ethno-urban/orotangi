from rest_framework import viewsets
from orotangi.models import Notes, Books, Tags
from orotangi.api.serializers import NoteSerializer, BookSerializer, TagSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    permission_classes = []  # to remove after testing


class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = []  # to remove after testing


class TagViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Tags.objects.all()
    serializer_class = TagSerializer
    permission_classes = []  # to remove after testing
