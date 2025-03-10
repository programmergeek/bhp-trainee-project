from django import forms

from ..models.subject_locator import SubjectLocator


class SubjectLocatorForm(forms.ModelForm):

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = SubjectLocator
        fields = '__all__'
