from django.contrib import admin
from ..admin_site import mock_study_admin
from ..forms.subject_locator_form import SubjectLocatorForm
from ..models.subject_locator import SubjectLocator


@admin.register(SubjectLocator, site=mock_study_admin)
class SubjectLocatorAdmin(admin.ModelAdmin):

    form = SubjectLocatorForm

    fieldsets = (
        (None, {
            'fields': (
                'date_signed',
                'local_clinic',
                'home_village',
            )}),
    )

    search_fields = ('subject_identifier', )
