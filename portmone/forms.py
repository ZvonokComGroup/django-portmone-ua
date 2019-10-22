from django import forms


class ResultForm(forms.Form):

    data = forms.CharField()


class RequestForm(forms.Form):

    bodyRequest = forms.CharField()
    typeRequest = forms.CharField(initial='json')
