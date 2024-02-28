import requests
from django.http import JsonResponse, HttpResponseBadRequest
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
    if request.method == "POST":
        TELEGRAM = Telegram.objects.last()
        TOKEN = TELEGRAM.bot_token
        TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}/"
        GROUP_ID = TELEGRAM.group_id

        name = request.POST.get("name")
        email = request.POST.get("email")
        text = request.POST.get("message")
        phone = request.POST.get("phone")

        message = "*New Message:*\n"
        message += f"👤 *Name*: {name}\n"
        message += f"✉️ *Mail:*: {email}\n"
        message += f"📞 *Phone*: {phone}\n"
        message += f"💬 *Message*: {text}\n"

        response = send_message(
            TELEGRAM_API_URL,
            "sendMessage",
            {"chat_id": GROUP_ID, "text": message, "parse_mode": "Markdown"},
        )
        if response.status_code == 200:
            return JsonResponse({"message": "Message Sent Successfully"})
    return HttpResponseBadRequest("Message Not Sent", status=400)