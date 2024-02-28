from rest_framework import viewsets
from .models import Banner, Responsibility, GettingStarter, Platform
from .serializers import (
    BannerSerializer,
    ResponsibilitySerializer,
    GettingStarterSerializer,
    PlatformSerializer,
)

# Create your views here.


class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class ResponsibilityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Responsibility.objects.all()
    serializer_class = ResponsibilitySerializer


class GettingStarterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GettingStarter.objects.all()
    serializer_class = GettingStarterSerializer


class PlatformViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
