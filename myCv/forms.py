from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Your name'}), 
        'email': forms.EmailInput(attrs={'placeholder': 'Your email'}),
        'message': forms.Textarea(attrs={'placeholder': 'Type your message'})}