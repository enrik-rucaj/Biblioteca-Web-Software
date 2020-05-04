from django import forms 
from .models import Libri, Prestiti


# creating a form 
class LibriForm(forms.ModelForm): 
	class Meta: 
		model = Libri
		fields = [ 
			"titolo", 
			"descrizione"
		] 

class PrenotaLibroForm(forms.ModelForm):
	class Meta:
		model = Libri
		fields = [
			"inprestito",
		]

class PrestitoLibroForm(forms.ModelForm):
	class Meta:
		model = Prestiti
		fields = [
			"idlibro",
			"idutente",
			"dataprelievo",
		]
