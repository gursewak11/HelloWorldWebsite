# Generated by Django 2.2.2 on 2019-08-29 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20190829_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='profile_picture',
        ),
    ]
