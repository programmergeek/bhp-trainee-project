from django.contrib import admin
from ..admin_site import mock_study_admin
from ..forms.subject_consent_form import SubjectConsentForm
from ..models.subject_consent import SubjectConsent


@admin.register(SubjectConsent, site=mock_study_admin)
class SubjectConsentAdmin(admin.ModelAdmin):

    form = SubjectConsentForm

    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'gender',)}),
        ('Review Questions', {
            'fields': (),
            'description': 'The following questions are directed to the interviewer.'}),
    )

    search_fields = ('subject_identifier', 'identity')

    readonly_fields = ('screening_identifier',)
