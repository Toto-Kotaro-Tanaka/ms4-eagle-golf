# Generated by Django 3.2.3 on 2021-07-04 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210703_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
