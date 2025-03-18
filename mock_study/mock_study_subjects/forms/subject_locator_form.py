from django import forms
from ..constants import YES, NO
from ..models.subject_locator import SubjectLocator
from edc_form_validators import FormValidatorMixin
from edc_locator.forms import SubjectLocatorFormValidator as BaseSubjectLocatorFormValidator


class SubjectLocatorFormValidator(BaseSubjectLocatorFormValidator):

    # This validato dynamically determines which fields are required based on the the responses from different questions
    def validate_indirect_contact(self):
        # inderect contact name is required if you have been allowed to contact them
        self.required_if(
            YES, field='may_contact_indirectly',
            field_required='indirect_contact_name')
        # relation to the indirect contact is required if you are allowed to contact them
        self.required_if(
            YES, field='may_contact_indirectly',
            field_required='indirect_contact_relation')
        # the inderect contact's numbers are required if you are allowed to contact them
        for field in ['indirect_contact_cell', 'indirect_contact_cell_alt',
                      'indirect_contact_phone']:
            self.not_required_if(
                NO, field='may_contact_indirectly', field_required=field,
                inverse=False)


class SubjectLocatorForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectLocatorFormValidator

    class Meta:
        model = SubjectLocator
        fields = '__all__'
