# Generated by Django 4.0.4 on 2022-05-29 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0003_images_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
    ]
