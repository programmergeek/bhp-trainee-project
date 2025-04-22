from edc_action_item import Action, site_action_items, HIGH_PRIORITY

FINAL_QUESTIONNAIRE_ACTION_ITEM_NAME = 'final_questionnaire'


class FinalQuestionnaireAction(Action):

    name = FINAL_QUESTIONNAIRE_ACTION_ITEM_NAME
    display_name = 'Finale Questionnaire'
    reference_model = 'mock_study_prn.finalquestionnaire'
    priority = HIGH_PRIORITY
    singleton = True


site_action_items.register(FinalQuestionnaireAction)
