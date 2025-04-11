from ..constants import MISSED_VISIT
from edc_constants.constants import OTHER
from edc_visit_tracking.form_validators import VisitFormValidator as BaseVisitFormValidator


class VisitFormValidator(BaseVisitFormValidator):

    def validate_required_fields(self):

        # if the reason for a visit is becuase the participant missed a visit, then the reason why they missed the visit is required
        self.required_if(
            MISSED_VISIT,
            field='reason',
            field_required='reason_missed')

        # if the visit is unscheduled then the reason for the unscheduled visit is required
        self.required_if(
            'Unscheduled visit/contact',
            field='reason',
            field_required='reason_unscheduled')

        # if the information provided in the visit from some place other than a
        # face to face meeting, or a call, with the participant, talking to
        # family or some designated person, or other listed information sources,
        # then you are required to specify how that information was obtained.
        self.required_if(
            OTHER,
            field='info_source',
            field_required='info_source_other')
        # if there is some other reason that the visit is unscheduled besides the ones listed, then you need to specify them.
        self.required_if(
            OTHER,
            field='reason_unscheduled',
            field_required='reason_unscheduled_other')
