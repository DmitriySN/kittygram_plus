from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, LightCatViewSet, OwnerViewSet

router = DefaultRouter()
router.register(r'mycats', LightCatViewSet)
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
