from .models import comment
from django.forms import ModelForm

class CommentForm(ModelForm):
    class Meta:
        model = comment
        fields = ['content']