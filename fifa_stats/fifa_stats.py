import pandas as pd
import helpers
import matplotlib.pyplot as plt
import seaborn as sns
from constants import PATH
import argparse

if __name__ == "__main__":

    fifa_21_stats = helpers.fifa_file_opener(
        PATH, "21"
    )  # Opening df of fifa 21 players

    top_defenders_21 = helpers.top_players_in_stat(
        fifa_21_stats, 5, "defending"
    )  # Calculating top 5 defenders in Fifa 21

    top_defenders_21_barplot = helpers.player_stat_barplot_creater(
        top_defenders_21, "defending", "21"
    )  # Creating a barplot showing the top 5 defenders
    print(top_defenders_21_barplot)
