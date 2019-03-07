from django import forms
from .models import Post, Activity, Seminar, Portfolio
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'thumbnail', )

class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ('title', 'text', 'thumbnail', )

class PortfolioForm(forms.ModelForm):

    class Meta:
        model = Portfolio
        fields = ('title', 'text', 'thumbnail', )

class SeminarForm(forms.ModelForm):

    class Meta:
        model = Seminar
        fields = ('title', 'text', 'thumbnail', )