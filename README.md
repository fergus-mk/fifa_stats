# Overview

---
This project generates insights based on stats from 
the Fifa series of games. It shows the players with 
the highest rating of a selected stat from a given
edition of the Fifa game

## Use

--- 
The project relies on packages contained in the 
stats_env.yml file. Users should use the command line 
command to initiate the environment:

`conda env create -f stats_env.yml`

To use the project enter the required year, stat and number of players
when calling the file in a python terminal e.g.,

`python fifa_stats.py 21 defending 3`

Would return a bar chart showing  the defending stat of the 3 best defenders 
in Fifa 21