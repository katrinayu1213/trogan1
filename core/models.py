from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings

#Model standard options

# sex
Male = 'M'
Female = 'F'
sex_unknown = 'U'
sex_choices = ((Male, 'Male'), (Female, 'Female'), (sex_unknown, 'Unknown'))

# city
port_au_prince = 'PAP'
port_de_paix = 'PDP'
city_unknown = 'U'
other = 'O'
city_choices = (
(port_au_prince, 'Port au Prince'), (port_de_paix, 'Port de Paix'), (city_unknown, 'Unknown'), (other, 'Other'))

# yes/no
Yes = 'Y'
No = 'N'
yes_no_choices = ((Yes, 'Yes'), (No, 'No'))

# status choices
waiting = 'W'
being_seen = 'B'
discharged = 'D'
no_show = 'NS'
returning = 'R'
status_choices = ((waiting, 'Waiting'), (being_seen, 'Being Seen'), (discharged, 'Discharged'), (no_show, 'No Show'),
                  (returning, 'Returning later'))

# department
pt = 'PT'
gen_med = 'GM'
wound = 'W'
prosth = 'P1'
peds = 'P2'
pelvic = 'P3'

dept_choices = ((pt, 'Physical Therapy'), (gen_med, 'Gen Med'), (wound, 'Wound'), (prosth, 'Prosthetics'), (peds, 'Peds'), (pelvic, 'Pelvic'))

# improvement
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
imp_choices = ((neg_five, '-5'), (neg_four, '-4'), (neg_three, '-3'), (neg_two, '-2'), (neg_one, -1), (zero, '0'), (one, '1'),
               (two, '2'), (three, '3'), (four, '4'), (five, '5'))



# Create your models here.
class patient(models.Model):

    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=sex_choices, default=sex_unknown)
    age = models.CharField(max_length=10, blank=False)
    phone = models.CharField(max_length=50, default='1')
    city = models.CharField(max_length=50)
    heard_of_stand = models.CharField(max_length=1, choices=yes_no_choices, default=No)
    heard_of_stand_how = models.CharField(max_length=200, blank=True)
    refugee_ever = models.CharField(max_length=1, choices=yes_no_choices, default=No)
    refugee_reason = models.CharField(max_length=500, blank=True)
    previous_patient = models.CharField(max_length=1, choices=yes_no_choices, default=No)
    pregnant = models.CharField(max_length=1, choices=yes_no_choices, default=No)
    created_at = models.DateTimeField(default=timezone.now)
    chief_complaint = models.TextField(max_length=500)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    status = models.CharField(max_length=2, choices=status_choices, default=waiting)
    department = models.CharField(max_length=2, choices=dept_choices, default=pt)
    provider_id = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    photo_permission = models.CharField(max_length=1, choices=yes_no_choices, default=No)
    card_ID = models.PositiveIntegerField(blank=False, null=False)


    class Meta(object):
        ordering = ('my_order', 'card_ID', 'age')

    def __str__(self):
        return str(self.id)

    def was_created_today(self):
        now = timezone.now()
        return now - datetime.timedelta(hours=16) <= self.record_date <= now

class encounter(models.Model):

    patient_id = models.ForeignKey(patient, on_delete=models.CASCADE)
    Back_Pain = models.BooleanField(default=False)

    Cane = models.BooleanField(default=False)
    Crutches = models.BooleanField(default=False)
    Walker = models.BooleanField(default=False)
    Wheel_Chair = models.BooleanField(default=False)

    Manual_Therapy = models.BooleanField(default=False)
    Education = models.BooleanField(default=False)
    Exercise = models.BooleanField(default=False)
    Improvement = models.IntegerField(choices=imp_choices)

    Systolic = models.CharField(max_length=4, blank=True, default='0')
    Diastolic = models.CharField(max_length=4, blank=True, default='0')
    Infection_UTI = models.BooleanField(default=False)
    Infection_Vaginal = models.BooleanField(default=False)
    Infection_Other = models.BooleanField(default=False)

    Gen_Med = models.BooleanField(default=False)
    Orthotics = models.BooleanField(default=False)
    Prosthetics = models.BooleanField(default=False)
    Refer_Out_Of_Stand = models.BooleanField(default=False)
    Neuro = models.BooleanField(default=False)
    Peds = models.BooleanField(default=False)
    Wound = models.BooleanField(default=False)
    Gen_PT = models.BooleanField(default=False)
    Pelvic_Health = models.BooleanField(default=False)

    Provider_Notes = models.TextField(max_length=500)
    Supplies_Used = models.TextField(max_length=500)

    Shoulder = models.BooleanField(default=False)
    Wrist = models.BooleanField(default=False)
    Knee = models.BooleanField(default=False)
    Elbow = models.BooleanField(default=False)
    Back = models.BooleanField(default=False)
    Ankle = models.BooleanField(default=False)
    AFO = models.BooleanField(default=False)
    Shoes = models.BooleanField(default=False)

    #servies
    Return = models.BooleanField(default=False)
    Discharged = models.BooleanField(default=False)
    Refer_Out = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    provider_id = models.ForeignKey(settings.AUTH_USER_MODEL)


    class Meta(object):
        ordering = ('my_order',)

    def __str__(self):
        return str(self.patient_id)


