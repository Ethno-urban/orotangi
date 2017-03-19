from orotangi.api.serializers import NoteSerializer, BookSerializer
from orotangi.models import Books, Notes

from rest_framework import viewsets


class UserMixin(viewsets.GenericViewSet):

    def get_queryset(self):
        """
        get the data of the current user
        :return:
        """
        qs = super(UserMixin, self).get_queryset()
        return qs.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        request.data['user'] = request.user.id
        return super(UserMixin, self).create(request, *args, **kwargs)


class NoteViewSet(UserMixin, viewsets.ModelViewSet):
    """
    This viewset provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer


class BookViewSet(UserMixin, viewsets.ModelViewSet):
    """
    This viewset provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer
