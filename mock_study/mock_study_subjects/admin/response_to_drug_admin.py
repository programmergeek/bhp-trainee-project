from django.contrib import admin

from ..admin_site import mock_study_admin
from ..models.response_to_drug import DrugResponse
from ..forms.response_to_drug_form import DrugResponseForm

@admin.register(DrugResponse, site=mock_study_admin)
class DrugResponseAdmin(admin.ModelAdmin):

    form = DrugResponseForm

    fieldsets = ((None, {
        'fields': [
            'drug_response',
            'response_datetime',
            'report_datetime',
        ]
    }),)
