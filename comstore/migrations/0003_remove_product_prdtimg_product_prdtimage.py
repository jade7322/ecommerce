# Generated by Django 4.1.2 on 2023-11-27 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comstore', '0002_categories_product_delete_membersdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='prdtimg',
        ),
        migrations.AddField(
            model_name='product',
            name='prdtimage',
            field=models.ImageField(default='', upload_to='image'),
        ),
    ]
