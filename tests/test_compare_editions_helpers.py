import pytest
from compare_editions.constants import PLAYER_DATA_PATH
import compare_editions.helpers as helpers
import compare_editions.constants as constants


fifa_20_stats = helpers.fifa_file_opener(
    constants.PLAYER_DATA_PATH, "20"
)  # Opening df of fifa 20 players


@pytest.mark.helper
def test_stat_selector():
    """
    Tests the function stat_selector
    """
    salah_overall_fifa20 = helpers.stat_selector(
        "M. Salah", "overall", PLAYER_DATA_PATH, 20
    )
    expected = 90
    assert salah_overall_fifa20 == expected


@pytest.mark.parametrize(
    "player, stat, stat_value1, stat_value2, year1, year2, result",
    [
        (
            "M. Salah",
            "overall",
            90,
            83,
            21,
            18,
            "M. Salah has improved overall by 7 points between fifa18 and fifa21",
        ),
        (
            "Isco",
            "passing",
            82,
            82,
            21,
            15,
            "Isco has stayed the same at passing between fifa15 and fifa21",
        ),
        (
            "Coutinho",
            "pace",
            72,
            81,
            21,
            19,
            "Coutinho has got worse at pace by 9 points between fifa19 and fifa21",
        ),
    ],
)
def test_stat_comparer(player, stat, stat_value1, stat_value2, year1, year2, result):
    """
    Tests the function stat_comparer
    """
    assert (
        helpers.stat_comparer(player, stat, stat_value1, stat_value2, year1, year2)
        == result
    )


@pytest.mark.helper
def test_top_players_in_stat():
    """
    Tests the function helpers.top_players_in_stat
    """
    best_passers_fifa_20 = helpers.top_players_stat(fifa_20_stats, "passing", 3)
    third_best_player = best_passers_fifa_20["short_name"].iloc[2]
    expected = "T. Kroos"
    assert third_best_player == expected
