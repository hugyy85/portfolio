from django import forms


class SiteForm(forms.Form):
    site = forms.CharField(max_length=128, label='Сайт')

