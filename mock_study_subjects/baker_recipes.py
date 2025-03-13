from model_bakery.recipe import Recipe
from .models.subject_screening import SubjectScreening
from .constants import YES, NO

patient_doe = Recipe(
    SubjectScreening,
    has_hypertension=YES,
    age=50,
    is_pregnant=NO,
    is_breastfeeding=NO,
    has_allergies_to_drug=NO,
    has_history_of_severe_cardiovascular_events=NO,
    enrollment_site='princess_marina_hospital'
)

patient_james = Recipe(
    SubjectScreening,
    has_hypertension=YES,
    age=15,
    is_pregnant=YES,
    is_breastfeeding=NO,
    has_allergies_to_drug=NO,
    has_history_of_severe_cardiovascular_events=NO,
    enrollment_site='princess_marina_hospital'
)
