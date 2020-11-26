from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ('created_by','title','body')


class CommentForm(forms.ModelForm):
    class Meta:
        model =Comment
        fields = ('comment_by','body','like_status')
        widgets = {'like_status': forms.RadioSelect()}