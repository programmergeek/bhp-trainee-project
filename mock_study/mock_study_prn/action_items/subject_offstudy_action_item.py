from edc_action_item import Action, site_action_items, HIGH_PRIORITY

SUBJECT_OFF_STUDY_ACTION_ITEM_NAME = 'subject_off_study'


class SubjectOffStudyAction(Action):

    name = SUBJECT_OFF_STUDY_ACTION_ITEM_NAME
    display_name = 'Subject Off Study'
    reference_model = 'mock_study_prn.subjectoffstudy'
    singleton = True
    priority = HIGH_PRIORITY


site_action_items.register(SubjectOffStudyAction)
