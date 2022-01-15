import typer
import helpers
import visualisation_helpers as vis_helpers
from constants import PLAYER_DATA_PATH, PATH


app = typer.Typer()


@app.command()
def comparer(player, stat, year1, year2):
    year1_stat = helpers.stat_selector(player, stat, PLAYER_DATA_PATH, year1)
    year2_stat = helpers.stat_selector(player, stat, PLAYER_DATA_PATH, year2)
    compared = helpers.stat_comparer(player, stat, year1_stat, year2_stat, year1, year2)
    vis_helpers.create_comparison_barplot(player, stat, year1_stat, year2_stat, year1, year2)
    print(compared)


@app.command()
def best(stat, fifa_year, no_of_players):
    fifa_df = helpers.fifa_file_opener(PLAYER_DATA_PATH, fifa_year)
    top_players_df = helpers.top_players_stat(fifa_df, stat, no_of_players)
    vis_helpers.create_best_players_barplot(top_players_df, stat, fifa_year)


if __name__ == '__main__':
    app()
