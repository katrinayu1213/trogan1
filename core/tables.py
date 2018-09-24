import django_tables2 as tables
from django_tables2.utils import A
from .models import patient


class PatientTable(tables.Table):

    class Meta:
        model = patient
        fields = ('id', 'last_name',
                  'first_name', 'sex', 'age',
                  'pregnant', 'chief_complaint', 'provider_id')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no patients matching the search criteria..."