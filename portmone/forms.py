from django import forms


class ResultForm(forms.Form):

    data = forms.CharField()
