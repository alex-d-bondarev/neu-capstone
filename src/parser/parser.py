import re
from pathlib import Path

import pandas
from pandas import DataFrame


def parse():
    form_df = _get_data_frame_from_xlsx()
    form_df = _make_column_names_parsible(form_df)
    form_df = _filter_necessary_columns(form_df)
    _write_results_to_xlsx(form_df)


def _write_results_to_xlsx(form_df):
    target_path = str(_get_root_path() / 'results.xlsx')
    form_df.to_excel(excel_writer=target_path, sheet_name='raw_results')


def _get_data_frame_from_xlsx() -> DataFrame:
    form_path = str(next(_get_root_path().glob('Test Form.xlsx')))
    form_df = pandas.read_excel(io=form_path, sheet_name='Form1')
    return form_df


def _get_root_path():
    return Path(__file__).parent.parent.parent


def _make_column_names_parsible(form_df: DataFrame) -> DataFrame:
    unparsible_values = [
        '\(Select all that apply\)',
        '\(Leave empty if you prefer to be anonymous\)',
        '\(1 worst - 10 best\)',
    ]  # noqa

    new_column_names = form_df.columns
    for value in unparsible_values:
        new_column_names = new_column_names.str.replace(value, '')

    new_column_names = new_column_names. \
        str.strip().str.lower(). \
        str.replace(' ', '_'). \
        str.replace('-', '_'). \
        str.replace('?', '_')

    form_df.columns = new_column_names

    return form_df.rename(columns=lambda c: re.sub('[^A-Za-z0-9_]+', '', c))


def _filter_necessary_columns(form_df: DataFrame) -> DataFrame:
    necessary_columns = [
        'are_you_a_big_sky_franchise_team_client_or_were_you_in_the_past_',
        'did_you_complete_the_franchise_process_',
        'what_do_you_think_are_big_skys_franchise_team_strengths_',
        'what_do_you_think_are_big_skys_franchise_team_weaknesses_',
        'how_would_you_rate_your_overall_experience_with_big_sky_on_a_scale_of_1_10',
        'how_likely_are_you_to_recommend_big_sky_franchise_team_services_to_a_friend_or_colleague_',
        'do_you_have_a_franchise_or_plan_to_start_one_',
        'how_many_locations_do_you_currently_have_',
        'what_were_the_reasons_to_close_the_franchise_',
        'which_areas_you_need_help_with_',
        'would_you_like_to_participate_in_an_optional_interview_to_share_more_insights_',
        'please_share_your_email_so_that_we_may_contact_you_for_an_optional_interview',
        'business_name',
    ]

    return form_df.filter(items=necessary_columns, axis=1)


if __name__ == '__main__':
    parse()
