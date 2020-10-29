from django import forms
from captcha.fields import CaptchaField
from . import initsettings


class UserReg(forms.Form):
    users = forms.CharField(label="用户名", max_length=16, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    passwd = forms.CharField(label="密码", max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                             required=True)
    passwdconfirm = forms.CharField(label="确认密码", max_length=16,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    email = forms.EmailField(label="邮箱", required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    confirm = CaptchaField(label="验证码")


class UserLogin(forms.Form):
    users = forms.CharField(label="用户名", max_length=16, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    passwd = forms.CharField(label="密码", max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                             required=True)


class AddData(forms.Form):
    name = forms.CharField(label="学生姓名", max_length=10, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    yuanxi = forms.ChoiceField(label="院系",choices=initsettings.yuanxi, required=True)
    detail = forms.CharField(max_length=3000,required=True,label="事件",widget=forms.TextInput(attrs={'class': 'form-control','rows':'10'}))
    date = forms.DateField(label="日期", widget=forms.DateInput())
