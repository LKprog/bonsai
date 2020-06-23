# Classes
## Team Bonsai - programmeertheorie - Universiteit van Amsterdam

## Info
This folder contains all of the code for our classes.
you will find more information on each of the classes in it's own section.

## Table of contents
* [map.py](#map.py)
* [station.py](#station.py)
* [traject.py](#traject.py)

#map.py
This file contains a Map class that serves as a 'map' in which the Station and Traject classes exist.
##Methods
* load_stations - this method takes a csv-file as argument and creates a Station object for each of the stations in a csv file.
* load_connections - this method takes a csv-file as argument and creates connections between Stations for all of the connections in the file. 

#station.py
This file contains a Station class that loads the stations and its corresponding connections, it also tracks the stations unused connections.
##Methods
* connection - a method that appends the connection with name and duration to the Stations connections list.
* add_unused_connection - a method that appends the unused_connections of the station to the unused connections list
* __repr__ - this method ensures that the object is printed properly if it is in a list or dict.

#traject.py
This file contains a Traject class that represents a train route comprised of multiple connections between stations.
##Methods
* get_connection - a method that retrieves the possible connections for the Station which the Traject is currently on
* add_connection - a method that moves the Traject to the next station and adds that station to the list of stations it has passed
* __repr__ - this method ensures that the object is printed properly if it is in a list or dict.
