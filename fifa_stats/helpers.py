import constants
import pandas as pd

def fifa_file_opener(path, game_year):
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
    return pd.read_csv(f'{path}players_{str(game_year)}.csv')

def top_players_in_stat(fifa_game, no_of_players, stat):
    """
    Returns the top x no players in a stat

    Parameters
    ----------
    fifa_game
        The fifa versions players (pd dataframe)
    no_of_players
        The number of players to return (int)
    stat
        The stat to sort by (string)

    Returns
    -------
        pd dataframe with x rows showing top x players in seleceted stat
    """
    top_players = fifa_game.sort_values(by=[stat], ascending=False).head(no_of_players)
    return top_players