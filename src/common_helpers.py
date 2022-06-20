import re
from collections import Counter
from typing import List, Tuple

from pandas import Series


def make_text_pandas_header_compatible(text: str) -> str:
    """
    Remove all characters from the given text that are not English letters,
    numbers, and " " (space character). Trim spaces
    return updated text
    """
    text = re.sub('[^A-Za-z\d ]+', '', text)
    return text.strip()


def get_counter_with_top(nouns_freq: Counter, top: int) -> Counter:
    top_nouns = nouns_freq.most_common(top)
    print(f'All keywords:\n{nouns_freq}')

    display_counter = Counter()
    for (k, v) in top_nouns:
        display_counter[k] = v

    return display_counter


def split_out_other_answers(
        series: Series, main_values: List) -> Tuple[Series, Series]:
    """Split multichoice responses with "Other" series
    into main answers series
    and "other" answers series

    :param series:
    :param main_values:
    :return:
    """
    temp_s = series.str.split(';').apply(Series).stack()
    temp_s.index = temp_s.index.droplevel(-1)

    main_series = temp_s[temp_s.isin(main_values)]
    other_series = temp_s[~temp_s.isin(main_values)]

    return main_series, other_series
