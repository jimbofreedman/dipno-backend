# Generated by Django 3.0.5 on 2020-05-12 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200511_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='facebook_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook_username',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
