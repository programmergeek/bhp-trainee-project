from .constants import NOT_APPLICABLE, OFF_STUDY, OTHER

YES_NO = (('yes', "Yes"), ('no', 'No'))

VISIT_INFO_SOURCE = (
    ('Clinic visit w/ subject', 'Clinic visit with participant'),
    ('Other contact w/ subject', 'Other contact with participant (i.e telephone call)'),
    ('Contact w/ health worker', 'Contact with health care worker'),
    ('Contact w/ family/design',
     'Contact with family or designated person who can provide information'),
    ('OTHER', 'Other,specify'),
)

VISIT_UNSCHEDULED_REASON = (
    ('Routine oncology', 'Routine oncology clinic visit (i.e. planned chemo, follow-up)'),
    ('Ill oncology', 'Ill oncology clinic visit'),
    ('Patient called', 'Patient called to come for visit'),
    (NOT_APPLICABLE, 'Not Applicable'),
    ('OTHER', 'Other, specify:'),
)

VISIT_REASON = (
    ('Quarterly visit/contact', 'Quarterly visit/contact'),
    ('Unscheduled visit/contact', 'Unscheduled visit/contact'),
    ('Missed quarterly visit', 'Missed quarterly visit'),
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
