from pandas import Series


class ExtendedSeries(Series):
    """Add extra methods to pandas Series class"""

    def make_lower_case_series_copy(self: Series) -> Series:
        """Self evident

        :param self:
        :return:
        """
        return self.copy().apply(
            lambda value: value.lower() if isinstance(value, str) else value)

    def mark_no_responses(self: Series) -> Series:
        """
        Return a new series where empty responses are marked as 'no response'.
        Returned values are all lower case.
        :param self:
        :param param:
        """
        return self.make_lower_case_series_copy(). \
            replace([' ', ''], 'no response')

    def trim_spaces(self: Series) -> Series:
        """
        Return a new series where spaces are trimmed.
        Returned values are all lower case.
        :param self:
        """
        return self.make_lower_case_series_copy().apply(
            lambda value: value.strip() if isinstance(value, str) else value)

    def replace_na_with_zeros(self: Series) -> Series:
        """
        Replace all None and N/A related values with 0 string.
        Returned values are all lower case.
        :param self:
        """
        return self.make_lower_case_series_copy().fillna('0'). \
            apply(
            lambda value: value.lower()
            if isinstance(value, str)
            else value). \
            replace(['na', 'n/a', 'n\\a'], '0')

    def replace_similar_answers(self: Series) -> Series:
        """
        Replace all None and N/A related values with 0 string.
        Returned values are all lower case.
        :param self:
        """
        similar_answers = [
            (['in the process', 'doing', 'in progress'], 'in process')
        ]

        result = self.make_lower_case_series_copy()
        for (to_replace, value) in similar_answers:
            result = result.replace(to_replace=to_replace, value=value)

        return result
