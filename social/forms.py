from django import forms
from django.forms import ClearableFileInput, SelectMultiple, Select
from .models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='Description du post',
        widget=forms.Textarea(attrs={
            'rows':'3',
            'placeholder':'Dites quelques choses',
            'class':'form-control',
        }))
    image = forms.FileField(
        required=True,
        widget=forms.FileInput(attrs={
            'multiple':True
        })
        )

    class Meta:
        model = Post
        fields = ['body']


class CommentForm(forms.ModelForm):
    commentaire = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows':'2',
            'placeholder':'Commentaire',
            'class':'form-control',
        }))

    class Meta:
        model = Comment
        fields = ['commentaire']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'