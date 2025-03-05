from django.utils.translation import gettext as _

YES = 'Yes'

NO = 'No'

DEFAULT_BASE_FIELDS = [
    'id', 'created', 'modified', 'user_created',
    'user_modified', 'hostname_created', 'hostname_modified',
    'revision', 'device_created', 'device_modified']

MALE = 'M'

FEMALE = 'F'

GENDER = (
    (MALE, _('Male')),
    (FEMALE, _('Female')),
)
