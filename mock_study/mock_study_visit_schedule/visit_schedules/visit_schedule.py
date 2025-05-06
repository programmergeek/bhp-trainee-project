from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedule import schedule

visit_schedule = VisitSchedule(
    name='mock_study_visit_schedule',
    verbose_name='Mock Study Visit Schedule',
    offstudy_model='mock_study_prn.subjectoffstudy',
    locator_model='mock_study_subjects.subjectlocator',
    death_report_model='mock_study_prn.deathreport',
    previous_visit_schedule=None
)

visit_schedule.add_schedule(schedule)

site_visit_schedules.register(visit_schedule)
