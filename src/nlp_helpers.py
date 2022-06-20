from typing import List

import spacy

from src.extended_pandas_series import ExtendedSeries


class NlpHelper:
    """Helper methods for parsing text"""

    def __init__(self):
        self.nlp = self._get_spacy_nlp_model()
        self.raw_list_of_values: List[str] = list()

    @staticmethod
    def _get_spacy_nlp_model() -> spacy.Language:
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

    def get_raw_list_of_lower_strings_from_series(
            self, series: ExtendedSeries) -> List[str]:
        """Self Evident

        :param series:
        """
        self.raw_list_of_values = [
            value.lower()
            for value in
            series.trim_spaces().mark_no_responses().group_na_values().tolist()
            if isinstance(value, str)]
        return self.raw_list_of_values
