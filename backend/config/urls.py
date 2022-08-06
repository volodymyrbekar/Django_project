from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from rest_framework.routers import DefaultRouter

from rest_framework_swagger.views import get_swagger_view

from backend.apps.restaurants.views import RestaurantViewSet
from backend.apps.files.views import FileViewSet
from backend.apps.menus.views import MenuViewSet


schema_view = get_swagger_view(title="Api restaurant")
router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, basename='restaurants')
router.register(r'menus', MenuViewSet, basename='menus')
router.register(r'files', FileViewSet, basename='files')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

