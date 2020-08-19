from django import forms
from .models import patient, encounter, pain_catastrophizing_scale, GMEncounter, UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, HTML
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from django.contrib.auth.forms import UserCreationForm
from .models import imp_choices

class RegistrationWithRole(forms.ModelForm):
    role = forms.CharField(
        required=True,
        widget=forms.Select(choices=(('PT', 'Physical Therapy'), ('GM', 'General Medicine'), ('Admin', 'Admin'))))

    class Meta:
        model = UserProfile
        fields = ('role', )


class PatientForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = ['first_name', 'last_name', 'age', 'phone', 'photo_permission', 'city', 'heard_of_stand', 'heard_of_stand_how',
                  'refugee_ever', 'refugee_reason', 'recent_earthquake', 'previous_patient', 'sex', 'pregnant', 'chief_complaint', 'card_ID']
    first_name = forms.CharField(
        label="First Name",
        required=True)
    last_name = forms.CharField(
        label="Last Name",
        required=True)
    age = forms.CharField(
        required=True,
        label="Age")
    refugee_reason = forms.CharField(
        required=False)
    phone = forms.CharField(
        required=True)
    heard_of_stand = forms.TypedChoiceField(
        label="Have you heard of STAND before?",
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
    recent_earthquake = forms.TypedChoiceField(
        label="Were you injured in the recent earthquake?",
        choices=(('Y', 'Yes'), ('N', 'No')),
        widget=forms.RadioSelect,
        initial='N',
        required=False
    )
    previous_patient = forms.TypedChoiceField(
        label="Have we treated this patient before?",
        choices=(('Y', 'Yes'), ('N', 'No')),
        widget=forms.RadioSelect,
        initial='N',
        required=True)
    card_ID = forms.IntegerField(
        required=True,
        label="Card Number")
    order_ID = 0


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
                    Field('city', placeholder='What City?'),
                    Field('phone', placeholder="Phone Number"),
                    ),
           Fieldset('Patient History',
                    InlineRadios('previous_patient'),
                    InlineRadios('refugee_ever'),
                    Field('refugee_reason',placeholder='If yes, why?'),
                    InlineRadios('recent_earthquake')
                    ),
           InlineRadios('heard_of_stand'),
           Field('heard_of_stand_how', placeholder='If yes, how?'),
           Fieldset('Chief Complaint',
                    Field('chief_complaint', placeholder='Why are they here today?'),
                    HTML("""<br>""")
                    )

        )
        self.helper.add_input(Submit('submit', 'Submit'))


class GMEncounterForm(forms.ModelForm):
    class Meta:
        model = GMEncounter
        fields = ['patient_id', 'GM_Provider_Notes', 'Systolic', 'Diastolic', 'GM_Medicine_List']

    def __init__(self, *args, **kwargs):
        super(GMEncounterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True;
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label
            field.label = ''
        # self.use_custom_control = True
        self.helper.form_id = 'pcs'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = "post_pcs/"
        self.fields['patient_id'].queryset = patient.objects.all().order_by('-id')
        self.helper.layout = Layout(
            Fieldset('Patient ID',
                     'patient_id',
                     ),
                    HTML("""<br>"""),
                    HTML("""<h4 class="customizedLabel">Blood pressure</h4>"""),
                    'Systolic',
                    'Diastolic',
                    HTML("""<br>"""),
                    HTML("""<h4 class="customizedLabel">Medicine List</h4>"""),
                    'GM_Medicine_List',
                    HTML("""<br>"""),
                    HTML("""<br>"""),
                    HTML("""<h4 class="customizedLabel">Provider Notes</h4>"""),
                    'GM_Provider_Notes',
                    HTML("""<br>"""),


        )
        self.helper.add_input(Submit('submit', 'Submit'))


class EncounterForm(forms.ModelForm):
    class Meta:
        model = encounter
        fields = ['patient_id', 'Systolic', 'Diastolic', 'Common_Diagnoses',
                  'Improvement', 'Patient_Type', 'Orthotics', 'Prosthetics', 'Cane', 'Crutches',
                  'Cupping', 'Tape', 'Dry_Needle', 'Walker', 'Wheel_Chair', 'Shoulder', 'Wrist', 'Knee', 'Elbow', 'Back',
                  'Ankle', 'AFO', 'Provider_Notes', 'Supplies_Used', 'Back_Pain', 'Shoes']
        # 'Next_Steps', 'Return', 'Discharged', 'Refer_Out'

    # choices
    neg_five = -5
    neg_four = -4
    neg_three = -3
    neg_two = -2
    neg_one = -1
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5

    #field definition
    Systolic = forms.CharField(
        required=False)
    Diastolic = forms.CharField(
        required=False)
    general_pain = forms.BooleanField(
        required=False)
    Infection_UTI = forms.BooleanField(
        required=False)
    Infection_Vaginal = forms.BooleanField(
        required=False)
    Infection_Other = forms.BooleanField(
        required=False)
    Peds = forms.BooleanField(
        required=False)
    Neuro = forms.BooleanField(
        required=False)
    Wound = forms.BooleanField(
        required=False)
    Prosthetics = forms.BooleanField(
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
    Cupping = forms.BooleanField(
        required=False)
    Tape = forms.BooleanField(
        required=False)
    Dry_Needle = forms.BooleanField(
        required=False)
    Return = forms.BooleanField(
        required=False)
    Discharged = forms.BooleanField(
        required=False)
    Refer_Out = forms.BooleanField(
        required=False)
    Next_Steps = forms.ChoiceField(
        choices=((Return, 'Return'), (Discharged, 'Discharged'), (Refer_Out, 'Refer Out')),
        initial=0,
        widget=forms.CheckboxSelectMultiple,
        required=False)
    Improvement = forms.ChoiceField(
        choices=((neg_five, '-5'), (neg_four, '-4'), (neg_three, '-3'), (neg_two, '-2'), (neg_one, -1), (zero, '0'), (one, '1'),
               (two, '2'), (three, '3'), (four, '4'), (five, '5')),
        initial=0,
        widget=forms.Select,
        required=False)
    Common_Diagnoses = forms.ChoiceField(
        choices=((general_pain, 'General Pain'), (Back_Pain, 'Back Pain'), (Infection_UTI, 'Infection UTI'), (Infection_Vaginal, 'Infection Vaginal'), (Infection_Other, 'Infection Other')),
        initial=0,
        widget=forms.CheckboxSelectMultiple,
        required=False)
    Patient_Type = forms.ChoiceField(
        choices=((Pelvic_Health, 'Pelvic Health'), (Wound, 'Wound'), (Neuro, 'Neuro'), (Peds, 'Peds')),
        initial=0,
        widget=forms.CheckboxSelectMultiple,
        required=False)
    Common_Supplies = forms.ChoiceField(
        choices=((Cupping, 'Cupping'), (Tape, 'Tape'), (Dry_Needle, 'Dry Needle')),
        initial=0,
        widget=forms.CheckboxSelectMultiple,
        required=False)
    Assistive_Devices = forms.ChoiceField(
        choices=((Cane, 'Cane'), (Crutches, 'Crutches'), (Walker, 'Walker'), (Wheel_Chair, 'Wheel Chair')),
        initial=0,
        widget=forms.CheckboxSelectMultiple,
        required=False)
    Orthotic_Devices = forms.ChoiceField(
        choices=((Shoulder, 'Shoulder'), (Wrist, 'Wrist'), (Knee, 'Knee'), (Elbow, 'Elbow'), (Back, 'Back'), (Ankle, 'Ankle'), (AFO, 'AFO'), (Shoes, 'Shoes')),
        initial=0,
        widget=forms.CheckboxSelectMultiple,
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
                    'Common_Diagnoses',
                    'Patient_Type',
                    'Systolic',
                    'Diastolic',
                    'Next_Steps',
                    'Improvement',
                    HTML("""<img id="groc" src=/static/images/groc.png width="700" height="200">"""),
                ),
                Tab(
                    'Supplies',
                    'Common_Supplies',
                    'Assistive_Devices',
                    'Orthotic_Devices'

                ),
            )
        )
        self.helper.add_input(Submit('submit', 'Submit'))


class PCSForm(forms.ModelForm):
    class Meta:
        model = pain_catastrophizing_scale
        fields = ['patient_id', 'q1_pcs', 'q2_pcs', 'q3_pcs','q4_pcs', 'q5_pcs', 'q6_pcs', 'q7_pcs', 'q8_pcs',  'q9_pcs', 'q10_pcs',
         'q11_pcs', 'q12_pcs', 'q13_pcs',]

    # choices
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4


    #field definition
    q1_pcs = forms.ChoiceField(
        choices=((zero, '0 - Not at all'), (one, '1 - to a slight degree'), (two, '2 - to a moderate degree'), (three, '3 - to a great degree'), (four, '4 - all the time')),
        widget=forms.RadioSelect,
        required=False)
    q2_pcs = forms.ChoiceField(
        choices=((zero, '0 - Not at all'), (one, '1 - to a slight degree'), (two, '2 - to a moderate degree'),
                 (three, '3 - to a great degree'), (four, '4 - all the time')),
        widget=forms.RadioSelect,
        required=False)
    q3_pcs = forms.ChoiceField(
        choices=((zero, '0 - Not at all'), (one, '1 - to a slight degree'), (two, '2 - to a moderate degree'),
                 (three, '3 - to a great degree'), (four, '4 - all the time')),
        widget=forms.RadioSelect,
        required=False)
    q4_pcs = forms.ChoiceField(
        choices=((zero, '0 - Not at all'), (one, '1 - to a slight degree'), (two, '2 - to a moderate degree'),
                 (three, '3 - to a great degree'), (four, '4 - all the time')),
        widget=forms.RadioSelect,
        required=False)
    q5_pcs = forms.ChoiceField(
        choices=((zero, '0 - Not at all'), (one, '1 - to a slight degree'), (two, '2 - to a moderate degree'),
                 (three, '3 - to a great degree'), (four, '4 - all the time')),
        widget=forms.RadioSelect,
        required=False)

    q6_pcs = forms.ChoiceField(
        choices=((zero, '0 - Not at all'), (one, '1 - to a slight degree'), (two, '2 - to a moderate degree'),
                 (three, '3 - to a great degree'), (four, '4 - all the time')),
        widget=forms.RadioSelect,
        required=False)
    q7_pcs = forms.ChoiceField(
        choices=((zero, '0 - Not at all'), (one, '1 - to a slight degree'), (two, '2 - to a moderate degree'),
                 (three, '3 - to a great degree'), (four, '4 - all the time')),
        widget=forms.RadioSelect,
        required=False)
    q8_pcs = forms.ChoiceField(
        choices=((zero, '0 - Not at all'), (one, '1 - to a slight degree'), (two, '2 - to a moderate degree'),
                 (three, '3 - to a great degree'), (four, '4 - all the time')),
        widget=forms.RadioSelect,
        required=False)
    q9_pcs = forms.ChoiceField(
        choices=((zero, '0 - Not at all'), (one, '1 - to a slight degree'), (two, '2 - to a moderate degree'),
                 (three, '3 - to a great degree'), (four, '4 - all the time')),
        widget=forms.RadioSelect,
        required=False)
    q10_pcs = forms.ChoiceField(
        choices=((zero, '0 - Not at all'), (one, '1 - to a slight degree'), (two, '2 - to a moderate degree'),
                 (three, '3 - to a great degree'), (four, '4 - all the time')),
        widget=forms.RadioSelect,
        required=False)
    q11_pcs = forms.ChoiceField(
        choices=((zero, '0 - Not at all'), (one, '1 - to a slight degree'), (two, '2 - to a moderate degree'),
                 (three, '3 - to a great degree'), (four, '4 - all the time')),
        widget=forms.RadioSelect,
        required=False)
    q12_pcs = forms.ChoiceField(
        choices=((zero, '0 - Not at all'), (one, '1 - to a slight degree'), (two, '2 - to a moderate degree'),
                 (three, '3 - to a great degree'), (four, '4 - all the time')),
        widget=forms.RadioSelect,
        required=False)
    q13_pcs = forms.ChoiceField(
        choices=((zero, '0 - Not at all'), (one, '1 - to a slight degree'), (two, '2 - to a moderate degree'),
                 (three, '3 - to a great degree'), (four, '4 - all the time')),
        widget=forms.RadioSelect,
        required=False)

    def __init__(self, *args, **kwargs):
        super(PCSForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label
            field.label = ''
        # self.use_custom_control = True
        self.helper.form_id = 'pcs'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = "post_pcs/"
        self.fields['patient_id'].queryset = patient.objects.all().order_by('-id')
        self.helper.layout = Layout(
            Fieldset('Patient ID',
                     HTML("""<br>"""),
                     'patient_id',
                     HTML("""<br>"""),
                     HTML("""<br>"""),
                     ),
           Fieldset('PCS',
                    HTML("""<br>"""),
                    HTML("""1. Mwen toujou ap enkyete’m eske doule sa ap fini"""),
                    ('q1_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""2. Mwen pa kwe map viv"""),
                    ('q2_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""3. Li terib et mwen panse li pap janm rale mye"""),
                    ('q3_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""4. Li pa bon menm mwen santi li komanse depase"""),
                    ('q4_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""5. Mwen santi’m pa kapab anko"""),
                    ('q5_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""6. Mwen komanse pe mwen panse doule a ap vinn pi mal"""),
                    ('q6_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""7. Mwen toujou ap panse ke mwen pral gen nouvo doule"""),
                    ('q7_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""8. Mwen enkyete anpil mwen vle doule sa fini"""),
                    ('q8_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""9. Mwen pa panse mwen ka retirel nan panse’m"""),
                    ('q9_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""10. Mwen toujou ap panse de jan lap fem mal la"""),
                    ('q10_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""11. Mwen toujou ap panse mwen paka tan pou doule sa fini"""),
                    ('q11_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""12. Pa gen anyen mwen ka fe poum redui entansite doule a"""),
                    ('q12_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""13. Map mande eske se pa yon bagay terib ki pral rive"""),
                    ('q13_pcs'),
                    HTML("""<br>"""),
                    ),


        )
        self.helper.add_input(Submit('submit', 'Submit'))