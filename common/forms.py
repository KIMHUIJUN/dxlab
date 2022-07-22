from django import forms
from common.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User  # 사용할 모델
        fields = ['email','username', 'password', 'sex', 'want_field', 'age', 'front_level', 'back_level', 'data_level']  #UserForm 에서 사용할 User 모델의 속성