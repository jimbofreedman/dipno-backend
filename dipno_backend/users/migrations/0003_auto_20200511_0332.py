# Generated by Django 3.0.5 on 2020-05-11 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200510_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='available_from',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='available_to',
            field=models.TimeField(blank=True, null=True),
        ),
    ]