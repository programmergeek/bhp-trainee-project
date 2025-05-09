import arrow
from datetime import datetime

from edc_consent.consent import Consent
from edc_consent.site_consents import site_consents
from edc_constants.constants import MALE, FEMALE

subject_consent_version_1 = Consent(
    'mock_study_subjects.subjectconsent',
    version='1',
    start=arrow.get(datetime(2024, 4, 30)).datetime,
    end=arrow.get(datetime(2028, 4, 3)).datetime,
    age_min=30,
    age_max=65,
    gender=[MALE, FEMALE]
)

site_consents.register(subject_consent_version_1)
