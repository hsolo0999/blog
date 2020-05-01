from django import forms
from .models import PostModel
from django.core.exceptions import ValidationError



class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('head', 'body', 'img')
        labels = {'head': ('input-head'),
        'body': ('input-body'),
        'img': ('input-img'),}
        widgets = {
                'head': forms.TextInput(attrs={
                                            'class': 'input-head inform',
                                            'placeholder': 'Введите название статьи',
                                            'form': 'mainform'
                                            }),

                'body': forms.Textarea(attrs={
                                            'class': 'input-body inform',
                                            'contenteditable': 'true',
                                            'form': 'mainform'
                                            }),
                                            

                'img': forms.FileInput(attrs={
                                            'class': 'input-img photo',
                                            'type': 'file',
                                            'id': 'imgInput',
                                            'name': 'pic[]',
                                            'form': 'mainform'
                                            }),
                }
                
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        
        return new_slug