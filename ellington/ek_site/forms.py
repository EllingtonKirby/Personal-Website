__author__ = 'Ellioc'
from django import forms

class ContactForm(forms.Form):
    sender = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
