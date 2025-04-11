from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist


class SubjectScreeningModelWrapperMixin:

    def subject_screening_model_obj(self):
        try:
            return self.subject_screening_model.objects.get(**self.subject_screening_options)
        except ObjectDoesNotExist:
            return None

    def subject_screening_cls(self):
        return apps.get_model('mock_study_subjects.subjectscreening')

    def subject_screening_options(self):

        options = dict(
            screening_identifier=self.screening_identifier
        )

        return options
