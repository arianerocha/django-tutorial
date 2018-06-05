
from django import forms
from .models import Comment

# Criando formulário à partir do Model `Comment`
# https://docs.djangoproject.com/pt-br/2.0/topics/forms/modelforms/#modelform
class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # atribuindo classes 'CSS' aos campos do form
        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-lg', 'required': True})
        self.fields['text'].widget.attrs.update({'class': 'form-control form-control-lg', 'required': True})
        # Colocando o Post como um campo invisível no formulário
        self.fields['post'].widget = forms.widgets.HiddenInput()

    class Meta:
        model = Comment
        # Apenas estes campos serão apresentados no formulário html
        fields = ['name', 'text', 'post']
