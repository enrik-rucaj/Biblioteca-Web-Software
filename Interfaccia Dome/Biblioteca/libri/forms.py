from django import forms 
from .models import Libri, Prestiti, Utenti
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML, Div

# creating a form 
class LibriForm(forms.ModelForm): 
	@property  
	def helper(self):  
		helper = FormHelper()
		helper.form_method = 'post'
		helper.add_input(Submit('submit', 'Aggiungi libro'))
		helper.add_layout(Layout(
			'dewey',
			'titolo',
			'immagine',
			'isbn',
			HTML('''
				<div style="padding-bottom: 20px;">
					<p>Editore*</p>
					<select name="list" id="list" style="width: 100%">
						{% for item in form.idedi %}
							<option value="{{ item.ideditore }}">{{ item }}</option>
						{% endfor %}
					</select>
				</div>
			'''),
			'nedizione',
			'annopubblicazione',
			'prezzo',
			'dataacquisto',
			'descrizione',
			'pagine',
			HTML('''
				<div style="padding-bottom: 20px;">
					<p>Collocazione*</p>
					<select name="list2" id="list2" style="width: 100%">
						{% for item in form.idcollocazione %}
							<option value="{{ item.collocazione }}">{{ item }}</option>
						{% endfor %}
					</select>
				</div>
			'''),
			HTML('''
				<div style="padding-bottom: 20px;">
					<p>Sede*</p>
					<select name="list3" id="list3" style="width: 100%">
						{% for item in form.idsede %}
							<option value="{{ item.idsede }}">{{ item }}</option>
						{% endfor %}
					</select>
				</div>
			'''),
			'idstato',
		))
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