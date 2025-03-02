from django import forms

from ..models.subject_screening import SubjectScreening


class SubjectScreeningFormMixin(forms.ModelForm):

    pass


class SubjectScreeningForm(SubjectScreeningFormMixin):

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    class Meta:
        model = SubjectScreening
        fields = '__all__'
