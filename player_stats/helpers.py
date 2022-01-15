import pandas as pd


def fifa_file_opener(path, game_year):
    """
    Opens fifa df for the given year

    Parameters
    ----------
    path
        The path to fifa player stats (str)
    game_year
        The fifa version (str)

    Returns
    -------
        pd dataframe of fifa version
    """
    return pd.read_csv(f"{path}/players_{str(game_year)}.csv")


def stat_selector(player, stat, in_path, year):
    """
    Selects stat for player in game year selected

    Parameters
    ----------
    player
        The player being assessed (str)
    stat
        The stat being assessed (str)
    in_path
        The path to the folder containing player data (str)
    year
        The year of game to look at (int)

    Returns
    -------
    stat_selected
        A number indicating the selected stat value (int)
    """
    df = fifa_file_opener(in_path, year)
    player_row = df.loc[df["short_name"] == player]
    stat_selected = int(player_row[stat])
    return stat_selected


def stat_comparer(player, stat, stat_value1, stat_value2, year1, year2):
    """
    Compares how a given players selected stat has changed between game editions

    Parameters
    ----------
    player
        The player being assessed (str)
    stat
        The stat being assessed (str)
    stat_value1
        The stat value in the more recent edition (int)
    stat_value2
        The stat value in the less recent edition (int)
    year1
        The more recent game year (int)
    year2
        The less recent game year (int)

    Returns
    -------
        A string describing if the player has improved, stayed the same or got worse
    """
    diff = stat_value1 - stat_value2
    if diff > 0:
        return f"{player} has improved {stat} by {str(diff)} points between fifa{year2} and fifa{year1}"
    elif diff == 0:
        return f"{player} has stayed the same at {stat} between fifa{year2} and fifa{year1}"
    elif diff < 0:
        return f"{player} has got worse at {stat} by {str(diff*-1)} points between fifa{year2} and fifa{year1}"
    else:
        return f"{stat} is not in both game verisons"


def top_players_stat(fifa_df, stat, no_of_players):
    """
    Returns the top x no players in a stat

    Parameters
    ----------
    fifa_df
        The fifa versions players (df)
    no_of_players
        The number of players to return (int)
    stat
        The stat to sort by (str)

    Returns
    -------
        pd df with x rows showing top x players in selected stat
    """
    n_players = int(no_of_players)
    top_players = fifa_df.sort_values(by=[stat], ascending=False).head(n_players)
    return top_players
