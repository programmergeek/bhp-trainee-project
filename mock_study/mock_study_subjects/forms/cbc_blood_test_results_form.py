from django import forms
from ..models.cbc_blood_test_result import CBCBloodTestResult


class CBCBloodTestResultForm(forms.ModelForm):

    class Meta:
        model = CBCBloodTestResult
        fields = '__all__'
