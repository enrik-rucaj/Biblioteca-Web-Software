# Generated by Django 3.0 on 2020-04-11 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0007_auto_20200411_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodiceDewey',
            fields=[
                ('idDew', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('Dew', models.TextField(default='')),
                ('Argomento', models.TextField(default='')),
            ],
        ),
    ]
