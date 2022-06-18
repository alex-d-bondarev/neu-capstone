from typing import Callable

import numpy
import pandas
from pandas import Series

from src.parser_helpers import (
    make_text_pandas_header_compatible, mark_no_responses,
    replace_na_with_zeros, trim_spaces)

EXAMPLE_VALUES = [
    'valid response', 'N/A', ' ', '', ' test', 'test ', pandas.NA, numpy.nan,
    None, 'None', 'none', 'Na', 'na', 1, 0
]
EXAMPLE_DATAFRAME = pandas.DataFrame({'test': EXAMPLE_VALUES})
EXAMPLE_DATAFRAME_COPY = EXAMPLE_DATAFRAME.copy()


def _assert_series_function_is_immutable_and_has_expected_result(
        func: Callable, expected: Series) -> None:
    pandas.testing.assert_series_equal(
        func(EXAMPLE_DATAFRAME['test']),
        expected
    )


def test_pandas_headers_renaming():
    question_before = 'What have been your biggest challenges in supporting your franchisees (select all that apply)?2 '
    question_after = 'What have been your biggest challenges in supporting your franchisees select all that apply2'

    assert make_text_pandas_header_compatible(question_before) == question_after

    pandas.testing.assert_frame_equal(EXAMPLE_DATAFRAME, EXAMPLE_DATAFRAME_COPY)


def test_empty_values_replaced_with_no_response():
    expected = pandas.Series(
        data=[
            'valid response', 'n/a', 'no response', 'no response', ' test',
            'test ', pandas.NA, numpy.nan, None, 'none', 'none', 'na', 'na',
            1, 0
        ],
        name="test")

    _assert_series_function_is_immutable_and_has_expected_result(
        func=mark_no_responses,
        expected=expected
    )


def test_trim_spaces():
    expected = pandas.Series(
        data=[
            'valid response', 'n/a', '', '', 'test', 'test', pandas.NA,
            numpy.nan, None, 'none', 'none', 'na', 'na', 1, 0
        ],
        name="test")

    _assert_series_function_is_immutable_and_has_expected_result(
        func=trim_spaces,
        expected=expected
    )


def test_na_replaced_with_zeros():
    expected = pandas.Series(
        data=[
            'valid response', '0', ' ', '', ' test', 'test ', '0', '0', '0', 'none', 'none', '0', '0', 1, 0
        ],
        name="test")

    _assert_series_function_is_immutable_and_has_expected_result(
        func=replace_na_with_zeros,
        expected=expected
    )
