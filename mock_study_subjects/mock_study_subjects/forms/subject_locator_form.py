from django import forms

from ..models.subject_locator import SubjectLocator


class SubjectLocatorForm(forms.ModelForm):

    class Meta:
        model = SubjectLocator
        fields = '__all__'
