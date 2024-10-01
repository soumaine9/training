from django import forms
from . models import Post, Image

class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows':'',
            'placeholder':'Mettez le titre du post'
        }))
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows':'3',
            'placeholder':'Mettez la Description du post'
        }))
    image = forms.ImageField(
        required=False,
'''        widget=forms.ClearableFileInput(attrs={
            'multiple':True
        } )'''
    )    

    class Meta:
        model = Post
        fields = ('title','body')

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label = 'Image')

    class Meta:
        model = Images
        fields = ['image']
        widget = {}