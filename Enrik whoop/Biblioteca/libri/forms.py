from django import forms 
from .models import Libri, Prestiti, Utenti, Autorilibri
from django_select2 import forms as s2forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Submit, Layout, HTML, Div

# creating a form 
class LibriForm(forms.ModelForm): 
	@property  
	def helper(self):  
		helper = FormHelper()
		helper.form_method = 'post'
		helper.add_input(Submit('submit', 'Conferma', css_class='btn-success'))
		return helper 
	
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
		widgets = {
			'idedi': s2forms.Select2Widget,
			'idcollocazione': s2forms.Select2Widget,
			'idsede': s2forms.Select2Widget,
#			'author': s2forms.ModelSelect2Widget(model=auth.get_user_model(),
#												search_fields=['first_name__istartswith', 'last_name__icontains']),
#			'attending': s2forms.ModelSelect2MultipleWidget …
		}
	
class AutoriLibriForm(forms.ModelForm):
	idlibro = forms.ModelChoiceField(queryset = Libri.objects.all(), disabled = True)

	@property  
	def helper(self):  
		helper = FormHelper()
		helper.form_method = 'post'
		helper.add_input(Submit('submit', 'Conferma', css_class='btn-success'))
		return helper 

	class Meta:
		model = Autorilibri
		fields = [
			'idlibro',
			'idautore',
		]
		widgets = {
			'idautore': s2forms.Select2Widget,
		}

class ApriPrestitiForm(forms.ModelForm):
	idlibro = forms.ModelChoiceField(queryset = Libri.objects.all(), disabled = True)

	@property  
	def helper(self):
		helper = FormHelper()
		helper.form_method = 'post'
		helper.form_tag = False
		helper.add_input(Submit('submit', 'Conferma', css_class='btn-success'))
		return helper 

	class Meta:
		model = Prestiti
		fields = [
			'idlibro',
			'idutente',
		]
		widgets = {
			'idutente': s2forms.Select2Widget,
		}

class ChiudiPrestitiForm(forms.ModelForm):
	idlibro = forms.ModelChoiceField(queryset = Libri.objects.all(), disabled = True)
	idutente = forms.ModelChoiceField(queryset = Utenti.objects.all(), disabled = True)
	datarestituzione = forms.DateTimeField(required = False, widget = forms.HiddenInput())

	@property  
	def helper(self):
		helper = FormHelper()
		helper.form_method = 'post'
		helper.form_tag = False
		helper.add_input(Submit('submit', 'Conferma', css_class='btn-success'))
		return helper 

	class Meta:
		model = Prestiti
		fields = [
			'idlibro',
			'idutente',
			'datarestituzione',
		]

class LibroInPrestitoForm(forms.ModelForm):
	inprestito = forms.BooleanField(required = False, widget = forms.HiddenInput())

	@property  
	def helper(self):
		helper = FormHelper()
		helper.form_method = 'post'
		helper.form_tag = False
		return helper 

	def __init__(self, *args, **kwargs):
		super(LibroInPrestitoForm, self).__init__(*args, **kwargs)
		self.fields['inprestito'].initial = True

	class Meta:
		model = Libri
		fields = ['inprestito']