from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist


class SubjectLocatorModelWrapperMixin:

    def subject_locator_model_obj(self):
        try:
            return self.subject_locator_cls.objects.get(**self.subject_locator_options)
        except ObjectDoesNotExist:
            return None
        pass

    def subject_locator(self):
        model_obj = self.subject_locator_model_obj or self.subject_locator_cls(
            **self.subject_locator_options)
        return self.subject_locator_wrapper(model_obj=model_obj)

    def subject_locator_cls(self):
        return apps.get_model('mock_study_subjects.subjectlocator')

    def subject_locator_options(self):
        options = dict(
            subject_identifier=self.subject_identifier
        )
        return options
