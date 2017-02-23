from django.http import HttpResponse
from orotangi.api.serializers import NoteSerializer
from orotangi.api.serializers import BookSerializer, TagSerializer
from orotangi.models import Notes, Books, Tags
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class NoteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id
        instance = self.get_object()
        serializer = NoteSerializer(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)


class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return Books.objects.filter(user=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tags.objects.filter(user=self.request.user)
