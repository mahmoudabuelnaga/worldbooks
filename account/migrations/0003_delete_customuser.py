# Generated by Django 2.1 on 2019-04-25 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190425_1408'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
