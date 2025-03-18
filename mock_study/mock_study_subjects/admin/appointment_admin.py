from django.contrib import admin

from ..admin_site import mock_study_admin
from ..forms.appointment_form import AppointmentForm
from ..models.appointment import Appointment
from edc_model_admin import audit_fieldset_tuple


@admin.register(Appointment, site=mock_study_admin)
class AppointmentAdmin(admin.ModelAdmin):

    form = AppointmentForm

    fieldsets = ((None, {
        'fields': [
            'subject_identifier',
            'appt_datetime',
            'appt_type',
            'appt_status',
            'appt_reason',
            'comment',
        ]
    }),
        audit_fieldset_tuple
    )
    radio_fields = {
        'site': admin.VERTICAL,
    }
