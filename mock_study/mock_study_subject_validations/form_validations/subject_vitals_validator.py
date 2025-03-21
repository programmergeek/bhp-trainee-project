from edc_form_validators import FormValidator
from django import forms


class SubjectVitalsValidator(FormValidator):

    def clean(self):
        super().clean()
        self.clean_vitals()

    def clean_vitals(self):

        data = self.cleaned_data

        systolic = data.get('systolic_blood_pressure')
        diastolic = data.get('diastolic_blood_pressure')
        heart_rate = data.get('heart_rate')
        height = data.get('height')
        weight = data.get('weight')

        if (systolic >= 250):
            raise forms.ValidationError({
                'systolic_blood_pressure': 'Value is too high',
            })

        if (diastolic >= 250):
            raise forms.ValidationError({
                'diastolic_blood_pressure': 'Value is too high',
            })

        if (heart_rate >= 200):
            raise forms.ValidationError({
                'heart_rate': 'Value is too high',
            })

        if (height >= 300):
            raise forms.ValidationError({
                'height': 'Value is too high',
            })

        if (weight >= 500):
            raise forms.ValidationError({
                'weightt': 'Value is too high',
            })

        if (systolic <= 50):
            raise forms.ValidationError({
                'systolic_blood_pressure': 'Value is too low',
            })

        if (diastolic <= 50):
            raise forms.ValidationError({
                'diastolic_blood_pressure': 'Value is too low',
            })

        if (heart_rate <= 30):
            raise forms.ValidationError({
                'heart_rate': 'Value is too low',
            })

        if (height <= 0):
            raise forms.ValidationError({
                'height': 'Value is too low',
            })

        if (weight >= 40):
            raise forms.ValidationError({
                'weightt': 'Value is too low',
            })
