from django.contrib import admin
# from django_revision.modeladmin_mixin import ModelAdminRevisionMixin

from ..admin_site import mock_study_admin
from ..forms.subject_screening_form import SubjectScreeningForm
from ..models.subject_screening import SubjectScreening
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin,
    ModelAdminRedirectOnDeleteMixin,
    ModelAdminFormInstructionsMixin
)


class SubjectScreeningAdminMixin(
        ModelAdminNextUrlRedirectMixin,
        ModelAdminRedirectOnDeleteMixin,
):
    pass


@admin.register(SubjectScreening, site=mock_study_admin)
class SubjectScreeningAdmin(ModelAdminFormInstructionsMixin, admin.ModelAdmin):

    form = SubjectScreeningForm

    fieldsets = (
        (None, {
            'fields': [
                'age',
                'gender',
                'has_hypertension',
                'is_pregnant',
                'is_breastfeeding',
                'has_allergies_to_drug',
                'has_history_of_severe_cardiovascular_events',
                'report_datetime',
                'enrollment_site'
            ]
        }),
    )

    search_fields = ('subject_identifier', )

    radio_fields = {
        'has_hypertension': admin.VERTICAL,
        'is_pregnant': admin.VERTICAL,
        'is_breastfeeding': admin.VERTICAL,
        'enrollment_site': admin.VERTICAL,
        'gender': admin.VERTICAL,
        'has_allergies_to_drug': admin.VERTICAL,
        'has_history_of_severe_cardiovascular_events': admin.VERTICAL
    }
