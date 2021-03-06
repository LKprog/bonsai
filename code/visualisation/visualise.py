"""
 * main.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
 *
 * Code used to visualise the results from the algorithms
"""

import numpy as np
import csv
import sys
import random
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Label, LabelSet
from bokeh.tile_providers import CARTODBPOSITRON, get_provider
from ..classes.station import Station
from pyproj import Proj, transform

class Visual:
    """
    class that handlees all of the visualisation of the output-data
    """

    # converts longitude and latitude into mercator coordinates
    def create_coordinates(self, long_arg, lat_arg):
        """
        method that converts a given longitude and latitude into mercator coordinates
        """

        in_wgs = Proj('epsg:4326')
        out_mercator = Proj('epsg:3857')
        long, lat = long_arg, lat_arg
        mercator_x, mercator_y = transform(in_wgs, out_mercator, long, lat)
        return mercator_x, mercator_y


    def histogram(self, score_csv):
        """
        method that creates a histogram from a csv-file
        """

        # retrieve information from csv and store in a list
        with open(score_csv, 'r') as input_file:
            reader = csv.reader(input_file)

            data = []
            for row in reader:
                data.append(float(row[0]))

            # use matplotlib functionality for creating a histogram
            x = np.array(data)
            plt.hist(x, bins=100)
            plt.ylabel('Frequency')
            plt.xlabel('Score objectivefunction (quality)')
            plt.show()

    # creates a visual representation of the given map and the routes created by any of the algorithms
    def visualise(self, map, trajects, score_csv):
        """
        method that creates a visual representation of the given trajects
        """

        # load Station data and store the x-coordinates, y-coordinates and the station names in seperate lists.
        merc_y = []
        merc_x = []
        stations = []

        for station in map.stations:
            stations.append(map.stations[station].name)
            new_coord = self.create_coordinates(float(map.stations[station].x), float(map.stations[station].y))
            merc_y.append(float(new_coord[1]))
            merc_x.append(float(new_coord[0]))

        # convert x- and y-lists to numpy array so they can be used in bokeh
        longitude = np.array(merc_y)
        latitude = np.array(merc_x)
        N = 4000

        # save data in a variable for later use
        source = ColumnDataSource(data=dict(latitude=latitude, longitude=longitude, stations=stations))

        # output to html-file
        output_file("color_scatter.html", title="color_scatter.py example", mode="cdn")

        # retrieves a map which serves as a background for the plot
        tile_provider = get_provider(CARTODBPOSITRON)

        # create a new plot with the specified tools, and explicit ranges
        TOOLS = "pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
        p = figure(x_range=(400000, 500000), y_range=(6700000, 7000000),
            x_axis_type="mercator", y_axis_type="mercator")
        font = 1

        # adds the background to the plot
        p.add_tile(tile_provider)

        # define colors for the different routes
        colors = ['red', 'yellow', 'green', 'black', 'blue', 'orange', 'purple', 'pink', 'lawngreen', 'teal', 'saddlebrown', 'gold', 'magenta', 'silver']

        # creates a line, representing a traject for each of the given trajects
        for values in trajects.values():
            x_list = []
            y_list = []

            for value in values:

                if value in map.stations:
                    new_coord = self.create_coordinates(float(map.stations[value].x), float(map.stations[value].y))
                    x_list.append(float(new_coord[1]))
                    y_list.append(float(new_coord[0]))

            color = colors.pop(0)
            colors.append(color)
            p.line(y_list, x_list, line_width=2, color=color, legend_label=f"{values[0]} || {values[-1]}")

        # legend settings
        p.legend.location = 'top_left'
        p.legend.click_policy="hide"

        # add a circle for each of the stations in the given map
        p.circle(latitude, longitude)

        # adds name-labels to the circles
        labels = LabelSet(x='latitude', y='longitude', text='stations', text_font_size='5pt', level='glyph',
                    x_offset=5, y_offset=5, source=source, render_mode='canvas')

        p.add_layout(labels)

        # show the results
        show(p)

        # make histogram of the "..-scores.csv"
        self.histogram(score_csv)