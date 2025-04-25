from django.contrib import admin
from ..admin_site import mock_study_prn_admin
from ..forms.compliance_form import ComplianceForm
from ..models.compliance import ComplianceReport


@admin.register(ComplianceReport, site=mock_study_prn_admin)
class ComplianceAdmin(admin.ModelAdmin):

    form = ComplianceForm

    fieldsets = ((None, {
        'fields': (
            'subject_identifier',
            'doses_prescribed',
            'doses_taken',
            'missed_visits',
            'report_datetime',
            'comment',
        )
    }),)
