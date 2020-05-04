from django import forms 
from .models import Libri
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# creating a form 
class LibriForm(forms.ModelForm): 

	# create meta class 
	class Meta: 
		
		model = Libri

		# specify fields to be used 
		fields = [ 
			"titolo", 
			"descrizione"] 
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Aggiungi libro'))
	