from edc_search.model_mixins import SearchSlugModelMixin as BaseSearchSlugModelMixin


class SearchSlugMixin(BaseSearchSlugModelMixin):

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.append('subject_identifier')
        return fields

    class Meta:
        abstract = True
