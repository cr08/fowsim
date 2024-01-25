# Generated by Django 3.2.6 on 2024-01-25 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardDatabase', '0048_auto_20231106_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardArtist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='decklist',
            name='shareMode',
            field=models.TextField(blank=True, choices=[['private', 'private'], ['tournament', 'tournament']], default='', max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='artists',
            field=models.ManyToManyField(blank=True, related_name='cards', to='cardDatabase.CardArtist'),
        ),
    ]
