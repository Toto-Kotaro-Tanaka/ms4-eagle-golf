# Generated by Django 3.2.3 on 2021-07-14 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_order_original_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='free_golf_balls',
        ),
        migrations.AlterField(
            model_name='order',
            name='original_cart',
            field=models.TextField(default=''),
        ),
    ]
