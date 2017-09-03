from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import patient


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
                    'chief_complaint', 'record_date', 'status', 'department',)
    actions = [being_seen, waiting, discharged, physical_therapy, gen_med,]

admin.site.register(patient, AllPatientAdmin)


#Today's patients
class TodayPatientAdmin(SortableAdminMixin, admin.ModelAdmin):
    def get_queryset(self):
        return super(TodayPatientAdmin, self).get_queryset().filter(patient.was_created_today()== True)
    actions = [being_seen, waiting, discharged,]


admin.site.register(patient, TodayPatientAdmin)






