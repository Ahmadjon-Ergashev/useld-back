import requests
from rest_framework import viewsets
from .models import Banner, Responsibility, GettingStarter, Platform, Telegram
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


def send_message(TELEGRAM_API_URL, method, data, files=None):
    return requests.post(TELEGRAM_API_URL + method, data, files=files)


def send_info(request):
    print(request.data)
    if request.method == "POST":
        TELEGRAM = Telegram.objects.last()
        TOKEN = TELEGRAM.bot_token
        TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}/"
        GROUP_ID = TELEGRAM.group_id

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        message = "*New Message:*\n"
        message += f"*Name*: {name}\n"
        message += f"*Mail:*: {email}\n"
        message += f"*Message*: {message}\n"

        response = send_message(
            TELEGRAM_API_URL,
            "sendMessage",
            {"chat_id": GROUP_ID, "text": message, "parse_mode": "Markdown"},
        )
        print(response.status_code)