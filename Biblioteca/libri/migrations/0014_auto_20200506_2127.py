# Generated by Django 3.0 on 2020-05-06 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libri', '0013_auto_20200506_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libri',
            name='immagine',
            field=models.ImageField(blank=True, db_column='Immagine', null=True, upload_to='media'),
        ),
    ]