from django import forms
from .models import patient, encounter


class PatientForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First Name...'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last Name...'
        }
    ))
    age = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Age...'
        }
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Phone...'
        }
    ))

    city_other = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': "If you marked 'other', what city?"
        }
    ))
    heard_of_stand_how = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'If No, How did they hear of us?'
        }
    ))
    refugee_reason = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'If No, Reason Forced from home...'
        }
    ))
    chief_complaint = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Chief Complaint...'
        }
    ))


    class Meta:
        model = patient
        fields = ['first_name', 'last_name', 'age', 'phone', 'city', 'city_other', 'heard_of_stand', 'heard_of_stand_how',
                  'refugee_ever', 'refugee_reason', 'previous_patient', 'sex', 'pregnant']

class EncounterForm(forms.ModelForm):
    class Meta:
        model = encounter
        fields = ['patient_id', 'back_pain', 'fever', 'wheelchair', 'manipulation', 'needling', 'cupping', 'improvement',
                  'ref_gen_med', 'ref_ortho', 'ref_prosth', 'ref_out', 'provider_notes', 'supplies_used',]
