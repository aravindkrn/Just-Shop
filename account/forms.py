from django import forms

from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Reenter Password',
        'class': 'form-control',
    }))

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        PLACEHOLDER = {
            'first_name': 'Enter First name',
            'last_name': 'Enter Last name',
            'email': 'Enter Email',
            'phone_number': 'Enter Phone number'
        }
        for field, text in PLACEHOLDER.items():
            self.fields[field].widget.attrs['placeholder'] = text

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password mismatched!")
