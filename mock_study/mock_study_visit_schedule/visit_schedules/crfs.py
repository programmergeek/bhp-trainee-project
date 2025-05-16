from edc_visit_schedule import FormsCollection, Crf

crfs = {}

visit0_crfs = FormsCollection(
    Crf(show_order=1, model='mock_study_subjects.symptoms'),
    Crf(show_order=2, model='mock_study_subjects.baseriskassessment'),
    Crf(show_order=3, model='mock_study_subjects.baseriskassessmentalcohol'),
    Crf(show_order=4, model='mock_study_subjects.baseriskassessmentphysicalactivity'),
    Crf(show_order=5, model='mock_study_subjects.baseriskassessmentdiet'),
    Crf(show_order=6, model='mock_study_subjects.baseriskassessmentfamily'),
    Crf(show_order=7, model='mock_study_subjects.baseriskassessmentdemographics'),
    Crf(show_order=8, model='mock_study_subjects.baseriskassessmenthealth'),
    Crf(show_order=9, model='mock_study_subjects.baseriskassessmentcaffeine'),
    Crf(show_order=10, model='mock_study_subjects.baseriskassessmentsleep'),
    Crf(show_order=11, model='mock_study_subjects.baseriskassessmentstress'),
    name='screening'
)
crfs.update({'V0': visit0_crfs})

visit1_crfs = FormsCollection(
    Crf(show_order=1, model='mock_study_subjects.subjectvitals'),
    Crf(show_order=2, model='mock_study_subjects.drugadministration'),
    Crf(show_order=3, model='mock_study_subjects.drugresponse'),
    Crf(show_order=4, model='mock_study_subjects.symptoms'),
    name='visit 1'
)
crfs.update({'V1': visit1_crfs})

visit2_crfs = FormsCollection(
    Crf(show_order=1, model='mock_study_subjects.subjectvitals'),
    Crf(show_order=2, model='mock_study_subjects.drugadministration'),
    Crf(show_order=3, model='mock_study_subjects.drugresponse'),
    Crf(show_order=4, model='mock_study_subjects.symptoms'),
    name='visit 2'
)
crfs.update({'V2': visit2_crfs})

visit3_crfs = FormsCollection(
    Crf(show_order=1, model='mock_study_subjects.subjectvitals'),
    Crf(show_order=2, model='mock_study_subjects.symptoms'),
    name='visit 3'
)
crfs.update({'V3': visit3_crfs})
