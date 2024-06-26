from django import forms
from .models import PostModel


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('name', 'slug', 'image', 'content', 'subject')