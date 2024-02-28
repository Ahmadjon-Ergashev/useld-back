from django.db import models
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.

class Banner(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=100, blank=True),
        body=models.TextField(blank=True)
    )
    image = models.ImageField(upload_to='banners/')
    
    def __str__(self):
        return self.title


class Responsibility(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=100),
        body=models.TextField()
    )
    
    def __str__(self):
        return self.title


class GettingStarter(TranslatableModel):
    translations = TranslatedFields(
        body=models.TextField()
    )
    image = models.ImageField(upload_to='getting_started/')

    def __str__(self):
        return self.body[:50]


class Platform(models.Model):
    title=models.CharField(max_length=100)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='platforms/')
    
    def __str__(self):
        return self.title
