# Generated by Django 3.0.4 on 2020-04-16 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autori',
            fields=[
                ('idautore', models.AutoField(db_column='IdAutore', primary_key=True, serialize=False)),
                ('cognomenome', models.CharField(db_column='CognomeNome', max_length=60)),
            ],
            options={
                'verbose_name_plural': 'Autori',
                'db_table': 'Autori',
            },
        ),
        migrations.CreateModel(
            name='Codicedewey',
            fields=[
                ('iddew', models.AutoField(db_column='IdDew', primary_key=True, serialize=False)),
                ('dew', models.DecimalField(db_column='Dew', decimal_places=0, max_digits=3)),
                ('argomento', models.CharField(db_column='Argomento', max_length=250)),
            ],
            options={
                'db_table': 'CodiceDewey',
            },
        ),
        migrations.CreateModel(
            name='Collocazione',
            fields=[
                ('collocazione', models.CharField(db_column='Collocazione', max_length=250, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Collocazione',
            },
        ),
        migrations.CreateModel(
            name='Editori',
            fields=[
                ('ideditore', models.AutoField(db_column='IdEditore', primary_key=True, serialize=False)),
                ('editore', models.CharField(db_column='Editore', max_length=250)),
            ],
            options={
                'db_table': 'Editori',
            },
        ),
        migrations.CreateModel(
            name='Libri',
            fields=[
                ('idlibro', models.AutoField(db_column='IdLibro', primary_key=True, serialize=False)),
                ('dewey', models.CharField(db_column='Dewey', max_length=25)),
                ('titolo', models.CharField(db_column='Titolo', max_length=250)),
                ('isbn', models.CharField(blank=True, db_column='Isbn', max_length=13, null=True)),
                ('nedizione', models.PositiveIntegerField(blank=True, db_column='Nedizione', null=True)),
                ('annopubblicazione', models.CharField(blank=True, db_column='AnnoPubblicazione', max_length=4, null=True)),
                ('prezzo', models.DecimalField(blank=True, db_column='Prezzo', decimal_places=2, max_digits=6, null=True)),
                ('dataacquisto', models.DateTimeField(blank=True, db_column='dataAcquisto', null=True)),
                ('descrizione', models.TextField(blank=True, db_column='Descrizione', null=True)),
                ('pagine', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('inprestito', models.BooleanField(db_column='InPrestito')),
                ('idstato', models.DecimalField(db_column='IdStato', decimal_places=0, max_digits=2)),
                ('idcollocazione', models.ForeignKey(db_column='IdCollocazione', default='[Vuoto]', on_delete=django.db.models.deletion.SET_DEFAULT, to='libri.Collocazione')),
                ('idedi', models.ForeignKey(db_column='IdEdi', on_delete=django.db.models.deletion.CASCADE, to='libri.Editori')),
            ],
            options={
                'db_table': 'Libri',
            },
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('idsede', models.AutoField(db_column='IdSede', primary_key=True, serialize=False)),
                ('sede', models.CharField(db_column='Sede', max_length=25)),
            ],
            options={
                'db_table': 'Sede',
            },
        ),
        migrations.CreateModel(
            name='Stato',
            fields=[
                ('idstato', models.AutoField(db_column='IdStato', primary_key=True, serialize=False)),
                ('stato', models.CharField(db_column='Stato', max_length=25)),
            ],
            options={
                'db_table': 'Stato',
            },
        ),
        migrations.CreateModel(
            name='Utenti',
            fields=[
                ('idutente', models.AutoField(db_column='IdUtente', primary_key=True, serialize=False)),
                ('cognomenome', models.CharField(db_column='CognomeNome', max_length=60)),
                ('classe', models.CharField(db_column='Classe', max_length=10)),
            ],
            options={
                'db_table': 'Utenti',
            },
        ),
        migrations.CreateModel(
            name='Scarichi',
            fields=[
                ('idlibro', models.OneToOneField(db_column='IdLibro', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='libri.Libri')),
                ('data', models.DateTimeField(db_column='Data')),
                ('motivo', models.CharField(db_column='Motivo', max_length=250)),
            ],
            options={
                'db_table': 'Scarichi',
            },
        ),
        migrations.CreateModel(
            name='Prestiti',
            fields=[
                ('idprestito', models.AutoField(db_column='IdPrestito', primary_key=True, serialize=False)),
                ('dataprelievo', models.DateTimeField(db_column='dataPrelievo')),
                ('datarestituzione', models.DateTimeField(blank=True, db_column='dataRestituzione', null=True)),
                ('idlibro', models.ForeignKey(db_column='IdLibro', on_delete=django.db.models.deletion.CASCADE, to='libri.Libri')),
                ('idutente', models.ForeignKey(db_column='IdUtente', on_delete=django.db.models.deletion.CASCADE, to='libri.Utenti')),
            ],
            options={
                'db_table': 'Prestiti',
            },
        ),
        migrations.AddField(
            model_name='libri',
            name='idsede',
            field=models.ForeignKey(db_column='IdSede', on_delete=django.db.models.deletion.CASCADE, to='libri.Sede'),
        ),
        migrations.CreateModel(
            name='Autorilibri',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('idautore', models.ForeignKey(db_column='IdAutore', on_delete=django.db.models.deletion.CASCADE, to='libri.Autori')),
                ('idlibro', models.ForeignKey(db_column='IdLibro', on_delete=django.db.models.deletion.CASCADE, to='libri.Libri')),
            ],
            options={
                'db_table': 'AutoriLibri',
            },
        ),
    ]
