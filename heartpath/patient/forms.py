from django import forms
from patient.models import PatientDetails

class PatientForm(forms.ModelForm):
    class Meta:
        model=PatientDetails
        fields="__all__"