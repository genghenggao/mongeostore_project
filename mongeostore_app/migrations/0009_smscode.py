# Generated by Django 3.0.5 on 2020-09-27 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mongeostore_app', '0008_auto_20200926_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmsCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=32, verbose_name='手机号')),
                ('smscode', models.CharField(max_length=8, verbose_name='验证码')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '手机验证码',
                'verbose_name_plural': '手机验证码',
            },
        ),
    ]