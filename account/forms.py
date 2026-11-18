from django import forms
from django.contrib.auth import get_user_model
class RegisterForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 
                  'first_name',
                  'username',
                  'password',
                  'phone_number'
                  ]

class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=50)
    password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput())
    