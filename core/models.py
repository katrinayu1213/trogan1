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

# patient status
waiting = 'W'
being_seen = 'B'
discharged = 'D'
status_choices = ((waiting, 'Waiting'), (being_seen, 'Being Seen'), (discharged, 'Discharged'))

# department
pt = 'PT'
gen_med = 'GM'
dept_choices = ((pt, 'Physical Therapy'), (gen_med, 'Gen Med'))

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
    age = models.IntegerField()
    phone = models.BigIntegerField()
    city = models.CharField(max_length=35, choices=city_choices, default=city_unknown)
    city_other = models.CharField(max_length=60, blank=True)
    heard_of_stand = models.CharField(max_length=1, choices=yes_no_choices, default=No)
    heard_of_stand_how = models.CharField(max_length=200, blank=True)
    refugee_ever = models.CharField(max_length=1, choices=yes_no_choices, default=No)
    refugee_reason = models.CharField(max_length=500,blank=True)
    previous_patient = models.CharField(max_length=1, choices=yes_no_choices, default=No)
    pregnant = models.CharField(max_length=1, choices=yes_no_choices, default=No)
    created_at = models.DateTimeField(default=timezone.now)
    chief_complaint = models.TextField(max_length=500)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    status = models.CharField(max_length=1, choices=status_choices, default=waiting)
    department = models.CharField(max_length=2, choices=dept_choices, default=pt)
    provider_id = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)


    class Meta(object):
        ordering = ('my_order',)

    def __str__(self):
        return str(self.id)

    def was_created_today(self):
        now = timezone.now()
        return now - datetime.timedelta(hours=16) <= self.record_date <= now

class encounter(models.Model):

    patient_id = models.ForeignKey(patient, on_delete=models.CASCADE)
    back_pain = models.BooleanField(default=False)
    fever = models.BooleanField(default=False)
    wheelchair = models.BooleanField(default=False)
    manipulation = models.BooleanField(default=False)
    needling = models.BooleanField(default=False)
    cupping = models.BooleanField(default=False)
    improvement = models.IntegerField(choices=imp_choices)
    ref_gen_med = models.BooleanField(default=False)
    ref_ortho = models.BooleanField(default=False)
    ref_prosth = models.BooleanField(default=False)
    ref_out = models.BooleanField(default=False)
    provider_notes = models.TextField(max_length=500)
    supplies_used = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    provider_id = models.ForeignKey(settings.AUTH_USER_MODEL)


    class Meta(object):
        ordering = ('my_order',)

    def __str__(self):
        return str(self.patient_id)


