import re

import spacy

# TODO: Split this file from a single big general file to smaller files
from pandas import Series


def get_spacy_nlp_model() -> spacy.Language:
    """
    Return spacy en_core_web_sm NLP model
    Download it if the model is not present (usually happens only once)
    """
    spacy_model = 'en_core_web_sm'
    try:
        return spacy.load(spacy_model)
    except OSError:
        print('===\nDownloading language model for a spaCy NLP model\n'
              '(don\'t worry, this will only happen once)\n===')
        from spacy.cli import download
        download(spacy_model)
        print('===\nFinished downloading the spaCy NLP model.\n===')
        return spacy.load(spacy_model)


def make_text_pandas_header_compatible(text: str) -> str:
    """
    Remove all characters from the given text that are not English letters,
    numbers, and " " (space character). Trim spaces
    return updated text
    """
    text = re.sub('[^A-Za-z\d ]+', '', text)
    return text.strip()


def make_lower_case_series_copy(series: Series) -> Series:
    """Self evident

    :param series:
    :return:
    """
    return series.copy().apply(
        lambda value: value.lower() if isinstance(value, str) else value)


def mark_no_responses(series: Series) -> Series:
    """
    Return a new series where empty responses are marked as 'no response'.
    Returned values are all lower case.
    :param series:
    :param param:
    """
    return make_lower_case_series_copy(series).\
        replace([' ', ''], 'no response')


def trim_spaces(series: Series) -> Series:
    """
    Return a new series where spaces are trimmed.
    Returned values are all lower case.
    :param series:
    """
    return make_lower_case_series_copy(series).apply(
        lambda value: value.strip() if isinstance(value, str) else value)


def replace_na_with_zeros(series: Series) -> Series:
    """
    Replace all None and N/A related values with 0 string.
    Returned values are all lower case.
    :param series:
    """
    return make_lower_case_series_copy(series). \
        fillna('0'). \
        apply(lambda value: value.lower() if isinstance(value, str) else value). \
        replace(['na', 'n/a', 'n\\a'], '0')
