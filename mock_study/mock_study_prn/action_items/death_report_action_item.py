from django.apps import apps
from edc_action_item import Action, site_action_items
from django.core.exceptions import ObjectDoesNotExist
from .subject_offstudy_action_item import SubjectOffStudyAction


DEATH_REPORT_ACTION_ITEM_NAME = "death_report"


class DeathReportAction(Action):
    name = DEATH_REPORT_ACTION_ITEM_NAME
    display_name = 'Death Report'
    reference_model = 'mock_study_prn.deathreport'
    singleton = True

    def get_next_actions(self):
        next_actions = []
        death_report_cls = apps.get_model('mock_study_prn.deathreport')

        subject_identifier = self.reference_model_cls().subject_identifier

        try:
            death_report_cls.object.get(subject_identifier=subject_identifier)
            next_actions = [SubjectOffStudyAction]
        except ObjectDoesNotExist:
            pass

        return next_actions
