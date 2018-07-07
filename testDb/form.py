from django import forms

class UserForm(forms.Form):
    # word = forms.CharField(max_length=250)
    name = forms.CharField(
        required = False,
    )
    age = forms.IntegerField(
        required = False,
    )
