from src.common_helpers import make_text_pandas_header_compatible


def test_pandas_headers_renaming():
    question_before = 'What have been your biggest challenges in supporting your franchisees (select all that apply)?2 '
    question_after = 'What have been your biggest challenges in supporting your franchisees select all that apply2'

    assert make_text_pandas_header_compatible(question_before) == question_after
