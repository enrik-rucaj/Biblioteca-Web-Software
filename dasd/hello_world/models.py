from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.
class Libro(models.Model):
    idLibro=models.IntegerField(primary_key=True,null=False,unique=True,auto_created=True)
    Dewey=models.TextField(default="")
    Titolo=models.TextField(default="")
    Isbn=models.TextField(default="")
    IdEdi=models.BigIntegerField(default=0)
    Nedizione=models.BigIntegerField(default=0)
    AnnoPubblicazione=models.IntegerField(default=0)
    Prezzo=MoneyField(
        decimal_places=2,
        default=0,
        default_currency='EUR',
        max_digits=11,
    )
    dataAcquisto=models.DateTimeField(auto_now=True)
    Descrizione=models.TextField(null=True)
    Pagine=models.IntegerField(default=0)
    IdCollocazione=models.IntegerField(default=0)
    IdSede=models.IntegerField(default=0)
    InPrestito=models.BooleanField(default=False)
    IdStato=models.IntegerField(default=0)

    
    class Meta:
        verbose_name_plural = "Libri"

class Autori(models.Model):
    idAutore=models.IntegerField(primary_key=True,null=False,unique=True,auto_created=True)
    CognomeNome=models.TextField(null=False)
    
    class Meta:
        verbose_name_plural = "Autori"

class AutoriLibri(models.Model):
    