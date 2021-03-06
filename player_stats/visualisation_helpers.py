import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def comparison_players_df_maker(stat_value1, stat_value2, game_year1, game_year2):
    """
    Combines stat values with associated game year in a df

    Parameters
    ----------
    stat_value1
        The stat value in the more recent edition (int)
    stat_value2
        The stat value in the less recent edition (int)
    game_year1
        The more recent game year (int)
    game_year2
        The less recent game year (int)

    Returns
    -------
        A df of stat values and associated game year
    """
    data = [[stat_value1, game_year1], [stat_value2, game_year2]]
    df = pd.DataFrame(data, index=[0, 1], columns=["stat", "game_year"])
    return df


def create_comparison_barplot(
    player_name, stat, stat_value1, stat_value2, game_year1, game_year2
):
    """
    Creates a barplot showing a comparison of two players in a given stat

    Parameters
    ----------
    player_name
        The player being assessed (str)
    stat
        The stat being assessed (str)
    stat_value1
        The stat value in the more recent edition (int)
    stat_value2
        The stat value in the less recent edition (int)
    game_year1
        The more recent game year (int)
    game_year2
        The less recent game year (int)

    Returns
    -------
        A barplot showing stat of selected player for chosen game years
    """
    plot_data = comparison_players_df_maker(
        stat_value1, stat_value2, game_year1, game_year2
    )
    sns.set_style("darkgrid")
    sns.barplot(
        x=plot_data["game_year"], y=plot_data["stat"], data=plot_data
    ).set_title(
        f"{player_name} {stat} comparison Fifa {game_year1} and Fifa {game_year2}"
    )
    plt.xlabel("game year")
    plt.ylabel(stat)
    plt.show()
    return None


def create_best_players_barplot(players, stat, fifa_year):
    """
    Creates a barplot for the selected players and stat

    Parameters
    ----------
    players
        Players to have stats calculated (df)
    stat
        The stat that is getting shown (str)
    fifa_year
        The game year (str)

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
