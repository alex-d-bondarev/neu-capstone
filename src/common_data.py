from collections import namedtuple

Synonyms = namedtuple("Synonyms", "main all")

NA_SYNONYMS = Synonyms('na', ['na', 'n/a', 'n\\a'])

SYNONYMS_LIST = [
    Synonyms('in process', ['in the process', 'doing', 'in progress']),
    Synonyms('budget', ['budget', 'cost']),
    Synonyms('pandemic', ['pandemic', 'covid', 'covid-19']),
    Synonyms('partner', ['partner', 'buyer', 'franchisee']),
    NA_SYNONYMS,
]

NO_RESPONSE = 'no_response'

DROP_WORDS = ['who', 'impacts']
