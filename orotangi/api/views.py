from django.http import HttpResponse
from orotangi.api.serializers import NoteSerializer
from orotangi.api.serializers import BookSerializer, TagSerializer
from orotangi.models import Notes, Books, Tags
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        """

        :param data:
        :param kwargs:
        """
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

    def update_tags(self, tags):
        """
        check the tags and update or create them

        @TODO: handle the case where the provided tags of the current note
        have been change : ie the current note had tag1 tag2, and the update
        provide tag3 and tag4.

        :param tags:
        :return:
        """
        my_tags = []
        for tag in tags:
            obj, created = Tags.objects.get_or_create(
                tag=tag.strip(),
                user=self.request.user,
                defaults={'tag': tag.strip(),
                          'user': self.request.user})
            if created:
                my_tags.append(created)
            else:
                my_tags.append(obj)
        return my_tags

    def create(self, request, *args, **kwargs):
        """
        create a note by adding the current user to the data to be saved
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.data
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def get_queryset(self):
        """
        get the data of the current user
        :return:
        """
        return Notes.objects.filter(user=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.data
        if len(data['tags']) > 0:
            tags = self.update_tags(data['tags'])
            data['tags'] = tags
        data['user'] = request.user.id
        instance = self.get_object()
        serializer = NoteSerializer(instance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
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
        """
        get the data of the current user
        :return:
        """
        return Books.objects.filter(user=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        """
        get the data of the current user
        :return:
        """
        return Tags.objects.filter(user=self.request.user)
