# Generated by Django 4.1.7 on 2023-05-01 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0009_remove_project_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='img',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
