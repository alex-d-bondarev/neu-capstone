from matplotlib.axes import Axes
from pandas import Series

from src.common_data import NO_RESPONSE


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
        Return a new series where empty responses are marked as NO_RESPONSE.
        Returned values are all lower case.
        :param self:
        :param param:
        """
        return ExtendedSeries(
            self.make_lower_case_series_copy().
            replace([' ', ''], NO_RESPONSE)
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

    def plot_bar_chart(self: 'ExtendedSeries', ax: Axes = None) -> None:
        """
            Show a bar chart for given data series.
            Values such as NaN, None, etc. are converted to 0.
            Data values are lazy sorted
            Data values are converted to percentages.
            x labels are rotated 15%
            """
        if self.empty:
            print("No Data for bar chart")
        else:
            self.prepare_data_for_plotting().plot(
                ylabel="percentage",
                kind="bar",
                rot=15,
                ax=ax,
            )

    def plot_1_10_hist_chart(self: 'ExtendedSeries') -> None:
        """
        Print mean value and show histogram chart for given data series.
        Always show x axis 1 to 10
        """
        print(f'Mean value is {round(self.mean(), 1)}')

        self.plot(
            kind='hist',
            xticks=range(1, 11)
        )

    def merge_to_string(self: 'ExtendedSeries') -> str:
        """Self evident"""
        values = self.values.tolist()
        string_values = [str(value) for value in values]  # noqa
        return ' '.join(string_values)
