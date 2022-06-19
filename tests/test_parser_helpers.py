from typing import Callable, List

import numpy
import pandas
from pandas import Series

from src.extended_pandas_series import ExtendedSeries
from src.parser_helpers import make_text_pandas_header_compatible

EXAMPLE_VALUES = [
    'valid response', 'N/A', ' ', '', ' test', 'test ', pandas.NA, numpy.nan,
    None, 'None', 'none', 'Na', 'na', 1, 0, 'In Process', 'in the process'
]
EXAMPLE_DATAFRAME = pandas.DataFrame({'test': EXAMPLE_VALUES})
EXAMPLE_DATAFRAME_COPY = EXAMPLE_DATAFRAME.copy()


def _assert_series_is_expected_and_initial_series_did_not_change(
        actual_series: Series, expected_data: List) -> None:
    expected = pandas.Series(
        data=expected_data,
        name="test")
    pandas.testing.assert_series_equal(
        actual_series,
        expected
    )


def test_pandas_headers_renaming():
    question_before = 'What have been your biggest challenges in supporting your franchisees (select all that apply)?2 '
    question_after = 'What have been your biggest challenges in supporting your franchisees select all that apply2'

    assert make_text_pandas_header_compatible(question_before) == question_after

    pandas.testing.assert_frame_equal(EXAMPLE_DATAFRAME, EXAMPLE_DATAFRAME_COPY)


def test_empty_values_replaced_with_no_response():
    expected_data = [
        'valid response', 'n/a', 'no response', 'no response', ' test',
        'test ', pandas.NA, numpy.nan, None, 'none', 'none', 'na', 'na',
        1, 0, 'in process', 'in the process'
    ]

    _assert_series_is_expected_and_initial_series_did_not_change(
        actual_series=ExtendedSeries(EXAMPLE_DATAFRAME['test']).mark_no_responses(),
        expected_data=expected_data
    )


def test_trim_spaces():
    expected_data = [
        'valid response', 'n/a', '', '', 'test', 'test', pandas.NA,
        numpy.nan, None, 'none', 'none', 'na', 'na', 1, 0, 'in process',
        'in the process'
    ]

    _assert_series_is_expected_and_initial_series_did_not_change(
        actual_series=ExtendedSeries(EXAMPLE_DATAFRAME['test']).trim_spaces(),
        expected_data=expected_data
    )


def test_na_replaced_with_zeros():
    expected_data = [
        'valid response', '0', ' ', '', ' test', 'test ', '0', '0', '0',
        'none', 'none', '0', '0', 1, 0, 'in process', 'in the process'
    ]

    _assert_series_is_expected_and_initial_series_did_not_change(
        actual_series=ExtendedSeries(EXAMPLE_DATAFRAME['test']).replace_na_with_zeros(),
        expected_data=expected_data
    )


def test_similar_answers_replaced():
    expected_data = [
        'valid response', 'n/a', ' ', '', ' test', 'test ', pandas.NA, numpy.nan,
        None, 'none', 'none', 'na', 'na', 1, 0, 'in process', 'in process'
    ]

    _assert_series_is_expected_and_initial_series_did_not_change(
        actual_series=ExtendedSeries(EXAMPLE_DATAFRAME['test']).replace_similar_answers(),
        expected_data=expected_data
    )
