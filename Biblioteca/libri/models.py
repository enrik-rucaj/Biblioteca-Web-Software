from django.db import models
from django.urls import reverse

class Autori(models.Model):
    idautore = models.AutoField(db_column='IdAutore', primary_key=True)
    cognomenome = models.CharField(db_column='CognomeNome', max_length=60)

    def __str__(self):
        return self.cognomenome

    class Meta:
        verbose_name_plural="Autori"
        db_table = 'Autori'


class Autorilibri(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)
    idlibro = models.ForeignKey('Libri', on_delete=models.CASCADE, db_column='IdLibro')
    idautore = models.ForeignKey('Autori', on_delete=models.CASCADE, db_column='IdAutore')

    class Meta:
        verbose_name_plural="Autorilibri"
        db_table = 'AutoriLibri'


class Codicedewey(models.Model):
    iddew = models.AutoField(db_column='IdDew', primary_key=True)
    dew = models.DecimalField(max_digits=3, decimal_places=0, db_column='Dew')
    argomento = models.CharField(db_column='Argomento', max_length=250)

    def __str__(self):
        return self.dew 
     
    class Meta:
        verbose_name_plural="CodiciDewey"
        db_table = 'CodiceDewey'


class Collocazione(models.Model):
    collocazione = models.CharField(db_column='Collocazione', max_length=250, primary_key=True)

    def __str__(self):
        return self.collocazione

    class Meta:
        verbose_name_plural="Collocazioni"
        db_table = 'Collocazione'


class Editori(models.Model):
    ideditore = models.AutoField(db_column='IdEditore', primary_key=True)
    editore = models.CharField(db_column='Editore', max_length=250)
    
    def __str__(self): 
        return self.editore

    class Meta:
        verbose_name_plural="Editori"
        db_table = 'Editori'


class Libri(models.Model):
    idlibro = models.AutoField(db_column='IdLibro', primary_key=True)
    dewey = models.CharField(db_column='Dewey', max_length=25)
    titolo = models.CharField(db_column='Titolo', max_length=250)
    immagine = models.ImageField(upload_to='images_libri/', db_column='Immagine', blank=True, null=True)
    isbn = models.CharField(db_column='Isbn', max_length=13, blank=True, null=True)
    idedi = models.ForeignKey('Editori', on_delete=models.CASCADE, db_column='IdEdi')
    nedizione = models.PositiveIntegerField(db_column='Nedizione', blank=True, null=True)
    annopubblicazione = models.CharField(db_column='AnnoPubblicazione', max_length=4, blank=True, null=True)
    prezzo = models.DecimalField(max_digits=6, decimal_places=2, db_column='Prezzo', blank=True, null=True)
    dataacquisto = models.DateTimeField(auto_now_add=False, db_column='dataAcquisto', blank=True, null=True)
    descrizione = models.TextField(db_column='Descrizione', blank=True, null=True)
    pagine = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    idcollocazione = models.ForeignKey('Collocazione', on_delete=models.SET_DEFAULT, default='[Vuoto]', db_column='IdCollocazione')
    idsede = models.ForeignKey('Sede', on_delete=models.CASCADE, db_column='IdSede')
    inprestito = models.BooleanField(db_column='InPrestito', default=False)
    idstato = models.DecimalField(max_digits=2, decimal_places=0, db_column='IdStato')

    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name_plural="Libri"
        db_table = 'Libri'

class Prestiti(models.Model):
    idprestito = models.AutoField(db_column='IdPrestito', primary_key=True)
    idlibro = models.ForeignKey('Libri', on_delete=models.CASCADE, db_column='IdLibro')
    idutente = models.ForeignKey('Utenti', on_delete=models.CASCADE, db_column='IdUtente')
    dataprelievo = models.DateTimeField(auto_now_add=True, db_column='dataPrelievo')
    datarestituzione = models.DateTimeField(auto_now_add=False, db_column='dataRestituzione', blank=True, null=True)

    class Meta:
        verbose_name_plural="Prestiti"
        db_table = 'Prestiti'


class Scarichi(models.Model):
    idlibro = models.OneToOneField('Libri', on_delete=models.CASCADE, db_column='IdLibro', primary_key=True)
    data = models.DateTimeField(auto_now_add=False, db_column='Data')
    motivo = models.CharField(db_column='Motivo', max_length=250)

    class Meta:
        verbose_name_plural="Scarichi"
        db_table = 'Scarichi'


class Sede(models.Model):
    idsede = models.AutoField(db_column='IdSede', primary_key=True)
    sede = models.CharField(db_column='Sede', max_length=25)

    def __str__(self):
        return self.sede

    class Meta:
        verbose_name_plural="Sedi"
        db_table = 'Sede'


class Stato(models.Model):
    idstato = models.AutoField(db_column='IdStato', primary_key=True)
    stato = models.CharField(db_column='Stato', max_length=25)

    def __str__(self):
        return str(self.idstato) + self.stato

    class Meta:
        verbose_name_plural="Stati"
        db_table = 'Stato'


class Utenti(models.Model):
    idutente = models.AutoField(db_column='IdUtente', primary_key=True)
    cognomenome = models.CharField(db_column='CognomeNome', max_length=60)
    classe = models.CharField(db_column='Classe', max_length=10)

    def __str__(self):
        return self.cognomenome

    class Meta:
        verbose_name_plural="Utenti"
        db_table = 'Utenti'

