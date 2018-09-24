from django import forms
from .models import patient, encounter
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, HTML
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab

class PatientForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = ['first_name', 'last_name', 'age', 'phone', 'photo_permission', 'city', 'heard_of_stand', 'heard_of_stand_how',
                  'refugee_ever', 'refugee_reason', 'previous_patient', 'sex', 'pregnant', 'chief_complaint','card_ID']
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
    card_ID = forms.IntegerField(
        required=True,
        label="Card Number")

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_id = 'demographics'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = "post_demogs/"
        self.helper.layout = Layout(
           Fieldset('What is on their Card?',
                    Field('card_ID', placeholder='Card Number'),
                    HTML("""<br>""")
                    ),
           Fieldset('Personal Information',
                    Field('first_name', placeholder='First Name'),
                    Field('last_name', placeholder="Last Name"),
                    Field('age', placeholder="Age"),
                    InlineRadios('sex'),
                    InlineRadios('pregnant'),
                    InlineRadios('photo_permission'),
                    ),
           Fieldset('Contact data',
                    Field('city', placeholder='From What City?'),
                    Field('phone', placeholder="Phone Number"),
                    ),
           Fieldset('Patient History',
                    InlineRadios('previous_patient'),
                    InlineRadios('refugee_ever'),
                    Field('refugee_reason',placeholder='If yes, why?'),
                    ),
           InlineRadios('heard_of_stand'),
           Field('heard_of_stand_how', placeholder='If yes, how?'),
           Fieldset('Chief Complaint',
                    Field('chief_complaint', placeholder='Why are they here today?'),
                    HTML("""<br>""")
                    )

        )
        self.helper.add_input(Submit('submit', 'Submit'))




class EncounterForm(forms.ModelForm):
    class Meta:
        model = encounter
        fields = ['patient_id', 'Systolic', 'Diastolic', 'Infection_UTI', 'Infection_Vaginal', 'Infection_Other', 'Improvement',
                    'Manual_Therapy', 'Education', 'Exercise', 'Gen_Med', 'Peds', 'Neuro',
                    'Wound', 'Orthotics', 'Prosthetics', 'Cane', 'Crutches',
                    'Walker', 'Wheel_Chair', 'Shoulder', 'Wrist', 'Knee', 'Elbow', 'Back', 'Ankle', 'AFO', 'Provider_Notes',
                  'Supplies_Used', 'Back_Pain', 'Shoes', 'Gen_PT', 'Pelvic_Health', 'Return', 'Discharged', 'Refer_Out']
    Systolic = forms.CharField(
        required=False)
    Diastolic = forms.CharField(
        required=False)
    Infection_UTI = forms.BooleanField(
        required=False)
    Infection_Vaginal = forms.BooleanField(
        required=False)
    Infection_Other = forms.BooleanField(
        required=False)
    Manual_Therapy = forms.BooleanField(
        required=False)
    Education = forms.BooleanField(
        required=False)
    Exercise = forms.BooleanField(
        required=False)
    Gen_Med = forms.BooleanField(
        required=False)
    Peds = forms.BooleanField(
        required=False)
    Neuro = forms.BooleanField(
        required=False)
    Wound = forms.BooleanField(
        required=False)
    Orthotics = forms.BooleanField(
        required=False)
    Prosthetics = forms.BooleanField(
        required=False)
    Gen_PT = forms.BooleanField(
        required=False)
    Pelvic_Health = forms.BooleanField(
        required=False)
    Cane = forms.BooleanField(
        required=False)
    Crutches = forms.BooleanField(
        required=False)
    Walker = forms.BooleanField(
        required=False)
    Wheel_Chair = forms.BooleanField(
        required=False)
    Shoulder = forms.BooleanField(
        required=False)
    Wrist = forms.BooleanField(
        required=False)
    Knee = forms.BooleanField(
        required=False)
    Elbow = forms.BooleanField(
        required=False)
    Back = forms.BooleanField(
        required=False)
    Ankle = forms.BooleanField(
        required=False)
    AFO = forms.BooleanField(
        required=False)
    Back_Pain = forms.BooleanField(
        required=False)
    Shoes = forms.BooleanField(
        required=False)
    Return = forms.BooleanField(
        required=False)
    Discharged = forms.BooleanField(
        required=False)
    Refer_Out = forms.BooleanField(
        required=False)



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
                    'Improvement',
                    HTML("""<img src=/static/images/groc.png width="700" height="200">
                """),
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
                    'Services',
                    'Gen_PT',
                    'Gen_Med',
                    'Peds',
                    'Neuro',
                    'Wound',
                    'Orthotics',
                    'Prosthetics',
                    'Pelvic_Health'
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
                    'Shoes'
                ),
                Tab(
                    'Plan',
                    'Return',
                    'Discharged',
                    'Refer_Out'
                )
            )
        )
        self.helper.add_input(Submit('submit', 'Submit'))

