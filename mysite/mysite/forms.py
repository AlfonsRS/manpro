from django import forms
from django.core import validators

class ContactForm(forms.Form):
	email = forms.EmailField()
	subject = forms.CharField(widget=forms.Textarea)
	honeypot = forms.CharField(widget=forms.HiddenInput, required=False, validators = [validators.MaxLengthValidator(0)])

	# def clean_honeypot(self):
	# 	honeypot = self.cleaned_data['honeypot']
	# 	if len(honeypot):
	# 		raise forms.ValidationError('ngga boleh diisi dong')
	# 	return honeypot