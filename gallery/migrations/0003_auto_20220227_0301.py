# Generated by Django 3.2.10 on 2022-02-27 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20220227_0233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='categories_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='gallery',
            old_name='gallery_descripton',
            new_name='descripton',
        ),
        migrations.RenameField(
            model_name='gallery',
            old_name='gallery_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='gallery',
            old_name='gallery_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='location_name',
            new_name='name',
        ),
    ]
