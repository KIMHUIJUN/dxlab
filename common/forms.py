from django import forms
from django.contrib.auth.forms import  UserCreationForm

from .models import User


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Reqired.add a vailid email address')
    class Meta:
        model = User
        fields = ('email', 'date_of_birth', 'sex', "want_field",
                  'password1','password2', 'front_level', 'back_level','data_level', )

    def clean_email(self):

        email = self.cleaned_data['email'].lower()
        try:
            account = User.objects.get(email=email)
        except Exception  as e:
            return email

        raise forms.ValidationError(f"Email {email} is already in use.")


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


