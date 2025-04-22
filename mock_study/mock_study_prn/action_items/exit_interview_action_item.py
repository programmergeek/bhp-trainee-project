from edc_action_item import Action, site_action_items, HIGH_PRIORITY

EXIT_INTERVIEW_ACTION_ITEM_NAME = 'exit_interview'


class ExitInterviewAction(Action):

    name = EXIT_INTERVIEW_ACTION_ITEM_NAME
    display_name = "Exit Interview"
    priority = HIGH_PRIORITY
    reference_model = 'mock_study_prn.exitinterview'
    singleton = True


site_action_items.register(ExitInterviewAction)
