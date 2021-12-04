import constants
import pandas as pd

def fifa_file_opener(path, game_year):
    """
    Opens Fifa df for the given year
    """
    return pd.read_csv(f'{path}players_{game_year}.csv')