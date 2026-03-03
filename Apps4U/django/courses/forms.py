from django import forms
from .models import Comment, Material

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)

        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': 'Відповісти...',
                'rows': 1,
                'class': 'comment-input'
            }),
        }

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', "upload"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наприклад: Теореми'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['upload'].required = True
        self.fields['upload'].widget.attrs.update({'required': True})
