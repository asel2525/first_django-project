from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):
    # title = forms.CharField(attrs={'class':'form-control'})
    # body = forms.Textarea(attrs={'class':'form-control'})
    class Meta:
        model = Post
        fields = ['title', 'body', ]

    widgets = {
        'title': forms.TextInput(attrs={'class':'forms-control'}),
        'body': forms.TextInput(attrs={'class':'forms-control'}),
        
    }

class SearchForm(forms.Form):

    search_param = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control me-2", 'type':"search", 'placeholder':"Search", 'aria-label':"Search"}))

def add_search_form(request):
    search_form = SearchForm()
    return {'search_form': search_form}
