# Generated by Django 4.2.1 on 2023-05-22 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0022_remove_service_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='i',
        ),
    ]