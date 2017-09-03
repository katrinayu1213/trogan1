from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import patient
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

#All Patients in System
class AllPatientAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('patient_id', 'first_name', 'last_name', 'sex', 'age', 'phone', 'city', 'pregnant',
                    'chief_complaint', 'status', 'department',)
    actions = [being_seen, waiting, discharged, physical_therapy, gen_med,]


# Today's patients proxy model
class TodayPatient(patient):
    class Meta:
        proxy = True

#Today's patients
class TodayPatientAdmin(AllPatientAdmin):
    def get_queryset(self,request):
        now = timezone.now()
        return patient.objects.filter(record_date__day=now.day)


# Today's PT Patients Proxy model
class PTPatient(patient):
    class Meta:
        proxy = True

# Today's PT Patients
class PTPatientAdmin(AllPatientAdmin):
    def get_queryset(self, request):
        now = timezone.now()
        return patient.objects.filter(record_date__day=now.day).filter(department='PT')


# Today's Gen Med Patients Proxy model
class GMPatient(patient):
    class Meta:
        proxy = True

#Today's Gen Med Patients
class GMPatientAdmin(AllPatientAdmin):
    def get_queryset(self, request):
        now = timezone.now()
        return patient.objects.filter(record_date__day=now.day).filter(department='GM')

admin.site.register(patient, AllPatientAdmin)
admin.site.register(TodayPatient, TodayPatientAdmin)
admin.site.register(PTPatient, PTPatientAdmin)
admin.site.register(GMPatient, GMPatientAdmin)
