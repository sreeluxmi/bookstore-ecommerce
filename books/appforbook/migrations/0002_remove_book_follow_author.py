# Generated by Django 4.1.7 on 2023-03-23 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appforbook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='follow_author',
        ),
    ]
