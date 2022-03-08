from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
# The model that will be affected is the User model
# The fields are the ones we want in the form in that order
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'content')

        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control',
                                     'placeholder': ''}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control',
                                         'placeholder': ''}),
            'author': forms.Select(attrs={'class': 'form-control',
                                   'placeholder': ''}),
            'content': forms.Textarea(attrs={'class': 'form-control',
                                      'placeholder': ''})
        }
