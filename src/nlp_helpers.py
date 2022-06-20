import copy
import re
from collections import Counter
from typing import List

import spacy

from spacy.tokens import Doc, Token
from src.common_data import DROP_WORDS, NA_SYNONYMS, Synonyms, SYNONYMS_LIST
from src.extended_pandas_series import ExtendedSeries


class NlpHelper:
    """Helper methods for parsing text"""

    def __init__(self):
        self.nlp = self._get_spacy_nlp_model()
        self.raw_list_of_values: List[str] = list()
        self.filtered_values: List[List[str]] = list()
        self.no_synonyms_list: List[List[str]] = list()

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

    def get_nouns_from_raw_list(
            self, raw_list: List[str] = None) -> List[List[str]]:
        """Use nlp library to extract only nouns,
        in singular form from a given list

        :param raw_list:
        """
        if raw_list is None:
            raw_list = self.raw_list_of_values

        self.filtered_values = [
            self._filter_out_nouns(self.nlp(value)) for value in raw_list]

        return self.filtered_values

    def _filter_out_nouns(self, doc: Doc) -> List[str]:
        return [
            token.text
            for token in doc if
            (
                    self._is_noun(token=token)
                    and not token.is_stop
                    and not token.is_punct
                    and token.text not in DROP_WORDS
            ) or (
                    token.text == NA_SYNONYMS.main
            )
        ]

    @staticmethod
    def _is_noun(token: Token) -> bool:
        return (token.pos_ == "NOUN"
                or token.pos_ == "PROPN"
                or token.pos_ == "PRON")

    def remove_synonyms(
            self, values: List[List[str]] = None) -> List[List[str]]:
        """Self evident

        :param values:
        :return:
        """
        if values is None:
            values = self.filtered_values

        self.no_synonyms_list = copy.deepcopy(values)

        for synonyms in SYNONYMS_LIST:
            self.no_synonyms_list = self._replace_given_synonyms(
                synonyms=synonyms)

        for row_id, row in enumerate(self.no_synonyms_list):
            self.no_synonyms_list[row_id] = sorted(list(set(row)))

        return self.no_synonyms_list

    def _replace_given_synonyms(
            self, synonyms: Synonyms) -> List[List[str]]:

        result = copy.deepcopy(self.no_synonyms_list)
        synonyms_for_regex = "|".join(synonyms.all)
        pattern = f'({synonyms_for_regex})'

        for row_id, row in enumerate(result):
            for word_id, word in enumerate(row):
                result[row_id][word_id] = re.sub(
                    pattern=pattern, repl=synonyms.main, string=word)

        return result

    def count_unique_occurrences(
            self, values: List[List[str]] = None) -> Counter:
        """Self evident

        :param values:
        :return:
        """
        if values is None:
            values = self.no_synonyms_list

        all_occurrences = [
            value for row in values for value in row
        ]

        return Counter(all_occurrences)

    def count_series(self, series: ExtendedSeries) -> Counter:
        self.get_raw_list_of_lower_strings_from_series(series=series)
        self.get_nouns_from_raw_list()
        self.remove_synonyms()
        return self.count_unique_occurrences()
