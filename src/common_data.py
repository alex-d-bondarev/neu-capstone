from collections import namedtuple

Synonyms = namedtuple("Synonyms", "index all")

SYNONYMS_LIST = [
    Synonyms('in process', ['in the process', 'doing', 'in progress']),
    Synonyms('budget', ['budget', 'cost']),
    Synonyms('pandemic', ['pandemic', 'covid', 'covid-19']),
    Synonyms('partner', ['partner', 'buyer', 'franchisee']),
]

NO_RESPONSE = 'no response'
