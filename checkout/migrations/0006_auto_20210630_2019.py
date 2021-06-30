# Generated by Django 3.2.3 on 2021-06-30 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='right_or_left',
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='product_club',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
