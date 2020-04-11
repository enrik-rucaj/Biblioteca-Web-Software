# Generated by Django 3.0 on 2020-04-11 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0006_auto_20200411_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autori',
            fields=[
                ('idAutore', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('CognomeNome', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Autori',
            },
        ),
        migrations.AlterField(
            model_name='libro',
            name='idLibro',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]