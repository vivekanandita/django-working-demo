from django import forms
class studentregistrationform(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
