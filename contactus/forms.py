from  django import forms 

class KhabarnameForm(forms.Form):
    email = forms.EmailField(max_length=254)
