import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def parse_arg_adder(arg, type, help_string, arg_parser):
    """
    Adds arguments and help description to parser

    Parameters
    ----------
    arg
        The argument to be added to the parser (string)
    type
        The data type
    help_string
        The text for the help string
    arg_parser
        The required argument parser

    Returns
    -------
    The argument is added to the parser in the correct type with a help text description

    """
    return arg_parser.add_argument(arg, metavar=arg, type=type, help=help_string,)


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
    return pd.read_csv(f"{path}/players_{str(game_year)}.csv")


def top_players_in_stat(fifa_game, no_of_players, stat):
    """
    Returns the top x no players in a stat

    Parameters
    ----------
    fifa_game
        The fifa versions players (df)
    no_of_players
        The number of players to return (int)
    stat
        The stat to sort by (string)

    Returns
    -------
        pd df with x rows showing top x players in seleceted stat
    """
    top_players = fifa_game.sort_values(by=[stat], ascending=False).head(no_of_players)
    return top_players


def player_stat_barplot_creater(players, stat, fifa_year):
    """
    Creates a barplot for the selected players and stat

    Parameters
    ----------
    players
        Players to have stats calculated (df)
    stat
        The stat that is getting shown (string)
    fifa_year
        The game year (string)

    Returns
        A barplot showing stat for the selected players
    -------
    """
    sns.set_style("darkgrid")
    sns.barplot(x=players["short_name"], y=stat, data=players).set_title(
        f"Fifa {fifa_year} {stat} top players"
    )
    plt.xlabel("name")
    plt.show()
    return None