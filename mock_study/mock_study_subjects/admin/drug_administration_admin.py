from django.contrib import admin

from ..admin_site import mock_study_admin
from ..forms.drug_administration_form import DrugAdministrationForm
from ..models.drug_administration import DrugAdministration


@admin.register(DrugAdministration, site=mock_study_admin)
class DrugAdministrationAdmin(admin.ModelAdmin):

    form = DrugAdministrationForm

    fieldsets = ((None, {
        'fields': [
            'subject_identifier',
            'drug_taken',
            'comment'
        ]
    }),)
