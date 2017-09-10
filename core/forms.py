from django import forms
from .models import patient, encounter
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab

class PatientForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = ['first_name', 'last_name', 'age', 'phone', 'photo_permission', 'city', 'heard_of_stand', 'heard_of_stand_how',
                  'refugee_ever', 'refugee_reason', 'previous_patient', 'sex', 'pregnant', 'chief_complaint']
    first_name = forms.CharField(
        required=True)
    last_name = forms.CharField(
        required=True)
    age = forms.CharField(
        required=True)
    refugee_reason = forms.CharField(
        required=False)
    phone = forms.CharField(
        required=True)
    chief_complaint = forms.CharField(
        required=True)
    heard_of_stand = forms.TypedChoiceField(
        label="Have you heard of Stand before?",
        choices=(('Y', 'Yes'), ('N', 'No')),
        widget=forms.RadioSelect,
        initial='N',
        required=True)
    photo_permission = forms.TypedChoiceField(
        label="Is it ok if we take their photo?",
        choices=(('Y', 'Yes'), ('N', 'No')),
        widget=forms.RadioSelect,
        initial='N',
        required=True)
    heard_of_stand_how = forms.CharField(
        required=False)
    sex = forms.TypedChoiceField(
        label="What sex is the patient?",
        choices=(('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')),
        widget=forms.RadioSelect,
        initial='U',
        required=True)
    pregnant = forms.TypedChoiceField(
        label="Is the patient pregnant?",
        choices=(('Y', 'Yes'), ('N', 'No')),
        widget=forms.RadioSelect,
        initial='N',
        required=True)
    city = forms.CharField(
        label="What city is the patient from?",
        required=True)
    refugee_ever = forms.TypedChoiceField(
        label="Were they ever forced to leave home?",
        choices=(('Y', 'Yes'), ('N', 'No')),
        widget=forms.RadioSelect,
        initial='N',
        required=True)
    refugee_reason = forms.CharField(
        required=False)
    previous_patient = forms.TypedChoiceField(
        label="Have we treated this patient before?",
        choices=(('Y', 'Yes'), ('N', 'No')),
        widget=forms.RadioSelect,
        initial='N',
        required=True)

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_id = 'demographics'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = "post_demogs/"
        self.helper.layout = Layout(
           Fieldset('Personal Information',
                    Field('first_name', placeholder='First Name'),
                    Field('last_name', placeholder="Last Name"),
                    Field('age', placeholder="Age"),
                    InlineRadios('sex'),
                    InlineRadios('pregnant'),
                    InlineRadios('photo_permission'),
                    ),
           Fieldset('Contact data',
                    Field('city', placeholder='What city is the patient from?'),
                    Field('phone', placeholder="Phone Number"),
                    ),
           Fieldset('Patient History',
                    InlineRadios('previous_patient'),
                    InlineRadios('refugee_ever'),
                    Field('refugee_reason',placeholder='If yes, why did they need to leave?'),
                    ),
           InlineRadios('heard_of_stand'),
           Field('heard_of_stand_how', placeholder='If yes, how did they hear of STAND?'),
           Fieldset('Chief Complaint',
                    Field('chief_complaint', placeholder='Why are they here today?')
                    )

        )
        self.helper.add_input(Submit('submit', 'Submit'))




class EncounterForm(forms.ModelForm):
    class Meta:
        model = encounter
        fields = ['patient_id', 'Systolic', 'Diastolic', 'Infection_UTI', 'Infection_Vaginal', 'Infection_Other', 'Improvement',
                    'Manual_Therapy', 'Education', 'Exercise', 'Refer_To_Gen_Med', 'Refer_To_Peds', 'Refer_To_Neuro',
                    'Refer_To_Wound', 'Refer_To_Orthotics', 'Refer_To_Prosthetics', 'Refer_Out_Of_Stand', 'Cane', 'Crutches',
                    'Walker', 'Wheel_Chair', 'Shoulder', 'Wrist', 'Knee', 'Elbow', 'Back', 'Ankle', 'AFO', 'Provider_Notes',
                  'Supplies_Used','Back_Pain']


    def __init__(self, *args, **kwargs):
        super(EncounterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'encounter'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = "post_encounter/"
        self.fields['patient_id'].queryset = patient.objects.all().order_by('-id')
        self.helper.layout = Layout(
            TabHolder(
                Tab(
                    'Patient',
                    'patient_id',
                    'Provider_Notes',
                    'Supplies_Used',
                    'Improvement'
                ),
                Tab(
                    'Condition',
                    'Systolic',
                    'Diastolic',
                    'Back_Pain',
                    'Infection_UTI',
                    'Infection_Vaginal',
                    'Infection_Other',

                ),
                Tab(
                    'Treatment',
                    'Manual_Therapy',
                    'Education',
                    'Exercise',
                ),
                Tab(
                    'Referrals',
                    'Refer_To_Gen_Med',
                    'Refer_To_Peds',
                    'Refer_To_Neuro',
                    'Refer_To_Wound',
                    'Refer_To_Orthotics',
                    'Refer_To_Prosthetics',
                    'Refer_Out_Of_Stand'
                ),
                Tab(
                    'Assistive Devices',
                    'Cane',
                    'Crutches',
                    'Walker',
                    'Wheel_Chair',
                ),
                Tab(
                    'Orthotics',
                    'Shoulder',
                    'Wrist',
                    'Knee',
                    'Elbow',
                    'Back',
                    'Ankle',
                    'AFO',
                )
            )
        )
        self.helper.add_input(Submit('submit', 'Submit'))

