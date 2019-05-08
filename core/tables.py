import django_tables2 as tables
from django_tables2.utils import A
from .models import patient, encounter


class PatientTable(tables.Table):

    class Meta:
        model = patient
        fields = ('id', 'last_name',
                  'first_name', 'age',
                  'chief_complaint', 'provider_id','department', 'card_ID')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no patients matching the search criteria"


class EncounterTable(tables.Table):

    class Meta:
        model = encounter
        fields = ('provider_id', 'patient_id', 'Provider_Notes', 'Supplies_Used', 'medication_list')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no encounters matching the search criteria"