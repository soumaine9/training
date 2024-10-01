from django import forms
from django.forms import ClearableFileInput, SelectMultiple, Select
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _
from .models import Post, Comment
from django.contrib.auth.models import User



class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='Description du post',
        widget=forms.Textarea(attrs={
            'rows':'3',
            'placeholder':'Dites quelques choses',
            'class':'form-control',
        }))
    image = MultipleFileField(
        label='Images',
        required=True,
    )

    class Meta:
        model = Post
        fields = ['body', 'image']


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
