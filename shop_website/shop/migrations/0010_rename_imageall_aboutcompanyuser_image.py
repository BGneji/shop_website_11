# Generated by Django 4.2 on 2023-04-20 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_aboutcompanyuser_alter_bestsellingproducts_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutcompanyuser',
            old_name='imageall',
            new_name='image',
        ),
    ]