from django import forms
from .models import *


class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "full_name",
            "card_ID",
            "age",
            "sex",
            "tel",
            "address",
        ]


class ContactEditForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "full_name",
            "card_ID",
            "sex",
            "age",
            "tel",
            "address",
        ]

class SearchContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields = [
            "tel"
        ]
