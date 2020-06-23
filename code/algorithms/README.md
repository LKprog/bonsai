# Algorithms
## Team Bonsai - programmeertheorie - Universiteit van Amsterdam

## Info
This folder contains all of the code for our algorithms.
You will find more information on each of the algorithms in it's own section.

## Table of contents

* [breadthfirst.py](#breadthfirst.py)
* [depthfirst.py](#depthfirst.py)
* [hillclimber.py](#hillclimber.py)
* [random_greedy.py](#random_greedy.py)
* [randomize.py](#randomize.py)

# breadthfirst.py
This is a constructive algorithm that searches a tree data structure. It starts at the root node and first explores all the nodes in the first depth before continuing to next depth.

## Heuristics
The following heuristics were used for this algorithm:
1. The first station of the route is randomly selected
2. From all the solutions per tree, the solutions with the most connections are selected
3. From those solutions, the solution with the shortest duration is returned to the user as best found result

## Methods
* get_next_state - method gets the next item from the stack
* get_start_stations - method sets a random station to start the new traject from
* check_solution - method that checks the solution and returns the traject with the most connections used and lowest duration
* calculate_p - method that calculates the fraction of unused connections
* calculate_min - method that calculates the total duration of all routes together
* objectivefunction - method to determine the quality (K) of the set of train routes, where P is the fraction of used connections, T is number of routes used and Min is the total duration of all routes
* run - method that runs the breadth first algorithm

# depthfirst.py
This is a constructive algorithm that searches a tree data structure. It starts at the root node and first explores a full branch before going back one step and continue with the next branch.

## Heuristics
The following heuristics were used for this algorithm:
1. The first station of the route is randomly selected
2. From all the solutions per tree, the solutions with the most connections are selected
3. From those solutions, the solution with the shortest duration is returned to the user as best found result

## Methods
* get_next_state - this method gets the next item from the stack
* get_start_stations - this method sets a random station to start the new traject from
* check_solution - method that checks the solution and returns the traject with the most connections used and lowest duration
* calculate_p - method that calculates the fraction of unused connections
* calculate_min - method that calculates the total duration of all routes together
* objectivefunction - method to determine the quality (K) of the set of train routes, where P is the fraction of used connections, T is number of routes used and Min is the total duration of all routes
* run - method that runs the depth first algorithm

# hillclimber.py
This is an iterative algorithm that searches for a better solution by making changes to an already exisiting solution.

## Heuristics
1. The first and last connection of the route is randomly replaced with a different connection
2. Only newly made routes that have a higher K than before are saved

## Methods
* get_connections_secondtolast - method that returns the connections from the second to last station in the traject
* get_connections_second - method that returns the connections from the second to last station in the traject
* remove_last - method that removes the time of the connection which will be replaced
* remove_first - method that removes the time of the connection which will be replaced
* add_connection_last - method that adds the connection at the end of the traject
* add_connection_first - method that adds the connection at the start of the traject
* mutate_last_connection - method that mutates the last connection in a random traject
* mutate_first_connection - method that mutates the first connection in a random traject
* check_small_traject - method that deletes trajects of only 1 connection
* objectivefunction - method to determine the quality (K) of the set of train routes, where P is the fraction of used connections, T is number of routes used and Min is the total duration of all routes
* check_solution - method that checks if the new score is better than the previous score
* run - method that runs the hillclimber algorithm {iterations} amount of times

# random_greedy.py
This is an algorithm that keeps chosing either the shortest or longest connection until the maximum duration of a route is reached and/or all connections are used.

## Heuristics
1. The first station of the route is randomly selected from a list that contains the stations that still have unused connections
2. The algorithm always favors unused connections over used connections if possible
3. Depending on whether min or max is selected, algorithm will pick the connection with the shortest or longest duration respectivel

## Methods
* max_value - method that returns the connection with the longest duration
* min_value - method that returns the connection with the shortest duration
* run - method that runs the random greedy algorithm a "num_repeats" amount of times

# randomize.py
This is an algorithm that keeps chosing a random connection from the list of connections until the maximum duration of a route is reached and/or all connections are used.

## Heuristics
1. The first station of the route is randomly selected from a list that contains the stations that still have unused connections
2. The algorithm always favors unused connections over used connections if possible
3. If there are no unused connections of which the duration falls within the remaining timeframe, the route is ended and saved

## Methods
* reset_variables - method to reset all the list and variables in order to run a new set of routes
* unused_connection_in_duration - method that checks whether a connection can be appended to the traject without having the duration get higher than the limit
* remove_unused_connection - method that updates the list of unused connections by removing used connections from the list of the relevant station
* end_traject - method that appends the complete traject to the full_traject list
* objectivefunction - method to determine the quality (K) of the set of train routes
* best_score - method that saves the highest quality score and it's corresponding train routes and the duration
* run - method that runs the random algorithm an "num_repeats" amount of times

