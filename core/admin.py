from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import patient, encounter, pain_catastrophizing_scale
from django.utils import timezone
import datetime


# Register your models here.

def being_seen(modeladmin, request, queryset):
    queryset.update(status='B')


def waiting(modeladmin, request, queryset):
    queryset.update(status='W')


def discharged(modeladmin, request, queryset):
    queryset.update(status='D')

def no_show(modeladmin, request, queryset):
    queryset.update(status='NS')

def returning(modeladmin, request, queryset):
    queryset.update(status='R')

def physical_therapy(modeladmin, request, queryset):
    queryset.update(department='PT')

def gen_med(modeladmin, request, queryset):
    queryset.update(department='GM')

def wound(modeladmin, request, queryset):
    queryset.update(department='W')

def prosth(modeladmin, request, queryset):
    queryset.update(department='P1')

def peds(modeladmin, request, queryset):
    queryset.update(department='P2')

def pelvic(modeladmin, request, queryset):
    queryset.update(department='P3')

def make_urgent(modeladmin, request, queryset):
    queryset.update(order_ID=1)

def make_non_urgent(modeladmin, request, queryset):
    queryset.update(order_ID=0)




# All Patients in System
class AllPatientAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id','card_ID','first_name', 'last_name', 'sex', 'age', 'phone', 'city', 'pregnant',
                    'chief_complaint', 'status', 'department', 'created_at', 'provider_id', 'order_ID')
    actions = [being_seen, waiting, discharged, no_show, returning, physical_therapy, gen_med, wound, prosth, peds,
               pelvic, make_urgent, make_non_urgent]


# Today's patients proxy model
class TodayPatient(patient):
    class Meta:
        proxy = True

# Today's patients
class TodayPatientAdmin(AllPatientAdmin):
    def get_queryset(self,request):
        now = timezone.now()
        return patient.objects.filter(created_at__day=now.day)


# Today's PT Patients Proxy model
class PTPatient(patient):
    class Meta:
        proxy = True

# Today's PT Patients
class PTPatientAdmin(AllPatientAdmin):
    def get_queryset(self, request):
        now = timezone.now()
        return patient.objects.filter(created_at__day=now.day).filter(department='PT')


# Today's Gen Med Patients Proxy model
class GMPatient(patient):
    class Meta:
        proxy = True

# Today's Gen Med Patients
class GMPatientAdmin(AllPatientAdmin):
    def get_queryset(self, request):
        now = timezone.now()
        return patient.objects.filter(created_at__day=now.day).filter(department='GM')

# Today's Peds patients proxy model
class PedsPatient(patient):
    class Meta:
        proxy = True

# Today's Peds patients
class PedsPatientAdmin(AllPatientAdmin):
    def get_queryset(self, request):
        now = timezone.now()
        return patient.objects.filter(created_at__day=now.day).filter(department='P2')

# Today's Prosthetics patients proxy model
class ProsthPatient(patient):
    class Meta:
        proxy = True

# Today's Prosthetics patients
class ProsthPatientAdmin(AllPatientAdmin):
    def get_queryset(self, request):
        now = timezone.now()
        return patient.objects.filter(created_at__day=now.day).filter(department='P1')

# Today's Prosthetics patients proxy model
class WoundPatient(patient):
    class Meta:
        proxy = True

# Today's Prosthetics patients
class WoundPatientAdmin(AllPatientAdmin):
    def get_queryset(self, request):
        now = timezone.now()
        return patient.objects.filter(created_at__day=now.day).filter(department='W')

# Today's Pelvic patients proxy model
class PelvicPatient(patient):
    class Meta:
        proxy = True

# Today's Pelvic patients
class PelvicPatientAdmin(AllPatientAdmin):
    def get_queryset(self, request):
        now = timezone.now()
        return patient.objects.filter(created_at__day=now.day).filter(department='P3')

# Today's Discharged patients proxy model
class DischargedPatient(patient):
    class Meta:
        proxy = True

# Today's Discharged patients
class DischargedPatientAdmin(AllPatientAdmin):
    def get_queryset(self, request):
        now = timezone.now()
        return patient.objects.filter(created_at__day=now.day).filter(status='D')

# Today's Waiting patients proxy model
class WaitingPatient(patient):
    class Meta:
        proxy = True

# Today's Waiting patients
class WaitingPatientAdmin(AllPatientAdmin):
    def get_queryset(self, request):
        now = timezone.now()
        return patient.objects.filter(created_at__day=now.day).filter(status='W')

# Encounters
class EncounterAdmin(SortableAdminMixin, admin.ModelAdmin):

    list_display = ('id', 'provider_id', 'patient_id', 'Supplies_Used', 'Provider_Notes'
                    , 'medication_list', )

# PCS Scores
class PCSAdmin(SortableAdminMixin, admin.ModelAdmin):

    list_display = ('id','provider_id','patient_id', 'q1_pcs', 'q2_pcs', 'q3_pcs','q4_pcs', 'q5_pcs', 'q6_pcs', 'q7_pcs', 'q8_pcs',  'q9_pcs', 'q10_pcs',
         'q11_pcs', 'q12_pcs', 'q13_pcs',)


admin.site.register(patient, AllPatientAdmin)
admin.site.register(TodayPatient, TodayPatientAdmin)
admin.site.register(PTPatient, PTPatientAdmin)
admin.site.register(GMPatient, GMPatientAdmin)
admin.site.register(encounter, EncounterAdmin)
admin.site.register(PedsPatient, PedsPatientAdmin)
admin.site.register(ProsthPatient, ProsthPatientAdmin)
admin.site.register(WoundPatient, WoundPatientAdmin)
admin.site.register(PelvicPatient, PelvicPatientAdmin)
admin.site.register(DischargedPatient, DischargedPatientAdmin)
admin.site.register(WaitingPatient, WaitingPatientAdmin)
admin.site.register(pain_catastrophizing_scale, PCSAdmin)

