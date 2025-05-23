from edc_dashboard.listboard_filter import ListboardFilter, ListboardViewFilters


class ScreeningListBoardFilters(ListboardViewFilters):

    all = ListboardFilter(
        name='all',
        label='All',
        lookup={})

    eligible = ListboardFilter(
        label='Eligible',
        position=10,
        lookup={'eligible': True})

    not_eligible = ListboardFilter(
        label='Not Eligible',
        position=11,
        lookup={'eligible': False})

    consented = ListboardFilter(
        label='Consented',
        position=20,
        lookup={'eligible': True,
                'subjectconsent__isnull': False})

    not_consented = ListboardFilter(
        label='Not consented',
        position=21,
        lookup={'eligible': True,
                'subjectconsent__isnull': True})
