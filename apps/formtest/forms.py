from django import forms

class NameForm(forms.Form):
    nome = forms.CharField(label='', max_length=100)
