from edc_identifier.simple_identifier import SimpleUniqueIdentifier


class ScreeningIdentifier(SimpleUniqueIdentifier):

    random_string_length = 10
    identifier_type = 'screening_identifier'
