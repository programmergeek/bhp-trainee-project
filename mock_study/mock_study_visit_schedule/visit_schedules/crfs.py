from edc_visit_schedule import FormsCollection, Crf

crfs = {}

visit0_crfs = FormsCollection(
    Crf(show_order=1, model='mock_study_subjects.subjectvitals'),
    name='screening'
)
crfs.update({'V0': visit0_crfs})

visit1_crfs = FormsCollection(
    Crf(show_order=1, model='mock_study_subjects.subjectvitals'),
    Crf(show_order=2, model='mock_study_subjects.drugadministration'),
    name='visit 1'
)
crfs.update({'V1': visit1_crfs})

visit2_crfs = FormsCollection(
    Crf(show_order=1, model='mock_study_subjects.subjectvitals'),
    Crf(show_order=2, model='mock_study_subjects.drugadministration'),
    name='visit 2'
)
crfs.update({'V2': visit2_crfs})

visit3_crfs = FormsCollection(
    Crf(show_order=1, model='mock_study_subjects.subjectvitals'),
    Crf(show_order=2, model='mock_study_subjects.drugadministration'),
    name='visit 3'
)
crfs.update({'V3': visit3_crfs})
