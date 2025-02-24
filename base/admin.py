from django.contrib import admin
from .models.vitals_model import ParticipantVital
from .models.adverse_event_model import AdverseEvent
# Register your models here.

admin.site.register(ParticipantVital)
admin.site.register(AdverseEvent)
