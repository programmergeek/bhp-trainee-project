from django.contrib import admin

from ..admin_site import mock_study_admin
from ..forms.symptoms_form import SymptomsForm
from ..models.symptoms import Symptoms

@admin.register(Symptoms, site=mock_study_admin)
class SymptomsAdmin(admin.ModelAdmin):

    form = SymptomsForm

    fieldsets = ((None, {
        'fields': [
            'headache',
            'chest_pain',
            'dizziness',
            'breathing',
            'nausea',
            'vomiting',
            'blurry_vision',
            'anxiety',
            'abnomal_heart_rhythm',
            'other_symtoms',
            'report_datetime',
        ]
    }),)
