from django import forms
from .models import PictureDb


class PictureDbForm(forms.ModelForm):
    class Meta:
        model = PictureDb
        fields = ('name', 'webpage','picture1', 'picture2')
