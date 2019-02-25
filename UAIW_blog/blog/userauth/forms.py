from django.forms import Form,ModelForm,ValidationError
from django import forms
from .models import User
from captcha.fields import CaptchaField

class RegisterForm(ModelForm):
    captcha = CaptchaField(label='',required=True,error_messages={"invalid": "验证码错误"})
    class Meta:
        model = User
        exclude = ['img','c','sh','flower','star']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input'}),
            'password': forms.PasswordInput(attrs={'class': 'input'}),
            'email': forms.TextInput(attrs={'class': 'input'}),
            'tel': forms.TextInput(attrs={'class': 'input'}),
        }
        labels = {'username': '用户名','password': '密码','email': "邮箱",'tel': "联系方式"}

class LoginForm(ModelForm):
    captcha = CaptchaField(label='',required=True,error_messages={"invalid": "验证码错误"})
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input'}),
            'password': forms.PasswordInput(attrs={'class': 'input'}),
        }
        labels = {'username': '用户名','password': '密码'}
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username',None)
        password = cleaned_data.get('password',None)
        if username and password:
            res = User.objects.filter(username=username,password=password)
        if not res:
            raise ValidationError("用户名不存在或密码错误")


