# Generated by Django 3.0 on 2020-05-06 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libri', '0014_auto_20200506_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libri',
            name='immagine',
            field=models.ImageField(blank=True, db_column='Immagine', null=True, upload_to='C:\\Users\\Utente\\Documents\\DesktopBiblioteca\\Biblioteca\\media'),
        ),
    ]
