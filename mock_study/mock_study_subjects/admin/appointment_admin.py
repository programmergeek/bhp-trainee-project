from django.contrib import admin

from ..admin_site import mock_study_admin
from ..forms.appointment_form import AppointmentForm
from ..models.appointment import Appointment


@admin.register(Appointment, site=mock_study_admin)
class AppointmentAdmin(admin.ModelAdmin):

    form = AppointmentForm

    fieldsets = ((None, {
        'fields': [
            'subject_identifier',
            'datetime',
            'site'
        ]
    }),)

    radio_fields = {
        'site': admin.VERTICAL,
    }
