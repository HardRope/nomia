from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import CateringType, Question, Option


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = 'username', 'email', 'password1', 'password2'


class CateringTypeForm(forms.Form):
    catering_types = CateringType.objects.filter()

    CHOICES = [(type.name, type.name) for type in catering_types]

    type = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES
    )


class OptionForm(forms.Form):
    option = forms.ChoiceField(
        widget=forms.RadioSelect,
    )

    def __init__(self, options, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['option'].choices = [(option.text, option.text) for option in options]


class MultipleOptionForm(forms.Form):
    option = forms.ChoiceField(
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, options, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['option'].choices = [(option.text, option.text) for option in options]
