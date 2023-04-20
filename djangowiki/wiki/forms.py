from django import forms

from .models import Article


INPUT_CLASSES = ""


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'content': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
        }


class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'content': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
        }
