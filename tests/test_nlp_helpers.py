from collections import Counter

import pandas

from src.common_data import NO_RESPONSE, NA_SYNONYMS
from src.extended_pandas_series import ExtendedSeries
from src.nlp_helpers import NlpHelper

INITIAL_SERIES = pandas.Series(
    data=[
        'Approach franchisee, not only as a buyers, but also as a partners',
        'The Covid-19 pandemic was a big issue for my approach ',
        'n/a',
        'na',
        pandas.NA,
        ''
    ], name="test")

RAW_LIST = [
    'approach franchisee, not only as a buyers, but also as a partners',
    'the covid-19 pandemic was a big issue for my approach',
    NA_SYNONYMS.main,
    NA_SYNONYMS.main,
    NA_SYNONYMS.main,
    NO_RESPONSE
]

NLP_LIST = [
    ['approach', 'franchisee', 'buyers', 'partners'],
    ['covid-19', 'pandemic', 'issue', 'approach'],
    [NA_SYNONYMS.main],
    [NA_SYNONYMS.main],
    [NA_SYNONYMS.main],
    [NO_RESPONSE]
]

NO_SYNONYMS_LIST = [
    ['approach', 'partner'],
    ['approach', 'issue', 'pandemic'],
    [NA_SYNONYMS.main],
    [NA_SYNONYMS.main],
    [NA_SYNONYMS.main],
    [NO_RESPONSE]
]

COUNTER_RESULT = Counter({
    NA_SYNONYMS.main: 3,
    'approach': 2,
    'issue': 1,
    'partner': 1,
    'pandemic': 1,
    NO_RESPONSE: 1
})


def test_raw_list_of_strings_is_extracted_from_series():
    initial_series = ExtendedSeries(INITIAL_SERIES.copy())
    expected = RAW_LIST.copy()

    actual = NlpHelper().get_raw_list_of_lower_strings_from_series(
        series=initial_series)

    assert actual == expected


def test_raw_list_is_nlp_processed():
    initial = RAW_LIST.copy()
    expected = NLP_LIST.copy()

    actual = NlpHelper().get_nouns_from_raw_list(initial)

    assert actual == expected


def test_synonyms_are_replaced():
    initial = NLP_LIST.copy()
    expected = NO_SYNONYMS_LIST.copy()

    actual = NlpHelper().remove_synonyms(initial)

    assert actual == expected


def test_counter_from_processed_values():
    initial = NO_SYNONYMS_LIST.copy()
    expected = COUNTER_RESULT.copy()

    actual = NlpHelper().count_unique_occurrences(initial)

    assert actual == expected


def test_entire_nlp_process():
    initial_series = ExtendedSeries(INITIAL_SERIES.copy())
    expected = COUNTER_RESULT.copy()

    actual = NlpHelper().count_series(series=initial_series)

    assert actual == expected
