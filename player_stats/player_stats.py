import typer
import helpers
import visualisation_helpers as vis_helpers
from constants import PLAYER_DATA_PATH


app = typer.Typer()  # Creating a typer.Typer() app to call subcommands from


@app.command()
def comparer(player, stat, year1, year2):
    """
    Takes command line input, compares a player between game editions showing print statement and barplot

    Parameters
    ----------
    player
        The player being assessed (str)
    stat
        The stat being assessed (str)
    year1
        The more recent game year (int)
    year2
        The less recent game year (int)

    Returns
    -------
        Prints a statement describing if player has improved and returns a barplot showing change in stat for player
        between game editions
    """
    year1_stat = helpers.stat_selector(player, stat, PLAYER_DATA_PATH, year1)
    year2_stat = helpers.stat_selector(player, stat, PLAYER_DATA_PATH, year2)
    compared = helpers.stat_comparer(player, stat, year1_stat, year2_stat, year1, year2)
    vis_helpers.create_comparison_barplot(
        player, stat, year1_stat, year2_stat, year1, year2
    )
    print(compared)


@app.command()
def best(stat, fifa_year, no_of_players):
    """
    Takes command line input and returns a barplot showing top players for selected stat

    Parameters
    ----------
    stat
        The stat being assessed (str)
    fifa_year
        The fifa year being assessed (int)
    no_of_players
        The number of players to show (int)

    Returns
    -------
        A barplot showing the top n no_of_players for stat
    """
    fifa_df = helpers.fifa_file_opener(PLAYER_DATA_PATH, fifa_year)
    top_players_df = helpers.top_players_stat(fifa_df, stat, no_of_players)
    vis_helpers.create_best_players_barplot(top_players_df, stat, fifa_year)


if __name__ == "__main__":
    app()
