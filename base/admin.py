from django.contrib import admin
from .models.vitals_model import ParticipantVital
from .models.adverse_event_model import AdverseEvent
from .models.blood_samples_models import BloodSample
from .models.compliance_form_model import ComplianceForm
# Register your models here.

admin.site.register(ParticipantVital)
admin.site.register(AdverseEvent)
admin.site.register(BloodSample)
admin.site.register(ComplianceForm)
