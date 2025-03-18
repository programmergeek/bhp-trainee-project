# provides the base validation logic
from edc_form_validators import FormValidator


class SubjectConsentValidator(FormValidator):

    def clean(self):
        super().clean()  # handles the process of cleaning the data entered from the form and stopping validation when an error is raised
