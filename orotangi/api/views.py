from orotangi.api.serializers import NoteSerializer, BookSerializer
from orotangi.models import Books, Notes

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


class NoteResultsSetPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 50


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
    pagination_class = NoteResultsSetPagination
    # filter the note
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        """
        Optionally restricts the returned notes to a given user,
        by filtering against a `book` query parameter in the URL.
        """
        queryset = Notes.objects.all()
        book = self.request.query_params.get('book', None)
        if book is not None:
            queryset = queryset.filter(book__name=book)
        return queryset


class BookViewSet(UserMixin, viewsets.ModelViewSet):
    """
    This viewset provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer
