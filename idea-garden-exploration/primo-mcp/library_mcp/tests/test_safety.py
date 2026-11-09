from library_mcp.safety import clean_query, tidy


def test_clean_query_removes_commas_and_semicolons():
    assert clean_query("water, rights; colorado") == "water rights colorado"


def test_clean_query_limits_length():
    assert len(clean_query("a" * 500)) == 200


def test_tidy_shortens_long_text():
    assert len(tidy("x" * 1000)) == 300


def test_tidy_keeps_none():
    assert tidy(None) is None
