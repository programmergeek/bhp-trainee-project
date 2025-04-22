from django.apps import apps
from edc_action_item import Action, site_action_items, HIGH_PRIORITY
from django.core.exceptions import ObjectDoesNotExist
from .death_report_action_item import DeathReportAction

ADVERSE_EVENT_ACTION_NAME = 'adverse_event'


class AdverseEventAction(Action):
    name = ADVERSE_EVENT_ACTION_NAME
    display_name = "Adverse Event"
    reference_model = "mock_study_prn.adverseevent"
    priority = HIGH_PRIORITY
    singleton = True

    # After this action triggered, if the
    # severity of the action item is death
    # then the death report action item should be triggered
    def get_next_actions(self):
        next_actions = []
        adverse_event_cls = apps.get_model('mock_study_prn.adverseevent')

        # get the subject identifier
        subject_identifier = self.reference_model_cls().subject_identifer
        # get the severity
        severity = self.reference_model_cls().severity

        try:
            adverse_event_cls.model.get(subject_identifier=subject_identifier)
            # if the severity is death then the next actions should be
            # completing a death report
            # TODO: add death report to next_action
            if (severity == 'death'):
                next_actions = [DeathReportAction]
                pass
        except ObjectDoesNotExist:
            pass

        return next_actions


site_action_items.register(AdverseEventAction)
