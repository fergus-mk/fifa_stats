import pandas as pd


def fifa_file_opener(PATH, game_year):
    """
    Opens fifa df for the given year

    Parameters
    ----------
    game_year
        The fifa version (string)
    path
        The path to fifa player stats (string)

    Returns
    -------
        pd dataframe of fifa version
    """
    return pd.read_csv(f"{PATH}/players_{str(game_year)}.csv")


def stat_selector(player, stat, in_path, year):
    """
    Selects stat for player in game year selected
    """
    df = fifa_file_opener(in_path, year)
    player_row = df.loc[df['short_name'] == player]
    stat_selected = int(player_row[stat])
    return stat_selected


def stat_comparer(player, stat, stat_value1, stat_value2, year1, year2):
    """
    Compares how a given players selected stat has changed between game editions
    """
    diff = stat_value1 - stat_value2
    if diff > 0:
        # add return here instead of print
        return f'{player} has improved {stat} by {str(diff)} points between fifa{year2} and fifa{year1}'
    elif diff == 0:
        return f'{player} has stayed the same at {stat} between fifa{year2} and fifa{year1}'
    elif diff < 0:
        return f'{player} has got worse at {stat} by {str(diff*-1)} points between fifa{year2} and fifa{year1}'
    else:
        return f'{stat} is not in both game verisons'
