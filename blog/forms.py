from django import forms
from .models import PostModel
from django.core.exceptions import ValidationError



class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('head', 'body', 'img')
        labels = {'head': ('input-head'),
        'body': ('input-body'),
        'img': ('img-input'),}
        widgets = {
                'head': forms.TextInput(attrs={
                                            'class': 'input-head',
                                            'placeholder': 'Введите название статьи'}),

                'body': forms.Textarea(attrs={
                                            'contenteditable': 'true'}),
                                            

                'img': forms.FileInput(attrs={
                                            'type': 'file',
                                            'id': 'uploade-file',
                                            }),
                }
                
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        
        return new_slug