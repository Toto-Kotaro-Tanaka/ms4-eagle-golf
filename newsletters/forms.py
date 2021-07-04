from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = ['newsletter_email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.keys():
            sefl.fields[field].widget.attrs['class'] = 'form-control'