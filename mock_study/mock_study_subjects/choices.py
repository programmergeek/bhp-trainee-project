from .constants import NOT_APPLICABLE, OFF_STUDY, OTHER, MALE, FEMALE
from django.utils.translation import gettext as _


YES_NO = (('yes', "Yes"), ('no', 'No'))

VISIT_INFO_SOURCE = (
    ('Clinic visit w/ subject', 'Clinic visit with participant'),
    ('Other contact w/ subject', 'Other contact with participant (i.e telephone call)'),
    ('Contact w/ family/design',
     'Contact with family or designated person who can provide information'),
    ('OTHER', 'Other,specify'),
)

VISIT_UNSCHEDULED_REASON = (
    ('Patient called', 'Patient called to come for visit'),
    (NOT_APPLICABLE, 'Not Applicable'),
    ('OTHER', 'Other, specify:'),
)

VISIT_REASON = (
    ('Weekly visit/contact', 'Weekly visit/contact'),
    ('Unscheduled visit/contact', 'Unscheduled visit/contact'),
    ('Missed missed visit', 'Missed weekly visit'),
    ('Lost to follow-up', 'Lost to follow-up (use only when taking subject off study)'),
    ('Death', 'Death'),
    (OFF_STUDY, 'Off study'),
    ('deferred', 'Deferred'),
)

ID_TYPE = (
    ('country_id', 'Country ID number'),
    ('drivers_licence', 'Driver\'s license'),
    ('passport', 'Passport'),
    ('country_id_rcpt', 'Country ID receipt'),
    (OTHER, 'Other'),
)

ENROLLMENT_SITES = (
    ('gaborone_private_hospital', 'Gaborone Private Hospital (GPH)'),
    ('nyangabgwe_referral_hospital', 'Nyangabgwe Referral Hospital (NRH)'),
    ('princess_marina_hospital', 'Princess Marina Hospital (PMH)'),
    ('bokamoso_private_hospital', 'Bokamoso Private Hospital (BPH)'),
)

SEVERITY = (('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'))

TESTING_SITES = (
    ('optimum_health_medical_laboratory', 'Optimum Health Mediacal Laboratory'),
    ('diagnofirm_medical_laboratories', 'Diagnofirm Medical Laboratories'),
    ('mmoloki_medical_laboratories', 'Mmoloki Medical Laboratories')
)

TESTING_STATUS = (('pending', 'Pending'), ('complete', 'Complete'))

ANTICOAGULANTS = (('heparin', 'Heparin'), ('citrate', 'Citrate'))

GENDER = (
    (MALE, _('Male')),
    (FEMALE, _('Female')),
)

MARITAL_STATUS = (
    ('single', 'Single'),
    ('married', 'Married'),
    ('divorced', 'Divorced'),
    ('widowed', 'Widowed'),
    (OTHER, 'Other')
)

RACE = (
    ('black', 'Black'),
    ('white', 'White'),
    ('asian', 'Asian'),
    ('hispanic', 'Hispanic'),
    (OTHER, 'Other'),
)

EDUCATION = (
    ('psle', 'PSLE'),
    ('jse', 'CJSE'),
    ('bgcse', 'BGCSE'),
    ('igcse', 'IGCSE'),
    ('undergraduate', 'Undergraduate'),
    ('masters', 'Masters'),
    ('phd', 'PHD'),
    (OTHER, 'Other'),
)

RATING_SCALE = (('strongly_agree', 'Stongly Agree'), ('agree', 'Agree'), ('neutral',
                'Neutral'), ('disagree', 'Disagree'), ('strongly_disagree', 'Strongly Disagree'))
