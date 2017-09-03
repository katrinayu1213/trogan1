from django.db import models
import datetime
from django.utils import timezone

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


# Create your models here.
class patient(models.Model):

    patient_id = models.CharField(max_length=6)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=sex_choices, default=sex_unknown)
    age = models.IntegerField()
    phone = models.IntegerField()
    city = models.CharField(max_length=35, choices=city_choices, default=city_unknown)
    city_other = models.CharField(max_length=60, blank=True)
    heard_of_stand = models.CharField(max_length=1, choices=yes_no_choices, default=No)
    heard_of_stand_how = models.CharField(max_length=200, blank=True)
    refugee_ever = models.CharField(max_length=1, choices=yes_no_choices, default=No)
    refugee_reason = models.CharField(max_length=500,blank=True)
    previous_patient = models.CharField(max_length=1, choices=yes_no_choices, default=No)
    pregnant = models.CharField(max_length=1, choices=yes_no_choices, default=No)
    record_date = models.DateTimeField(default=timezone.now())
    chief_complaint = models.TextField(max_length=500)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    status = models.CharField(max_length=1, choices=status_choices, default=waiting)
    department = models.CharField(max_length=2, choices=dept_choices, default=pt)


    class Meta(object):
        ordering = ('my_order',)

    def __str__(self):
        return self.patient_id

    def was_created_today(self):
        now = timezone.now()
        return now - datetime.timedelta(hours=16) <= self.record_date <= now

