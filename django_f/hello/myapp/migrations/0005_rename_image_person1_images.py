# Generated by Django 4.1.6 on 2023-02-13 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_person1_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person1',
            old_name='image',
            new_name='images',
        ),
    ]
