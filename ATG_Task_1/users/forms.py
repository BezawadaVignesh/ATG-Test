from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from .models import CustomUser, PProfile, DProfile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'image',
                  'address', 'zip', 'ph', 'password1', 'password2']


class PProfileCreationForm(forms.ModelForm):
    class Meta:
        model = PProfile
        fields = ['Occupation', 'i_company_name', 'symptom']


class DProfileCreationForm(forms.ModelForm):
    class Meta:
        model = DProfile
        fields = ['exp_in_years', 'edu', 'awards', 'fee_charged']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'image', 'address', 'zip', 'ph']


class PProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = PProfile
        fields = ['Occupation', 'i_company_name', 'symptom']


class DProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = DProfile
        fields = ['exp_in_years', 'edu', 'awards', 'fee_charged']

