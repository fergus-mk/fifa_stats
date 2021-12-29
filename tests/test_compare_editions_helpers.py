import pytest
from compare_editions.constants import PATH
import compare_editions.helpers as helpers

@pytest.mark.helper
def test_stat_selector():
    """
    Tests the function stat_selector
    """
    salah_overall_fifa20 = helpers.stat_selector('M. Salah', 'overall', PATH, 20)
    expected = 90
    assert salah_overall_fifa20 == expected


@pytest.mark.parametrize(
    'player, stat, stat_value1, stat_value2, year1, year2, result',
    [
        (
            'M. Salah',
            'overall',
            90,
            83,
            21,
            18,
            'M. Salah has improved overall by 7 points between fifa18 and fifa21',
        ),
        (
            'Isco',
            'passing',
            82,
            82,
            21,
            15,
            'Isco has stayed the same at passing between fifa15 and fifa21',
        ),
        (
            'Coutinho',
            'pace',
            72,
            81,
            21,
            19,
            'Coutinho has got worse at pace by 9 points between fifa19 and fifa21',
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