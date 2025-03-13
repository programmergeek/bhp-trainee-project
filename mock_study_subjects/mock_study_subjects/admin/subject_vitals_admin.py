from django.contrib import admin
from ..forms.subject_vitals_form import SubjectVitalsForm
from ..models.subject_vitals import SubjectVitals
from ..admin_site import mock_study_admin


@admin.register(SubjectVitals, site=mock_study_admin)
class SubjectVitalsAdmin(admin.ModelAdmin):

    form = SubjectVitalsForm

    fieldsets = ((None, {
        'fields': [
            'subject_identifier',
            'collection_site',
            'were_vitals_collected',
            'measurement_date',
            'systolic_blood_pressure',
            'diastolic_blood_pressure',
            'anatomical_location_of_measurement',
            'height',
            'weight',
            'is_baseline'
        ]
    }),)

    radio_fields = {
        'collection_site': admin.VERTICAL,
    }
