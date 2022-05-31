from django import forms

class StorageForm(forms.Form):
    name = forms.CharField(max_length=50)
    size = forms.IntegerField()
    price = forms.FloatField()


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class SearchForm(forms.Form):
    search = forms.CharField(max_length=10)

class RangesortForm(forms.Form):
    storage1 = forms.IntegerField(min_value=1)
    storage2 = forms.IntegerField(min_value=1)
    storage3 = forms.IntegerField(min_value=1)
    storage4 = forms.IntegerField(min_value=1)

