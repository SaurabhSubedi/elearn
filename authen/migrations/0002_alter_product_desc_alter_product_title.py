# Generated by Django 4.1.7 on 2023-04-07 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.TextField(max_length=50),
        ),
    ]
