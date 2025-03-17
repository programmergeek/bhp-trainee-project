from .constants import NOT_APPLICABLE, OFF_STUDY, OTHER

YES_NO = (('yes', "Yes"), ('no', 'No'))

VISIT_INFO_SOURCE = (
    ('', ''),
)

VISIT_UNSCHEDULED_REASON = (('', ''),)

VISIT_REASON = (('', ''),)

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
