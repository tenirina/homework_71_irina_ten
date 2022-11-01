from django import forms
from django.forms import widgets

from posts.models import Post, Comment


class SearchForm(forms.Form):
    search_value = forms.CharField(
        required=False,
        label='Search',
        max_length=50
    )

    class Meta:
        fields = ['search_value']


class PostForm(forms.ModelForm):
    description = forms.CharField(required=False, label='Description', max_length=150, widget=widgets.Textarea,)
    image = forms.ImageField(required=True)

    class Meta:
        model = Post
        fields = ('image', 'description',)


class CommentForm(forms.ModelForm):
    text = forms.CharField(required=False, label='Comment', max_length=150, widget=widgets.Textarea, )

    class Meta:
        model = Comment
        fields = ('author', 'text', 'post',)

