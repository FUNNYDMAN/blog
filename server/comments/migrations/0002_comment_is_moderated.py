# Generated by Django 2.0 on 2018-08-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_moderated',
            field=models.BooleanField(default=False),
        ),
    ]
