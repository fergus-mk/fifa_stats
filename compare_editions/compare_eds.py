import typer
import helpers
from constants import PATH


app = typer.Typer()


@app.command()
def comparer(player, stat, year1, year2):
    year1_stat = helpers.stat_selector(player, stat, PATH, year1)
    year2_stat = helpers.stat_selector(player, stat, PATH, year2)
    compared = helpers.stat_comparer(player, stat, year1_stat, year2_stat, year1, year2)
    print(compared)


if __name__ == '__main__':
    app()
