from django.db.models.signals import post_save
from django.dispatch import receiver
from edc_visit_schedule import site_visit_schedules
from .subject_consent import SubjectConsent


@receiver(post_save, sender=SubjectConsent, dispatch_uid="add_subject_onschedule_on_consent_post_save")
def add_subject_onschedule_on_consent_post_save(sender, instance, raw, created, **kwargs):
    if not raw:
        if created:
            _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                onschedule_model='mock_study_subjects.onschedule',
                name=instance.schedule_name
            ),
            schedule.put_on_schedule(
                subject_identifier=instance.subject_identifier,
                onschedule_datetime=instance.report_datetime,
            )
