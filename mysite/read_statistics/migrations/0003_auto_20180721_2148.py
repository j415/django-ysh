# Generated by Django 2.0 on 2018-07-21 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistics', '0002_readdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='readdetail',
            old_name='data',
            new_name='date',
        ),
    ]
