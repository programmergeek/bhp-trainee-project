from django.contrib import admin

from ..models.subject_visit import SubjectVisit
from ..admin_site import mock_study_admin
from ..forms.subject_visit_form import SubjectVisitForm


@admin.register(SubjectVisit, site=mock_study_admin)
class SubjectVisitAdmin(admin.ModelAdmin):

    form = SubjectVisitForm

    fieldsets = (
        (None, {
            'fields': [
                'appointment',
                'reason',
                'reason_unscheduled',
                'info_source',
            ]}),
    )

    radio_fields = {
        'reason': admin.VERTICAL,
        'reason_unscheduled': admin.VERTICAL,
        'info_source': admin.VERTICAL}
