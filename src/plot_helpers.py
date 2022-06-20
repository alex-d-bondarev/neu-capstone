from typing import List

import numpy
import pandas
from matplotlib import pyplot
from matplotlib.axes import Axes
from pandas import Series

from src.common_data import PLOT_WIDTH, SPACE_BETWEEN_PLOTS, DOUBLE_PLOT_HEIGHT
from src.common_helpers import get_counter_with_top, split_out_other_answers
from src.extended_pandas_series import ExtendedSeries
from src.nlp_helpers import NlpHelper


def plot_bar_chart(series: Series, ax: Axes = None) -> None:
    """
    Show a bar chart for given data series.
    Values such as NaN, None, etc. are converted to 0.
    Data values are lazy sorted
    Data values are converted to percentages.
    x labels are rotated 15%
    """
    if series.empty:
        print("No Data for bar chart")
    else:
        ExtendedSeries(series).prepare_data_for_plotting().plot(
            ylabel="percentage",
            kind="bar",
            rot=15,
            ax=ax,
        )


def plot_1_10_hist_chart(series: Series) -> None:
    """
    Print mean value and show histogram chart for given data series.
    Always show x axis 1 to 10
    """
    print(f'Mean value is {round(series.mean(), 1)}')

    series.plot(
        kind='hist',
        xticks=range(1, 11)
    )


def plot_text_answer(series: Series, top: int, ax: Axes = None) -> None:
    """Self evident"""
    series_counter = NlpHelper().count_series(series=ExtendedSeries(series))

    if series_counter.total() > 0:
        display_counter = get_counter_with_top(series_counter, top)

        # Create a plot
        # Credit to https://stackoverflow.com/a/22222738/8661297
        keys = display_counter.keys()
        y_pos = numpy.arange(len(keys))
        x_values = display_counter.values()
        max_value = display_counter.most_common(1)[0][1]

        if ax:
            ax.barh(y_pos, x_values)
        else:
            pyplot.barh(y_pos, x_values)

        pyplot.yticks(y_pos, keys)
        pyplot.xticks(range(0, (max_value + 1)))


# TODO: use split_out_other_answers
def plot_multichoice_with_other(series: Series, main_values: List, top: int) -> None:
    """
    Show 2 plots if enough data
    First plot is plot_bar_chart() for expected values
    Second plot is plot_text_answer() for "Other" values
    """
    temp_s = series.str.split(';').apply(pandas.Series).stack()
    temp_s.index = temp_s.index.droplevel(-1)

    main_series, other_series = split_out_other_answers(series, main_values)

    fig, axs = pyplot.subplots(2, figsize=(PLOT_WIDTH, DOUBLE_PLOT_HEIGHT))
    pyplot.subplots_adjust(hspace=SPACE_BETWEEN_PLOTS)

    plot_bar_chart(main_series, ax=axs[0])
    plot_text_answer(other_series, top=top, ax=axs[1])
