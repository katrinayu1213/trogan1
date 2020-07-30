from django import forms
from .models import patient, encounter, pain_catastrophizing_scale, pain_catastrophizing_scale2
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, HTML
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from django.contrib.auth.forms import UserCreationForm
from .models import imp_choices
from .models import UserProfile


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
        required=True)
    last_name = forms.CharField(
        required=True)
    age = forms.CharField(
        required=True,
        label="Age")
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
                    Field('city', placeholder='From What City?'),
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




class EncounterForm(forms.ModelForm):
    class Meta:
        model = encounter
        fields = ['patient_id', 'Systolic', 'Diastolic', 'Infection_UTI', 'Infection_Vaginal', 'Infection_Other', 'Improvement',
                    'Manual_Therapy', 'Education', 'Exercise', 'Gen_Med', 'Peds', 'Neuro',
                    'Wound', 'Orthotics', 'Prosthetics', 'Cane', 'Crutches',
                    'Walker', 'Wheel_Chair', 'Shoulder', 'Wrist', 'Knee', 'Elbow', 'Back', 'Ankle', 'AFO', 'Provider_Notes',
                  'Supplies_Used', 'Back_Pain', 'Shoes', 'Gen_PT', 'Pelvic_Health','general_pain', 'Return', 'Discharged', 'Refer_Out'
                  , 'medication_list']

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
    general_pain = forms.BooleanField(
        required=False)
    Improvement = forms.ChoiceField(
        choices=((neg_five, '-5'), (neg_four, '-4'), (neg_three, '-3'), (neg_two, '-2'), (neg_one, -1), (zero, '0'), (one, '1'),
               (two, '2'), (three, '3'), (four, '4'), (five, '5')),
        initial=0,
        widget=forms.Select,
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
                    'medication_list',
                    'Supplies_Used',
                    'Improvement',
                    HTML("""<img src=/static/images/groc.png width="700" height="200">
                """),
                ),
                Tab(
                    'Condition',
                    'Systolic',
                    'Diastolic',
                    'general_pain',
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

class PCSForm2(forms.ModelForm):
    class Meta:
        model = pain_catastrophizing_scale2
        fields = ['patient_id', 'q1_pcs', 'q2_pcs',]

    # choices
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4

    # field definition
    q1_pcs = forms.ChoiceField(
        choices=((zero, '0 - Not at all'), (one, '1 - to a slight degree'), (two, '2 - to a moderate degree'),
                 (three, '3 - to a great degree'), (four, '4 - all the time')),
        widget=forms.RadioSelect,
        required=False)
    q2_pcs = forms.ChoiceField(
        choices=((zero, '0 - Not at all'), (one, '1 - to a slight degree'), (two, '2 - to a moderate degree'),
                 (three, '3 - to a great degree'), (four, '4 - all the time')),
        widget=forms.RadioSelect,
        required=False)

    def __init__(self, *args, **kwargs):
        super(PCSForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        # you can also remove labels of built-in model properties
        self.fields['name'].label = ''
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
                     HTML("""Mwen toujou ap enkyete’m eske doule sa ap fini"""),
                     ('q1_pcs'),
                     HTML("""<br>"""),

                     HTML("""<br>"""),
                     HTML("""Mwen pa kwe map viv"""),
                     ('q2_pcs'),
                     HTML("""<br>"""),
                ),
        ),

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
        choices=((zero, ' Not at all'), (one, '1 - to a slight degree'), (two, '2 - to a moderate degree'), (three, '3 - to a great degree'), (four, '4 - all the time')),
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
                    HTML("""Mwen toujou ap enkyete’m eske doule sa ap fini"""),
                    ('q1_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""Mwen pa kwe map viv"""),
                    ('q2_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""Li terib et mwen panse li pap janm rale mye"""),
                    ('q3_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""Li pa bon menm mwen santi li komanse depase"""),
                    ('q4_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""Mwen santi’m pa kapab anko"""),
                    ('q5_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""Mwen komanse pe mwen panse doule a ap vinn pi mal"""),
                    ('q6_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""Mwen toujou ap panse ke mwen pral gen nouvo doule"""),
                    ('q7_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""Mwen enkyete anpil mwen vle doule sa fini"""),
                    ('q8_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""Mwen pa panse mwen ka retirel nan panse’m"""),
                    ('q9_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""Mwen toujou ap panse de jan lap fem mal la"""),
                    ('q10_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""Mwen toujou ap panse mwen paka tan pou doule sa fini"""),
                    ('q11_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""Pa gen anyen mwen ka fe poum redui entansite doule a"""),
                    ('q12_pcs'),
                    HTML("""<br>"""),

                    HTML("""<br>"""),
                    HTML("""Map mande eske se pa yon bagay terib ki pral rive"""),
                    ('q13_pcs'),
                    HTML("""<br>"""),
                    ),


        )
        self.helper.add_input(Submit('submit', 'Submit'))