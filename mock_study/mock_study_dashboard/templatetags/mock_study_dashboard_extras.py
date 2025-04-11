from django import template

register = template.Library()


@register.inclusion_tag('mock_study_dashboard/templates/buttons/screening_button.html')
def screening_button(model_wrapper):
    title = ['Add subject\'s screening form']
    return dict(
        screening_identifier=model_wrapper.object.screening_identifier,
        add_subject_screening_href=model_wrapper.subject_screening.href,
        subject_screening_model_obj=model_wrapper.subject_screening_model_obj,
        title=' '.join(title)
    )
