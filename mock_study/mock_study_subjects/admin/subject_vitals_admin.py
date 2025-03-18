from django.contrib import admin
from ..forms.subject_vitals_form import SubjectVitalsForm
from ..models.subject_vitals import SubjectVitals
from ..admin_site import mock_study_admin


@admin.register(SubjectVitals, site=mock_study_admin)
class SubjectVitalsAdmin(admin.ModelAdmin):

    form = SubjectVitalsForm

    fieldsets = ((None, {
        'fields': [
            'subject_visit',
            'report_datetime',
            'systolic_blood_pressure',
            'diastolic_blood_pressure',
            'heart_rate',
            'height',
            'weight',
        ]
    }),)
