from edc_form_validators import FormValidator
from edc_constants.constants import YES, NO

class BaseRiskAssessmentCaffeineValidator(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='consumes_caffeine',
            field_required='drinks_per_week'
        )
        self.required_if(
            YES,
            field='consumes_caffeine',
            field_required='amount_of_drinks'
        )
        self.not_required_if(
            NO,
            field='consumes_caffeine',
            field_required='amount_of_drinks',
            not_required_msg=''
        )
