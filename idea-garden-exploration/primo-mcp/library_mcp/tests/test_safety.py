from library_mcp.safety import clean_query, tidy


def test_clean_query_removes_commas_and_semicolons():
    assert clean_query("water, rights; colorado") == "water rights colorado"


def test_clean_query_limits_length():
    assert len(clean_query("a" * 500)) == 200


def test_tidy_shortens_long_text():
    assert len(tidy("x" * 1000)) == 300


def test_tidy_keeps_none():
    assert tidy(None) is None


from library_mcp.models import DatabaseSearchResult
from library_mcp import az_sync

# def test_hostile_description_is_kept_but_labelled_as_data():
#     record = az_sync.to_database(SAMPLE[3])  # the Open Data Portal record
#     assert "IGNORE ALL PREVIOUS INSTRUCTIONS" in record.description
#     result = DatabaseSearchResult(query="x", returned=1, last_synced="now", databases=[record])
#     assert "not instructions" in result.notice