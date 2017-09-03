from django import forms
from .models import patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = ['patient_id', 'first_name', 'last_name', 'sex', 'age', 'phone', 'city', 'city_other', 'heard_of_stand', 'heard_of_stand_how',
                  'refugee_ever', 'refugee_reason', 'previous_patient', 'pregnant']
