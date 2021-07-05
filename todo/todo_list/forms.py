from django import forms
from .models import Liste

class ListForm(forms.ModelForm):
	class Meta:
		model = Liste
		fields = ["item", "completed"]