# Generated by Django 4.1.5 on 2023-01-07 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cars',
            new_name='car',
        ),
    ]
