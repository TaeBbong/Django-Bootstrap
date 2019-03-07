from django import forms
from .models import Post, AdPost, Images
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image', )

class AdPostForm(forms.ModelForm):

    class Meta:
        model = AdPost
        fields = ('title', 'text', 'thumb', 'file', )

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Images
        fields = ('image', )