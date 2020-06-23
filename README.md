# RailNL
### Team Bonsai - programmeertheorie - Universiteit van Amsterdam

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
To approach the problem posed in the assignment, we developed several algorithms: Random, Random greedy, Depth first, Breadth first and Hill climber. The Depth first and Breadth first algorithms are constructive algorithms while the Hill climber is an interative algorithms and is used on top of another algorithm such as Random or Random greedy or one of the constructive algorithms. For full details on the algorithms and the heuristics see the [README](https://github.com/LKprog/bonsai/tree/master/code/algorithms) in the /code/algorithms folder.


# Installation

## Set up

We recommend using “Git Bash” on Windows or the “Terminal” on macOS or Linux to run the codes. Not using either of these may result in no visual output.

Use pip to install the required packages from requirement.txt:
```
pip3 install -r requirements.txt
```

and install extra for matplotlib:
```
python -m pip install -U matplotlib
```

## Usage
To execute the main script and run the case:
```
python3 main.py
```

The user will then automatically be prompted to choose between Holland (2 provinces) and the Netherlands. 
Then, the user can choose the algorithm they want to run and finally, how many iterations.

If you did not use “Git Bash” on Windows or the “Terminal” on macOS or Linux, the color_scatter.html doesn't open automatically. If this is the case, you should right click on the html file and select "Reveal in File Explorer". The computer should open an explorer screen where the html is located. When you double tap the html file, it will open in a new browser tab. The histogram of all the K scores will not appear either.

## Structure
In this repository there are several folders with different files that are imported by main.py. The following list describes the different folders and files:

    /code: contains all the code of the project
        /code/algorithms: contains all the algorithms used
        /code/classes: contains all three classes necessary for this case
        /code/visualisation: contains the code for the visualisation of the case
    /data: contains all the initial data files in csv format that are necessary to run the code
    /output: contains all the output files in csv format
        /code/Holland: contains all the solution and score files for each algorithm for Holland
        /code/Netherlands: contains all the solution and score files for each algorithm for the Netherlands

For an extensive description of the folders, see the README in each folder.

# Authors
* Willem Henkelman
* Lieke Kollen
* Daphne Westerdijk