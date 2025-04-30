from edc_form_validators import FormValidator
from edc_constants.constants import NO


class FinalQuestionnaireValidator(FormValidator):

    def clean(self):
        self.required_if(
            NO,
            field='study_purpose',
            field_required='study_purpose_grievance'
        )
        self.required_if(
            NO,
            field='respectful_staff',
            field_required='respectful_staff_comment'
        )
        self.required_if(
            'disagree',
            field='instruction_clearity',
            field_required='instruction_clearity_grievance'
        )
        self.required_if(
            'strongly_disagree',
            field='instruction_clearity',
            field_required='instruction_clearity_grievance'
        )
