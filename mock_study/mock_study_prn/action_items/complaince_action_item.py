from edc_action_item import Action

COMPLIANCE_ACTION_ITEM_NAME = 'compliance'


class ComplianceAction(Action):

    name = COMPLIANCE_ACTION_ITEM_NAME
    reference_model = 'mock_study_prn.complaincereport'
    singleton = True
    display_name = 'Compliance Report'
