from django import forms
from .models import UserInfo

class UserInfoFrom(forms.ModelForm):
    class Meta:
        # fields = "__all__"
        exclude = ['u']
        model = UserInfo
        widgets = {
            # 'u': forms.HiddenInput(attrs={'value', ''}),
            "realname": forms.TextInput(attrs={'class': 'input'}),
            "company": forms.TextInput(attrs={'class': 'input'}),
            "position": forms.TextInput(attrs={'class': 'input'}),
            "hobby": forms.TextInput(attrs={'class': 'input'}),
            "reason": forms.Textarea(attrs={'class': 'input input1'}),
        }
        labels = {"company": "公司", "position": "职位", "hobby": "爱好", "realname": "真实姓名", "reason": "原因"}
        def __str__(self):
            return self.name