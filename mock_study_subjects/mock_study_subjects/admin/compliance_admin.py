from django.contrib import admin

from ..admin_site import mock_study_admin
from ..forms.compliance_form import ComplianceForm
from ..models.compliance import Compliance


@admin.register(Compliance, site=mock_study_admin)
class ComplianceAdmin(admin.ModelAdmin):

    form = ComplianceForm

    fieldsets = ((None, {
        'fields': [
            'subject_identifier',
            'doses_taken',
            'prescribed_dosage',
            'subject_feedback',
            'investigator_comments'
        ]
    }),)
