# Generated by Django 5.0.2 on 2024-02-28 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_telegramgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramgroup',
            name='bot_token',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
