from .constants import YES, NO


class HypertensionStatusEvaluator:

    def __init__(self,
                 hypertension_status=None,
                 is_preganent=None,
                 is_breastfeeding=None,
                 has_allergies_to_drug=None,
                 age=None,
                 has_history_of_severe_cardiovascular_events=None
                 ):
        self.eligible = None
        if (hypertension_status == YES and
            is_preganent == NO and
            is_breastfeeding == NO and
            has_allergies_to_drug == NO and
            (age >= 30 and age <= 65) and
                has_history_of_severe_cardiovascular_events == NO):
            self.eligible = True

        else:
            self.eligible = False


class Eligibility:

    def __init__(self,
                 hypertension_status,
                 is_pregnant,
                 is_breastfeeding,
                 has_allergies_to_drug,
                 age,
                 has_history_of_severe_cardiovascular_events
                 ):

        self.hypertension_status_evaluator = HypertensionStatusEvaluator(
            hypertension_status=hypertension_status,
            age=age,
            is_preganent=is_pregnant,
            is_breastfeeding=is_breastfeeding,
            has_allergies_to_drug=has_allergies_to_drug,
            has_history_of_severe_cardiovascular_events=has_history_of_severe_cardiovascular_events
        )
        self.criteria = dict(
            hypertension_status=self.hypertension_status_evaluator.eligible
        )
        self.eligible = all(self.criteria.values())
        pass
