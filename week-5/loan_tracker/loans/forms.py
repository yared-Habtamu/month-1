from django.forms import forms
from django import forms
from .models import Loan


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['name', 'amount', 'date_issued', 'reason']
        widgets = {
            'date_issued': forms.DateInput(attrs={'type': 'date'}),
        }
