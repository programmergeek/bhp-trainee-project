from django.contrib import admin

from ..admin_site import mock_study_admin
from ..forms.subject_blood_sample_form import SubjectBloodSampleForm
from ..models.subject_blood_sample import SubjectBloodSample


@admin.register(SubjectBloodSample, site=mock_study_admin)
class SubjectBloodSampleAdmin(admin.ModelAdmin):

    form = SubjectBloodSampleForm

    fieldsets = ((None, {
        'fields': [
            'subject_identifier',
            'sample_identifier',
            'sample_type',
            'collection_date',
            'collection_site',
            'volume',
            'anticoagulant',
            'tube_type',
            'storage_location',
            'status'
        ]
    }),)

    radio_fields = {
        'collection_site': admin.VERTICAL,
    }
