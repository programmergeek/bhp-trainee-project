from edc_metadata import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import P, CrfRule, CrfRuleGroup, predicate, register
from edc_constants.constants import YES

APP_LABEL='mock_study_subjects'

@register()
class BaseRiskAssessmentRuleGroup(CrfRuleGroup):
    drinks_alcohol = CrfRule(
        predicate=P('dinks_alcohol', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{APP_LABEL}.baseriskassessmentalcohol']
    )

    drinks_caffeine = CrfRule(
        predicate=P('drinks_caffeine', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{APP_LABEL}.baseriskassessmentcaffeine']
    )

    preexisting_conditions = CrfRule(
        predicate=P('preexisting_condition', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{APP_LABEL}.baseriskassessmenthealth']
    )

    class Meta:
        app_label = 'mock_study_subjects'
        source_model = f'{APP_LABEL}.baseriskassessment'
