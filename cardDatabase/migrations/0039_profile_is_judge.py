# Generated by Django 3.2.6 on 2022-10-17 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardDatabase', '0038_bannedcard_combinationbannedcards_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_judge',
            field=models.BooleanField(default=False),
        ),
    ]
