from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import patient, encounter
from django.utils import timezone
import datetime


# Register your models here.

def being_seen(modeladmin, request, queryset):
    queryset.update(status='B')


def waiting(modeladmin, request, queryset):
    queryset.update(status='W')


def discharged(modeladmin, request, queryset):
    queryset.update(status='D')

def physical_therapy(modeladmin, request, queryset):
    queryset.update(department='PT')

def gen_med(modeladmin, request, queryset):
    queryset.update(department='GM')


# All Patients in System
class AllPatientAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'sex', 'age', 'phone', 'city', 'pregnant',
                    'chief_complaint', 'status', 'department', 'created_at', 'provider_id')
    actions = [being_seen, waiting, discharged, physical_therapy, gen_med,]


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


# Encounters
class EncounterAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('patient_id', 'back_pain', 'fever', 'wheelchair', 'manipulation', 'needling', 'cupping', 'improvement',
                    'ref_gen_med', 'ref_ortho', 'ref_prosth', 'ref_out', 'supplies_used', 'provider_id')


admin.site.register(patient, AllPatientAdmin)
admin.site.register(TodayPatient, TodayPatientAdmin)
admin.site.register(PTPatient, PTPatientAdmin)
admin.site.register(GMPatient, GMPatientAdmin)
admin.site.register(encounter, EncounterAdmin)
