from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .models import Banner, Responsibility, GettingStarter, Platform


class BannerSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Banner)

    class Meta:
        model = Banner
        fields = ["translations", "image"]


class ResponsibilitySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Responsibility)

    class Meta:
        model = Responsibility
        fields = ["translations"]


class GettingStarterSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=GettingStarter)

    class Meta:
        model = GettingStarter
        fields = ["translations", "image"]


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ["title", "url", "image"]
