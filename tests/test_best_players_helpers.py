import pytest
import best_players.helpers as helpers
import best_players.constants as constants

fifa_20_stats = helpers.fifa_file_opener(
    constants.PATH, "20"
)  # Opening df of fifa 20 players


@pytest.mark.helper
def test_top_players_in_stat():
    """
    Tests the function helpers.top_players_in_stat
    """
    best_passers_fifa_20 = helpers.top_players_in_stat(fifa_20_stats, 3, 'passing')
    third_best_player = best_passers_fifa_20['short_name'].iloc[2]
    expected = 'T. Kroos'
    assert third_best_player == expected
