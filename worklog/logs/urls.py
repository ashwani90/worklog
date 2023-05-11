from rest_framework import routers
from .views import NoteViewSet,LogViewSet, CategoryViewSet, TypeViewSet, HealthTypeViewSet, ExerciseViewSet, HealthLogViewSet
from django.urls import path, include
from . import views as log_views
from django.views.decorators.csrf import csrf_exempt
# from graphene_django.views import GraphQLView

router = routers.DefaultRouter()
router.register(r'note', NoteViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'type', TypeViewSet)
router.register(r'log', LogViewSet)
router.register(r'health_type', HealthTypeViewSet)
router.register(r'exercise', ExerciseViewSet)
router.register(r'health', HealthLogViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('app/', log_views.listing, name='listing'),
    path("app/view_log/<int:log_id>", log_views.view_log, name="view_log"),
    path("app/acc", include("django.contrib.auth.urls")),
    # path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]