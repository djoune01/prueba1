from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Purchase

from django.contrib.auth.forms import PasswordChangeForm

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})

# 用户注册表单
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),  # 用户名输入框的HTML属性设置
            'password1': forms.TextInput(attrs={'class': 'form-control'}),  # 密码输入框的HTML属性设置
            'password2': forms.TextInput(attrs={'class': 'form-control'}),  # 密码确认输入框的HTML属性设置
        }

# 购买表单
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['product_id', 'name', 'quantity', 'amount']
        widgets = {
            'product_id': forms.TextInput(attrs={'class': 'form-control'}),  # 商品ID输入框的HTML属性设置
            'name': forms.TextInput(attrs={'class': 'form-control'}),  # 名称输入框的HTML属性设置
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),  # 数量输入框的HTML属性设置
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),  # 金额输入框的HTML属性设置
        }

