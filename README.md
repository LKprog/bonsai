# RailNL
## Team Bonsai - programmeertheorie - Universiteit van Amsterdam

## Table of contents

* [Introduction](#Introduction)
* [Algorithms](#Algorithms)
* [Installation](#Installation)
* [Authors](#Authors)

# Introduction

## Case
The Netherlands has a large rail network and it was our task to increase the efficiency and quality of the network. More specifically, we focus on the intercity trains for North- and South holland and for the whole of the Netherlands. 

## Constraints
The assignment introduced some constraints and is therefore an example of a constrained optimization problem. For the two stages of the assignment, the constraints are as follows:
* North- and South Holland: a maximum of 7 routes (refered to as "traject" in the code) and each route can have a maximum duration of 120 minutes
* Netherlands: a maximum of 20 routes (refered to as "traject" in the code) and each route can have a maximum duration of 180 minutes

## Objective function
Optimization was according to an objective function provided by RailNL:  

K = p * 10000 - (T * 100 + Min)

Where p stands for the fraction of connections used, T equals the amount of routes used and Min was the total duration of the rail network in minutes. Hence, the quality is the highest when the lowest possible number of routes is used while using the shortest connections to construct the routes.


# Algorithms
To approach the problem posed in the assignment, we developed several algorithms:
* Random - algorithm that keeps chosing a random connection from the list of connections until the maximum duration of a route is reached and/or all connections are used
* Random-greedy - algorithm that keeps chosing either the shortest or longest connection until the maximum duration of a route is reached and/or all connections are used
* Depth first - constructive algorithm that searches a tree data structure. It starts at the root node and first explores a full branch before going back one step and continue with the next branch. 
* Breadth first - constructive algorithm that searches a tree data structure. It starts at the root node and first explores all the nodes in the first depth before continuing to next depth.
* Hill climber - iterative algorithm that searches for a better solution by making changes to an already exisiting solution.

## Heuristics
....

# Installation

## Set up
Use pip to install the required packages from requirement.txt
```
pip3 install -r requirements.txt
```

## Usage
To execute the main script and run the case, run
```
python3 main.py
```

The user will be prompted to choose between Holland (2 provinces) and the Netherlands. 
Then, the user can choose the algorithm they want to run and finally, how many iterations.

## Structure
In this repository there are several folders with different files that are imported by main.py. The following list describes the different folders and files:

    /code: contains all the code of the project
        /code/algorithms: contains all the algorithms used
        /code/classes: contains all three classes necessary for this case
        /code/visualisation: contains the code for the visualisation of the case
    /data: contains all the initial data files in csv format that are necessary to run the code
    .....

# Authors
* Willem Henkelman
* Lieke Kollen
* Daphne Westerdijk