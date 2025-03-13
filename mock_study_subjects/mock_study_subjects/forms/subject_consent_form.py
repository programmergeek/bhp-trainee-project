from django import forms

from ..choices import ID_TYPE
from ..models.subject_consent import SubjectConsent


class SubjectConsentForm(forms.ModelForm):

    identity_type = forms.CharField(
        label='What type of identity number is this?',
        widget=forms.RadioSelect(choices=list(ID_TYPE)))

    class Meta:
        model = SubjectConsent
        fields = '__all__'
