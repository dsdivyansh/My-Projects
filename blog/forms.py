from django import forms
from django.contrib.auth.models import User
from blog.models import Post,Comment

class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']


class post_form(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
