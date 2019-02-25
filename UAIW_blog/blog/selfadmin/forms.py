from .models import Artical
from django.forms import Form,ModelForm,ValidationError
from ckeditor.fields import RichTextField
from django import forms

class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Artical
        exclude = ['a', 'c_time', 'u_time', 'look', 'status']
        widgets = {
            'c' : forms.Select(attrs={'class': 'form-control', 'id': 'exampleFormControlSelect1'}),
            'k' : forms.Select(attrs={'class': 'form-control', 'id': 'exampleFormControlSelect1'}),
            'title' : forms.TextInput(attrs={'class': 'form-control input-full', 'id': 'inlineinput'}),
            'con' : forms.Textarea(attrs={'class':'form-control', 'id': 'comment', 'rows': '5'})
        }
        labels = {"c": "分类", "k": "关键词", "title": "标题", "con": "内容"}
        def __str__(self):
            return self.name