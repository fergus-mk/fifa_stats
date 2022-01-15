# Overview

---
This project generates insights based on stats from 
the Fifa series of games.

## Use

--- 
The project relies on packages contained in the 
stats_env.yml file. Users should use the command line 
command to initiate the environment:

`conda env create -f stats_env.yml`

To use the project enter the folder player_stats and
call functions directly from  player_stats.py 
directly from the command line. Currently there are 
two options:

`python .\player_stats.py comparer 'M. Salah', 
'overall',  21, 19`

Demonstrates use of the 'comparer' function which 
compares an individual player at a selected stats
between different editions of the game. It displays
this via a print statement and the creation of a 
barplot. In this example the player 'M. Salah' is
compared between Fifa 21 and Fifa 19.

`python .\Player_stats.py best 'defending', 18, 3`

Demonstrates use of the 'best' function which 
produces a barplot showing the best players at 
the selected stat for a given game year. In this
example the top players at defending in Fifa 18 
are shown. The final argument, '3' selects how 
many players to show.