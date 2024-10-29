from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# register form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'input is-primary'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        # Add classes to form fields
        self.fields['username'].widget.attrs.update({'class': 'input is-primary'})
        self.fields['password1'].widget.attrs.update({'class': 'input is-primary'})
        self.fields['password2'].widget.attrs.update({'class': 'input is-primary'})

# login form
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuário', widget=forms.TextInput(attrs={'class': 'input is-primary'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'input is-primary'}))
