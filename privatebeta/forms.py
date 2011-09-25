from django import forms
from models import InviteRequest

class InviteRequestForm(forms.ModelForm):
    class Meta:
        model = InviteRequest
        fields = ['email']
