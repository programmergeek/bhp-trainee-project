from django.contrib import admin
from ..admin_site import mock_study_admin
from ..forms.subject_consent_form import SubjectConsentForm
from ..models.subject_consent import SubjectConsent
from edc_consent.modeladmin_mixins import ModelAdminConsentMixin
from edc_model_admin import (
    audit_fieldset_tuple
)


@admin.register(SubjectConsent, site=mock_study_admin)
class SubjectConsentAdmin(ModelAdminConsentMixin, admin.ModelAdmin):

    form = SubjectConsentForm

    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'first_name',
                'last_name',
                'initials',
                'language',
                'is_literate',
                'witness_name',
                'consent_datetime',
                'gender',
                'dob',
                'guardian_name',
                'is_dob_estimated',
                'identity',
                'confirm_identity',
                'identity_type',
                'other_idenity_type',
                'is_incarcerated')}),
        ('Review Questions', {
            'fields': (
                'consent_reviewed',
                'study_questions',
                'assessment_score',
                'consent_signature',
                'consent_copy'),
            'description': 'The following questions are directed to the interviewer.'}),
        audit_fieldset_tuple)

    search_fields = ('subject_identifier', 'identity')

    radio_fields = {
        "assessment_score": admin.VERTICAL,
        "consent_copy": admin.VERTICAL,
        "consent_reviewed": admin.VERTICAL,
        "consent_signature": admin.VERTICAL,
        "gender": admin.VERTICAL,
        "is_dob_estimated": admin.VERTICAL,
        "is_incarcerated": admin.VERTICAL,
        "is_literate": admin.VERTICAL,
        "language": admin.VERTICAL,
        "may_store_samples": admin.VERTICAL,
        "study_questions": admin.VERTICAL,
    }

    search_fields = ('subject_identifier', 'identity')
