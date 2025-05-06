from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from .crfs import crfs
from .requisitions import requisitions

schedule = Schedule(
    name='mock_study_schedule',
    verbose_name='Mock Study',
    onschedule_model='mock_study_subjects.onschedule',
    offschedule_model='mock_study_prn.subjectoffstudy',
    consent_model='mock_study_subjects.subjectconsent',
    appointment_model='mock_study_subjects.appointment'
)

visit1 = Visit(
    code='1',
    title='Screening (Day 0)',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crfs.get(''),
    facility_name='Princess Marina Hospital'
)

visit2 = Visit(
    code='2',
    title='Visit 1',
    timepoint=1,
    rbase=relativedelta(weeks=2),
    rupper=relativedelta(days=0),
    rlower=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crfs.get('')
)

visit3 = Visit(
    code='3',
    title='Visit 2',
    timepoint=2,
    rbase=relativedelta(weeks=6),
    rupper=relativedelta(days=0),
    rlower=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crfs.get('')
)

visit3 = Visit(
    code='4',
    title='Visit 3',
    timepoint=3,
    rbase=relativedelta(weeks=12),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crfs.get('')
)

schedule.add_visit(visit=visit1)
schedule.add_visit(visit=visit2)
schedule.add_visit(visit=visit3)
