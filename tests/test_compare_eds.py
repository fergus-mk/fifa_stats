import pytest
import compare_editions.compare_eds as compare_eds


@pytest.mark.paremeterize(
    'player, stat, year1, year2, result',
    [
        (
            'T. Kroos',
            'attacking_crossing',
            20,
            16,
            'T. Kroos has improved attacking_crossing by 3 points between fifa16 and fifa20'
        ),
        (
            'T. Courtois',
            'gk_diving',
            21,
            20,
            'M. Neuer has stayed the same at gk_diving between fifa21 and fifa20'
        ),
        (
            'P. Pogba',
            'overall',
            21,
            19,
            'P. Pogba has got worse at overall by 2 points between fifa19 and fifa21')
    ]
    )


def test_comparer(player, stat, year1, year2, result):  # Why doesn't this work, is it because of where the function is called in compare_eds.py?
    """
    Tests the function comparer
    """
    assert (
        compare_eds.comparer(player, stat, year1, year2)
        == result
    )