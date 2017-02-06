from django.conf.urls import url, include

from orotangi.api.views import BookViewSet, NoteViewSet, TagViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'tags', TagViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
