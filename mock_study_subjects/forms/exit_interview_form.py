from django import forms

from ..models.exit_interview import ExitInterview


class ExitInterviewForm(forms.ModelForm):

    class Meta:
        model = ExitInterview
        fields = '__all__'
