import pandas as pd
import helpers

if __name__ == '__main__':


    path = 'C:/Users/fergu/PycharmProjects/player_data/'
    fifa_20_stats = helpers.fifa_file_opener(path, '20')
    fifa_21_stats = helpers.fifa_file_opener(path, '21')

    print(fifa_20_stats.head())






