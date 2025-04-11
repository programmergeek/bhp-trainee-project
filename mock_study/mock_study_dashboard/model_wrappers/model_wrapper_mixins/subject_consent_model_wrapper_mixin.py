from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist


class SubjectConsentModelWrapperMixin:

    def subject_consent_model_obj(self):
        """
        Find a subject consent assesment using the options passed into the 
        parameters. If none is found then return None.
        """
        try:
            return self.subject_consent_cls.objects.get(**self.subject_consent_options)
        except ObjectDoesNotExist:
            return None
        pass

    def subject_consent(self):
        """
        Returns a wrapped consent model instance for either a saved on unsaved consent assessment.
        """
        model_obj = self.subject_consent_model_obj or self.subject_consent_cls(
            **self.subject_consent_options)
        return self.subject_consent_wrapper(model_obj=model_obj)

    def subject_consent_cls(self):
        """Returns the consent model"""
        return apps.get_model('mock_study_subjects.subjectconsent')

    def subject_consent_options(self):
        """Returns a dictionary which defines the options that will passed to the consent model"""
        options = dict(
            subject_identifier=self.subject_identifier
        )
        return options
