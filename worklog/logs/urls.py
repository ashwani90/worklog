from rest_framework import routers
from .views import NoteViewSet,LogViewSet, CategoryViewSet, TypeViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'note', NoteViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'type', TypeViewSet)
router.register(r'log', LogViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]