from django import forms
from .models import Gorev

class GorevForm(forms.ModelForm):
    class Meta:
        model = Gorev
        fields = ['baslik', 'aciklama', 'tamamlandi']
        widgets = {
            'baslik': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Görev başlığı'}),
            'aciklama': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tamamlandi': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
