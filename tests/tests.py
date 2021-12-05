import pytest
import fifa_stats.helpers as helpers
import fifa_stats.fifa_stats as fifa_stats
from fifa_stats.constants import PATH
from pandas.testing import assert_series_equal



@pytest.mark.helper
def test_fifa_file_opener():
    """
    Tests the function fifa_file_opener
    """
    assert_series_equal()