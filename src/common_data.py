from collections import namedtuple

Synonyms = namedtuple("Synonyms", "main all")

NA_SYNONYMS = Synonyms('na', ['na', 'n/a', 'n\\a', 'n//a'])

SYNONYMS_LIST = [
    Synonyms('in process', ['in the process', 'doing', 'in progress']),
    Synonyms('budget', ['budget', 'cost']),
    Synonyms('pandemic', ['pandemic', 'covid-19', 'covid']),
    Synonyms('partner', ['partners', 'buyers', 'franchisee', 'buyer', 'partner']),
    NA_SYNONYMS,
]

NO_RESPONSE = 'no_response'

DROP_WORDS = ['who', 'impacts']

PLOT_WIDTH = 6.5
DOUBLE_PLOT_HEIGHT = 12
SPACE_BETWEEN_PLOTS = 0.4
