# Generated by Django 4.2 on 2023-05-03 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_rename_imageall_aboutcompanyuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(null=True, upload_to='image/product/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(null=True, upload_to='image/product/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(null=True, upload_to='image/product/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(null=True, upload_to='image/product/'),
        ),
    ]
