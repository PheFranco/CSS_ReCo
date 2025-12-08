from django import forms
from .models import Donation, Message

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['title', 'description', 'condition', 'city', 'contact_email', 'contact_phone', 'is_available', 'image']
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'condition': 'Condição',
            'city': 'Cidade',
            'contact_email': 'E-mail de contato',
            'contact_phone': 'Telefone de contato',
            'is_available': 'Disponível',
            'image': 'Imagem',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows':4, 'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'condition': forms.Select(attrs={'class':'form-select'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class':'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class':'form-control'}),
            'is_available': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control'}),
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'image']
        labels = {
            'text': 'Mensagem',
            'image': 'Imagem (opcional)',
        }
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Escreva sua mensagem...',
                'id': 'message-input',
                'required': 'required'
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text', '').strip()
        
        # Validar que o texto não está vazio
        if not text:
            raise forms.ValidationError('A mensagem não pode estar vazia.')
        
        return cleaned_data