from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from registration.forms import RegistrationForm


class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['Admin', 'pub_date', 'admin_profile']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 1, 'cols': 10, }),
        }


class NewNeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['Admin', 'pub_date', 'admin_profile']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 2, 'cols': 10, }),
        }


class RegisterForm(RegistrationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        # self.helper = FormHelper()
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.helper.form_show_labels = True


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['Author', 'pub_date', 'author_profile', 'neighborhood']
        widgets = {
            'post': forms.Textarea(attrs={'rows': 2, 'cols': 10, }),
        }
