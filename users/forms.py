from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from newsite.models import Post, UserProfile, Comment


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'site_url', 'twitter_url', 'fb_url'
                  , 'github_url']
            
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'site_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'fb_url': forms.TextInput(attrs={'class': 'form-control'}),
            'github_url': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
# The model that will be affected is the User model
# The fields are the ones we want in the form in that order

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'blurb', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'blurb': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'blurb', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'blurb': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }


class EditProfileForm(UserChangeForm):

    email = forms.EmailField(widget=forms.EmailInput
                             (attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput
                                 (attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput
                                (attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput
                               (attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput
                                 (attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'last_login']


class PasswordChangingForm(PasswordChangeForm):

    old_password = forms.EmailField(widget=forms.PasswordInput
                                    (attrs={'class': 'form-control',
                                     'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput
                                    (attrs={'class': 'form-control',
                                     'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput
                                    (attrs={'class': 'form-control',
                                     'type': 'password'}))


    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
