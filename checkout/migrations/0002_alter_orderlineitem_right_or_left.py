# Generated by Django 3.2.3 on 2021-06-16 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='right_or_left',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
