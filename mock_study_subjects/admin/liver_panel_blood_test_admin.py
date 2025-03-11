from django.contrib import admin

from ..admin_site import mock_study_admin
from ..models.liver_panel_blood_test_result import LiverPanelBloodTestResult
from ..forms.liver_panel_blood_test_form import LiverPanelTestForm


@admin.register(LiverPanelBloodTestResult, site=mock_study_admin)
class LiverPanelBloodTestAdmin(admin.ModelAdmin):

    form = LiverPanelTestForm

    fieldsets = ((None, {
        'fields': [
            'sample_identifier',
            'test_date',
            'status',
            'alt',
            'alp',
            'ast',
            'bilirubin_total',
            'bilirubin_direct',
            'bilirubin_indirect',
            'albumin',
            'total_protien'
        ]
    }),)
