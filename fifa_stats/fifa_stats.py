import pandas as pd
import helpers
import matplotlib.pyplot as plt
import seaborn as sns
from constants import PATH
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Creates a barplot showing top players for selected stat"
    )

    helpers.parse_arg_adder(
        "year",
        str,
        'Enter the game year. Options: "15","16","17","18","19","20","21"',
        parser,
    )  # Adding the command line input 'game year' to parser
    helpers.parse_arg_adder(
        "stat",
        str,
        'Enter the player stat. Options: "pace","shooting","passing","dribbling","defending","physic"',
        parser,
    )  # Adding the command line input 'stat' to parser
    helpers.parse_arg_adder(
        "no_of_players", int, "Enter the desired number of players", parser
    )  # Adding the command line input 'number of players' to parser

    args = parser.parse_args()
    year = args.year  # The selected fifa year
    stat = args.stat  # The desired stat
    no_of_players = args.no_of_players  # The number of players to display

    fifa_stats = helpers.fifa_file_opener(
        PATH, year
    )  # Opening df of fifa players for selected year

    top_players = helpers.top_players_in_stat(
        fifa_stats, no_of_players, stat
    )  # Selecting no_of_players top players for selected stat

    top_players_barplot = helpers.player_stat_barplot_creater(
        top_players, stat, year
    )  # Creating a barplot showing the top players for selected stat

    print(top_players_barplot)
