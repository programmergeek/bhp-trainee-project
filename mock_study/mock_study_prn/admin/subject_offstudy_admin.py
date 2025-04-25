from django.contrib import admin
from ..admin_site import mock_study_prn_admin
from ..forms.subject_offstudy_form import SubjectOffStudyForm
from ..models.subject_offstudy import SubjectOffStudy


@admin.register(SubjectOffStudy, site=mock_study_prn_admin)
class SubjectOffStudyAdmin(admin.ModelAdmin):

    form = SubjectOffStudyForm

    fieldsets = ((None, {
        'fields': (
            'subject_identifier',
            'report_datetime',
            'off_study_date',
            'reason',
        )
    }),)
