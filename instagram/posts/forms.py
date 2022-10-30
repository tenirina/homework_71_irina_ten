from django import forms
from django.forms import widgets

from posts.models import Post


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
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ('image', 'description',)

