from django import forms 
from .models import Libri


# creating a form 
class LibriForm(forms.ModelForm): 

	# create meta class 
	class Meta: 
		
		model = Libri

		# specify fields to be used 
		fields = [ 
			"titolo", 
			"descrizione"] 
