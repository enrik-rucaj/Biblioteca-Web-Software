# Generated by Django 3.0 on 2020-04-08 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libri',
            name='autore',
            field=models.TextField(max_length=200),
        ),
    ]