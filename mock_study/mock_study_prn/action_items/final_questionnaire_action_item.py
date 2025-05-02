from edc_action_item import Action, site_action_items

FINAL_QUESTIONNAIRE_ACTION_ITEM_NAME = 'final_questionnaire'


class FinalQuestionnaireAction(Action):

    name = FINAL_QUESTIONNAIRE_ACTION_ITEM_NAME
    display_name = 'Finale Questionnaire'
    reference_model = 'mock_study_prn.finalquestionnaire'
    singleton = True
