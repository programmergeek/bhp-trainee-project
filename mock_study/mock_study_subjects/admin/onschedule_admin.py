from django.contrib import admin
from ..admin_site import mock_study_admin
from ..models.onschedule import OnSchedule


@admin.register(OnSchedule, site=mock_study_admin)
class OnScheduleAdmin(admin.ModelAdmin):

    pass
