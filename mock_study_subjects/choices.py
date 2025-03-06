from .constants import NOT_APPLICABLE

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
