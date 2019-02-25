# Generated by Django 2.1.4 on 2018-12-26 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='flower',
            field=models.TextField(default='', max_length=65535),
        ),
        migrations.AddField(
            model_name='user',
            name='star',
            field=models.TextField(default='', max_length=65535),
        ),
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(upload_to='user_image'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sh',
            field=models.IntegerField(choices=[(0, '未审核'), (1, '审核中'), (2, '审核通过')], default=0, verbose_name='申请状态'),
        ),
    ]
