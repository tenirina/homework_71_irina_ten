from django import forms


class SearchForm(forms.Form):
    search_value = forms.CharField(
        required=False,
        label='Search',
        max_length=50
    )

    class Meta:
        fields = ['search_value']
