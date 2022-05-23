from logging import PlaceHolder
from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'PlaceHolder': 'Title'}),
            'author': forms.Select(attrs={'class': 'form-control', 'PlaceHolder': 'Author'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'PlaceHolder': 'Body'})
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('title', 'image', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'PlaceHolder': 'Title'}),
            # 'author': forms.Select(attrs={'class': 'form-control', 'PlaceHolder': 'Author'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'PlaceHolder': 'Body'})
        }
