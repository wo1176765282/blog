# Generated by Django 2.1.4 on 2018-12-21 06:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='手机号不符合规范', regex='^(136|176|184)\\d{8}$')])),
                ('img', models.ImageField(upload_to='uploads/user_image')),
                ('c', models.IntegerField(choices=[(0, '普通用户'), (1, '高级用户')], default=0)),
                ('sh', models.IntegerField(choices=[(0, '未审核'), (1, '审核中'), (2, '审核通过')], default=0)),
            ],
        ),
    ]
