# Generated by Django 3.0.5 on 2020-10-27 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mongeostore_load', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileinfo2',
            old_name='name',
            new_name='filename',
        ),
    ]