from .models import Notes
from django.forms import ModelForm, TextInput, NumberInput, DateTimeInput, Textarea

class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description', 'priority', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'описание'
            }),
            "priority": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'приоритет'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'гг.мм.дд 00:00'
            }),
        }
