from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from . import views
from settings import settings

urlpatterns = [

]

from django.urls import include, path
from rest_framework import routers
from src import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'recycletypes', views.RecycleTypeView, basename='recycletypes')
router.register(r'projects', views.ProjectView, basename='projects')
router.register(r'events', views.EventView, basename='events')
router.register(r'posts', views.WallPostView, basename='posts')
router.register(r'pickpoints', views.PickPointView, basename='pickpoints')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)