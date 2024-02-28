from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import (
    BannerViewSet,
    ResponsibilityViewSet,
    GettingStarterViewSet,
    PlatformViewSet,
)

router = DefaultRouter()
router.register("banners", BannerViewSet)
router.register("responsibilities", ResponsibilityViewSet)
router.register("getting-starters", GettingStarterViewSet)
router.register("platforms", PlatformViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
