# Generated by Django 2.0 on 2018-03-28 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20180328_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateField(),
        ),
    ]
