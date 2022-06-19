import re

import spacy


# TODO: Split this file from a single big general file to smaller files


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
