import pytest
import fifa_stats.helpers as helpers
import fifa_stats.fifa_stats as fifa_stats
from pandas.testing import assert_series_equal

fifa_15_df = helpers.fifa_file_opener(fifa_stats.path, '15')

@pytest.mark.helper
def test_fifa_file_opener():
    """
    Tests the function fifa_file_opener
    """
    assert_series_equal()