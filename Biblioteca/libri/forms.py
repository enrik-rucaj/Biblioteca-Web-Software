from django import forms 
from .models import Libri, Prestiti, Utenti
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# creating a form 
class LibriForm(forms.ModelForm): 
	helper = FormHelper()
	helper.form_method = 'post'
	helper.add_input(Submit('submit', 'Aggiungi libro'))
	
	class Meta: 
		model = Libri
		fields = [
			'dewey',
			'titolo',
			'immagine',
			'isbn',
			'idedi',
			'nedizione',
			'annopubblicazione',
			'prezzo',
			'dataacquisto',
			'descrizione',
			'pagine',
			'idcollocazione',
			'idsede',
			'idstato',
		]
	
class ApriPrestitiForm(forms.ModelForm):
	idlibro = forms.ModelChoiceField(queryset = Libri.objects.all(), disabled = True)
	class Meta:
		model = Prestiti
		fields = [
			'idlibro',
			'idutente',
			'datarestituzione',
		]

class ChiudiPrestitiForm(forms.ModelForm):
	idlibro = forms.ModelChoiceField(queryset = Libri.objects.all(), disabled = True)
	idutente = forms.ModelChoiceField(queryset = Utenti.objects.all(), disabled = True)
	datarestituzione = forms.DateTimeField(required = False, widget = forms.HiddenInput())
	class Meta:
		model = Prestiti
		fields = [
			'idlibro',
			'idutente',
			'datarestituzione',
		]

class LibroInPrestitoForm(forms.ModelForm):
	inprestito = forms.BooleanField(required = False, widget = forms.HiddenInput())
	class Meta:
		model = Libri
		fields = ['inprestito']