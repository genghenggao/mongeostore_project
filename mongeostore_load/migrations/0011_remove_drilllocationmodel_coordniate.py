# Generated by Django 3.0.5 on 2020-12-10 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mongeostore_load', '0010_drilllocationmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drilllocationmodel',
            name='coordniate',
        ),
    ]
