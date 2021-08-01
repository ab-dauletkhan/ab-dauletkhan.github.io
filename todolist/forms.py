from django import forms
from .models import Customer


class UserRegisterForm(forms.ModelForm):
    user_name = forms.CharField(label="Username")
    email = forms.CharField(label='E-mail', widget=forms.EmailInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('user_name', 'email')

    def clean_password_confirm(self):
        if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
            raise forms.ValidationError('Password doesn\`t \\ match.')
        return self.cleaned_data['password_confirm']
