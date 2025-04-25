from django.contrib import admin
from ..admin_site import mock_study_prn_admin
from ..forms.death_report_form import DeathReportForm
from ..models.death_reports import DeathReport


@admin.register(DeathReport, site=mock_study_prn_admin)
class DeathReportAdmin(admin.ModelAdmin):

    form = DeathReportForm

    fieldsets = ((None, {
        'fields': (
            'subject_identifier',
            'date_of_death',
            'cause_of_death',
            'is_death_date_estimated',
            'source_of_info',
            'was_hospitalised',
            'hospital_hospitalised',
            'reason_hospitalised',
            'days_hospitalised',
        )
    }),)
