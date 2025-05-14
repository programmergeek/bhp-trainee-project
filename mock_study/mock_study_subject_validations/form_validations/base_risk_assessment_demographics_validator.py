from edc_form_validators import FormValidator

class BaseRiskAssessmentDemographicsValidator(FormValidator):
    
    def clean(self):
        self.validate_other_specify(
            field='marital_status',
            other_specify_field='marital_status_other'
        )
        self.validate_other_specify(
            field='race',
            other_specify_field='race_other'
        )
        self.validate_other_specify(
            field='education',
            other_specify_field='education_other'
        )

    pass
