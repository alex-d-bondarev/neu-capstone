import pandas

from src.common_data import NO_RESPONSE
from src.extended_pandas_series import ExtendedSeries
from src.nlp_helpers import NlpHelper

INITIAL_SERIES = ExtendedSeries(pandas.Series(
    data=[
        'Approach franchisee, not only as a buyers, but also as a partners',
        'The Covid-19 pandemic was a big issue',
        'N/A',
        pandas.NA,
    ], name="test"))


def test_raw_list_of_strings_is_extracted_from_series():
    expected = [
        'approach franchisee, not only as a buyers, but also as a partners',
        'the covid-19 pandemic was a big issue',
        'n/a',
        'n/a',
        'n/a',
        NO_RESPONSE
    ]
    initial_series = ExtendedSeries(pandas.Series(
        data=[
            'Approach franchisee, not only as a buyers, but also as a partners',
            'The Covid-19 pandemic was a big issue ',
            'n/a',
            'na',
            pandas.NA,
            ''
        ], name="test")
    )

    actual = NlpHelper().get_raw_list_of_lower_strings_from_series(
        series=initial_series)

    assert actual == expected


def test_raw_list_is_nlp_processed():
    initial = [
        'approach franchisee, not only as a buyers, but also as a partners',
        'the covid-19 pandemic was a big issue',
        'n/a',
        NO_RESPONSE
    ]

    expected = [
        'Approach franchisee, not only as a buyers, but also as a partners',
        'The Covid-19 pandemic was a big issue',
        'n/a',
    ]
