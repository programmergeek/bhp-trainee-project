from django.contrib import admin
# from django_revision.modeladmin_mixin import ModelAdminRevisionMixin

from ..admin_site import mock_study_admin
from ..forms.mock_study_subject_screening_form import SubjectScreeningForm
from ..models.subject_screening import SubjectScreening


class ModelAdminMixin():

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'


@admin.register(SubjectScreening, site=mock_study_admin)
class SubjectScreeningAdmin(admin.ModelAdmin):

    form = SubjectScreeningForm

    fieldsets = (
        (None, {
            'fields': {
                'report_datetine',
                'subject_identifier',
                'has_hypertension',
                'is_pregnant',
                'is_breastfeeding',
                'enrollment_site'
            }
        }),

    )

    search_fields = ('subject_identifier', )

    radio_fields = {
        'has_hypertension': admin.VERTICAL,
        'is_pregnant': admin.VERTICAL,
        'is_breastfeeding': admin.VERTICAL,
        'enrollment_site': admin.VERTICAL,
    }

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj))
