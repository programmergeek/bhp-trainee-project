from django.contrib import admin
from .models.vitals_model import ParticipantVital
from .models.adverse_event_model import AdverseEvent
from .models.blood_samples_models import BloodSample
from .models.compliance_form_model import ComplianceForm
from .models.exit_interview_model import ExitInterview
from .models.final_questionnaire_model import FinalQuestionnaire
from .models.participant_medical_history_model import ParticipantMedicalHistory, Allergy, Doctor, Medication, PreviousMedicalEvents
# Register your models here.

admin.site.register(ParticipantVital)
admin.site.register(AdverseEvent)
admin.site.register(BloodSample)
admin.site.register(ComplianceForm)
admin.site.register(ExitInterview)
admin.site.register(FinalQuestionnaire)
admin.site.register(ParticipantMedicalHistory)
admin.site.register(Allergy)
admin.site.register(Doctor)
admin.site.register(Medication)
admin.site.register(PreviousMedicalEvents)
