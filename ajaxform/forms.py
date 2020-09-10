from django import forms


attr = {'class': 'form-control'}


class TestForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs=attr))
    family = forms.CharField(max_length=100, widget=forms.TextInput(attrs=attr))

