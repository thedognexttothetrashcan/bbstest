from django import forms
from user.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'password', 'age', 'sex', 'icon']

    password2 = forms.CharField(max_length=128)
    print(password2,'qweqweqwewq')

    def clean_password2(self):
        '''检查两次输入是否一致'''
        cleand_data = super().clean()
        if cleand_data['password'] != cleand_data['password2']:
            raise forms.ValidationError('两次输入的密码不一致')
