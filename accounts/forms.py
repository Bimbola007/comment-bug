from django.contrib.auth.forms import UserCreationForm , UserChangeForm

from  .models import CustomUser

from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['age','email',]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        #fields = UserCreationForm.Meta.fields
        fields = ['age', 'email', ]

