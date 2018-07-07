from django import forms

class SearchForm(forms.Form):
    # word = forms.CharField(max_length=250)
    a = forms.IntegerField()
    b = forms.IntegerField()
    sum = forms.IntegerField(
        required = False,
    )