# Generated by Django 2.2 on 2019-05-29 13:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bat', '0006_auto_20190529_1346'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bat',
            new_name='Bat_textquestions',
        ),
    ]
