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
        fields = ('id', 'card_id', 'provider_id', "first_name", 'last_name',
                  'sex', 'age', 'chief_complaint', 'Provider_Notes')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no patients mathing the search criteria"
