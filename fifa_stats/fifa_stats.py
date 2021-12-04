import pandas as pd
# from helpers import fifa_file_opener, top_players_in_stat
import helpers

if __name__ == '__main__':


    path = 'C:/Users/fergu/PycharmProjects/player_data/'
    fifa_21_stats = helpers.fifa_file_opener(path, '21')

    top_defenders_21 = helpers.top_players_in_stat(fifa_21_stats, 5, 'defending')  # Calculating top 5 defenders in
                                                                                   # Fifa 21








