import re


# TODO: Split this file from a single big general file to smaller files


def make_text_pandas_header_compatible(text: str) -> str:
    """
    Remove all characters from the given text that are not English letters,
    numbers, and " " (space character). Trim spaces
    return updated text
    """
    text = re.sub('[^A-Za-z\d ]+', '', text)
    return text.strip()
