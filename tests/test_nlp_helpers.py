import pandas

from src.common_data import NO_RESPONSE, NA_SYNONYMS
from src.extended_pandas_series import ExtendedSeries
from src.nlp_helpers import NlpHelper

INITIAL_SERIES = pandas.Series(
    data=[
        'Approach franchisee, not only as a buyers, but also as a partners',
        'The Covid-19 pandemic was a big issue ',
        'n/a',
        'na',
        pandas.NA,
        ''
    ], name="test")

RAW_LIST = [
    'approach franchisee, not only as a buyers, but also as a partners',
    'the covid-19 pandemic was a big issue',
    NA_SYNONYMS.main,
    NA_SYNONYMS.main,
    NA_SYNONYMS.main,
    NO_RESPONSE
]

NLP_LIST = [
    ['approach', 'franchisee', 'buyers', 'partners'],
    ['covid-19', 'pandemic', 'issue'],
    [NA_SYNONYMS.main],
    [NA_SYNONYMS.main],
    [NA_SYNONYMS.main],
    [NO_RESPONSE]
]


def test_raw_list_of_strings_is_extracted_from_series():
    expected = RAW_LIST.copy()
    initial_series = ExtendedSeries(INITIAL_SERIES.copy())

    actual = NlpHelper().get_raw_list_of_lower_strings_from_series(
        series=initial_series)

    assert actual == expected


def test_raw_list_is_nlp_processed():
    initial = RAW_LIST.copy()
    expected = NLP_LIST.copy()

    actual = NlpHelper().get_nouns_from_raw_list(initial)

    assert actual == expected
