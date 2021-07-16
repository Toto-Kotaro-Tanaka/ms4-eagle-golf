from django import forms
from .models import Newsletter


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('subscribe_email',)