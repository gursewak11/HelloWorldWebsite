# Generated by Django 2.2.2 on 2019-08-11 18:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_teammember_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='authorised',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='birth_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='designation',
            field=models.CharField(blank=True, default='Member', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='joined_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='specialisation',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='user_name',
            field=models.CharField(blank=True, default='UserName', max_length=200, null=True),
        ),
    ]