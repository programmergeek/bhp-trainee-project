from edc_base.model_mixins import BaseModel
from edc_visit_schedule.model_mixins import OnScheduleModelMixin
from django.core.exceptions import ValidationError

from .subject_consent import SubjectConsent


class OnSchedule(OnScheduleModelMixin, BaseModel):

    def get_consent_version(self):
        try:
            subject_consent = SubjectConsent.objects.get(
                subject_identifier=self.subject_identifier)
        except SubjectConsent.DoesNotExist:
            raise ValidationError(
                'Missing Consent form. Cannot proceed.'
            )
        else:
            return subject_consent.version

    def save(self, *args, **kwargs):
        self.consent_version = ''
        pass
