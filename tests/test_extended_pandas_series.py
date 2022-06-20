import numpy
import pandas

from src.common_data import NO_RESPONSE, NA_SYNONYMS
from src.extended_pandas_series import ExtendedSeries

EXAMPLE_VALUES = [
    'valid response', 'N/A', ' ', '', ' test', 'test ', pandas.NA, numpy.nan,
    None, 'None', 'none', 'Na', 'na', 1, 0, 'In Process', 'in the process'
]
EXAMPLE_DATAFRAME = pandas.DataFrame({'test': EXAMPLE_VALUES})
EXAMPLE_DATAFRAME_COPY = EXAMPLE_DATAFRAME.copy()


def test_empty_values_replaced_with_no_response():
    expected = [
        'valid response', 'n/a', NO_RESPONSE, NO_RESPONSE, ' test',
        'test ', pandas.NA, numpy.nan, None, 'none', 'none', 'na', 'na',
        1, 0, 'in process', 'in the process'
    ]

    actual = ExtendedSeries(
        EXAMPLE_DATAFRAME['test']).mark_no_responses().tolist()
    assert actual == expected


def test_trim_spaces():
    expected = [
        'valid response', 'n/a', '', '', 'test', 'test', pandas.NA,
        numpy.nan, None, 'none', 'none', 'na', 'na', 1, 0, 'in process',
        'in the process'
    ]

    actual = ExtendedSeries(EXAMPLE_DATAFRAME['test']).trim_spaces().tolist()
    assert actual == expected


def test_na_grouped():
    expected = [
        'valid response', NA_SYNONYMS.main, ' ', '', ' test', 'test ',
        NA_SYNONYMS.main, NA_SYNONYMS.main, NA_SYNONYMS.main, 'none', 'none',
        NA_SYNONYMS.main, NA_SYNONYMS.main, 1, 0, 'in process', 'in the process'
    ]

    actual = ExtendedSeries(
        EXAMPLE_DATAFRAME['test']).group_na_values().tolist()
    assert actual == expected


def test_similar_answers_replaced():
    expected = [
        'valid response', 'n/a', ' ', '', ' test', 'test ', pandas.NA, numpy.nan,
        None, 'none', 'none', 'na', 'na', 1, 0, 'in process', 'in process'
    ]

    actual = ExtendedSeries(
        EXAMPLE_DATAFRAME['test']).replace_similar_answers().tolist()
    assert actual == expected


def test_no_nan_records():
    expected = [
        'valid response', 'N/A', ' ', '', ' test', 'test ', 'None',
        'none', 'Na', 'na', 1, 0, 'In Process', 'in the process'
    ]

    actual = ExtendedSeries(
        EXAMPLE_DATAFRAME['test']).filter_out_nan().tolist()
    assert actual == expected


def test_data_is_prepared_for_bar_chart():
    initial_data = [
        '2021', '2022', '2022', 'In process ', pandas.NA, pandas.NA, '2019',
        pandas.NA, pandas.NA, '2007', pandas.NA, pandas.NA, '2022',
        'currently planning', pandas.NA, 'in the process', 'Have not yet',
        pandas.NA, '2017-18', pandas.NA, pandas.NA, pandas.NA, '2022',
    ]
    initial_series = ExtendedSeries(pandas.Series(
        data=initial_data, name="test"))
    expected_values = [NA_SYNONYMS.main, '2022', 'in process', '2007', '2017-18', '2019',
                       '2021', 'currently planning', 'have not yet']
    expected_counts = [47.8, 17.4, 8.7, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3]

    actual_data = initial_series.prepare_data_for_plotting()

    assert actual_data.keys().tolist() == expected_values
    assert actual_data.tolist() == expected_counts


def test_series_to_string_merge():
    initial_series = ExtendedSeries(pandas.Series(
        data=['test', 'some text', 2], name="test"))
    expected_string = 'test some text 2'

    assert initial_series.merge_to_string() == expected_string
