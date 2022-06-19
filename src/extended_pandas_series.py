from pandas import Series


class ExtendedSeries(Series):
    """Add extra methods to pandas Series class"""

    def make_lower_case_series_copy(self: 'ExtendedSeries') -> 'ExtendedSeries':
        """Self evident

        :param self:
        :return:
        """
        return ExtendedSeries(
            self.copy().
            apply(
                lambda value: value.lower()
                if isinstance(value, str)
                else value
            )
        )

    def mark_no_responses(self: 'ExtendedSeries') -> 'ExtendedSeries':
        """
        Return a new series where empty responses are marked as 'no response'.
        Returned values are all lower case.
        :param self:
        :param param:
        """
        return ExtendedSeries(
            self.make_lower_case_series_copy().
            replace([' ', ''], 'no response')
        )

    def trim_spaces(self: 'ExtendedSeries') -> 'ExtendedSeries':
        """
        Return a new series where spaces are trimmed.
        Returned values are all lower case.
        :param self:
        """
        return ExtendedSeries(
            self.make_lower_case_series_copy().
            apply(
                lambda value: value.strip()
                if isinstance(value, str)
                else value
            )
        )

    def group_na_values(self: 'ExtendedSeries') -> 'ExtendedSeries':
        """
        Replace all None and N/A related values with 0 string.
        Returned values are all lower case.
        :param self:
        """
        common_na = 'n/a'
        return ExtendedSeries(
            self.make_lower_case_series_copy().fillna(common_na).
            apply(
                lambda value: value.lower()
                if isinstance(value, str)
                else value
            ).
            replace(['na', 'n/a', 'n\\a'], common_na)
        )

    def replace_similar_answers(self: 'ExtendedSeries') -> 'ExtendedSeries':
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

        return ExtendedSeries(result)

    def prepare_data_for_plotting(self: 'ExtendedSeries') -> 'ExtendedSeries':
        """
        Return a new series with value counts.
        Similar values should be counted as same values.
        Data values are lazy sorted.
        Data values are converted to percentages.
        """
        return ExtendedSeries(self.trim_spaces().
                              mark_no_responses().
                              group_na_values().
                              replace_similar_answers().
                              sort_values().
                              value_counts(normalize=True).
                              mul(100).
                              round(1))
