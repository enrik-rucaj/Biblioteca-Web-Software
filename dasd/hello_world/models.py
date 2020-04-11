# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Autori(models.Model):
    idautore = models.TextField(db_column='IdAutore', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cognomenome = models.TextField(db_column='CognomeNome', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Autori'


class Autorilibri(models.Model):
    idlibro = models.TextField(db_column='IdLibro', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    idautore = models.TextField(db_column='IdAutore', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'AutoriLibri'


class Codicedewey(models.Model):
    iddew = models.TextField(db_column='IdDew', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dew = models.TextField(db_column='Dew', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    argomento = models.TextField(db_column='Argomento', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'CodiceDewey'


class Collocazione(models.Model):
    idcol = models.TextField(db_column='IdCol', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    collocazione = models.TextField(db_column='Collocazione', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Collocazione'


class Editori(models.Model):
    ideditore = models.TextField(db_column='IdEditore', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    editore = models.TextField(db_column='Editore', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Editori'


class Libri(models.Model):
    idlibro = models.TextField(db_column='IdLibro', primary_key=True, null=False)  # Field name made lowercase. This field type is a guess.
    dewey = models.TextField(db_column='Dewey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    titolo = models.TextField(db_column='Titolo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isbn = models.TextField(db_column='Isbn', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    idedi = models.TextField(db_column='IdEdi', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nedizione = models.TextField(db_column='Nedizione', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    annopubblicazione = models.TextField(db_column='AnnoPubblicazione', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prezzo = models.TextField(db_column='Prezzo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dataacquisto = models.TextField(db_column='dataAcquisto', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    descrizione = models.TextField(db_column='Descrizione', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pagine = models.TextField(db_column='Pagine', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    idcollocazione = models.TextField(db_column='IdCollocazione', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    idsede = models.TextField(db_column='IdSede', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    inprestito = models.TextField(db_column='InPrestito', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    idstato = models.TextField(db_column='IdStato', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Libri'


class Prestiti(models.Model):
    idprestito = models.TextField(db_column='IdPrestito', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    idlibro = models.TextField(db_column='IdLibro', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    idutente = models.TextField(db_column='IdUtente', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dataprelievo = models.TextField(db_column='dataPrelievo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    datarestituzione = models.TextField(db_column='dataRestituzione', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Prestiti'


class Scarichi(models.Model):
    idlibro = models.TextField(db_column='IdLibro', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    motivo = models.TextField(db_column='Motivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Scarichi'


class Sede(models.Model):
    idsede = models.TextField(db_column='IdSede', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sede = models.TextField(db_column='Sede', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Sede'


class Stato(models.Model):
    idstato = models.TextField(db_column='IdStato', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stato = models.TextField(db_column='Stato', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Stato'


class Utenti(models.Model):
    idutente = models.TextField(db_column='IdUtente', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cognomenome = models.TextField(db_column='CognomeNome', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    classe = models.TextField(db_column='Classe', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Utenti'
