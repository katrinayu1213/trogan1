from django.contrib import admin
from .models import patient


# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'first_name', 'last_name', 'sex', 'age', 'phone', 'city', 'pregnant',
                    'chief_complaint', 'record_date')

admin.site.register(patient, PatientAdmin)
