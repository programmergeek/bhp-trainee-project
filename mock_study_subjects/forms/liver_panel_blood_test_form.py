from django import forms
from ..models.liver_panel_blood_test_result import LiverPanelBloodTestResult


class LiverPanelTestForm(forms.ModelForm):

    class Meta:
        model = LiverPanelBloodTestResult
        fields = '__all__'
