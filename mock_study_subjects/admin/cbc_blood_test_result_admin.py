from django.contrib import admin

from ..admin_site import mock_study_admin
from ..forms.cbc_blood_test_results_form import CBCBloodTestResultForm
from ..models.cbc_blood_test_result import CBCBloodTestResult


@admin.register(CBCBloodTestResult, site=mock_study_admin)
class CBCBloodTestResultAdmin(admin.ModelAdmin):

    form = CBCBloodTestResultForm

    fieldsets = ((None, {
        'fields': [

        ]
    }),)
