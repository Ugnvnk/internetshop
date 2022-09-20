from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, SlugField


class ArticlesForm(ModelForm):

    class Meta:
        model = Articles
        fields = ['title', 'slug', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article title',

            }),
            'slug': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article slug',

            }),

            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article anons',

            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Publication date',

            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Article text',

            })
        }

