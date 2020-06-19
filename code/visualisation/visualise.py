"""
 * random.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
"""

import numpy as np
import csv
import sys
import random
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Label, LabelSet
from bokeh.tile_providers import CARTODBPOSITRON, get_provider
from bokeh.charts import Histogram
from ..classes.station import Station
from pyproj import Proj, transform

# converts longitude and latitude into mercator coordinates
def create_coordinates(long_arg,lat_arg):
    """
    method that converts a given longitude and latitude into mercator coordinates
    """
    in_wgs = Proj('epsg:4326')
    out_mercator = Proj('epsg:3857')
    long, lat = long_arg, lat_arg
    mercator_x, mercator_y = transform(in_wgs, out_mercator, long, lat)
    return mercator_x, mercator_y

# creates a visual representation of the given map and the routes created by any of the algorithms
def visualise(map, trajects):
    """
    method that creates a visual representation of the given trajects
    """
# load Station data
    merc_y = []
    merc_x = []
    stations = []
    for station in map.stations:
        stations.append(map.stations[station].name)
        new_coord = create_coordinates(float(map.stations[station].x), float(map.stations[station].y))
        merc_y.append(float(new_coord[1]))
        merc_x.append(float(new_coord[0]))
    longitude = np.array(merc_y)
    latitude = np.array(merc_x)
    N = 4000

    # save data in a variable for later use
    source = ColumnDataSource(data=dict(latitude=latitude, longitude=longitude, stations=stations))

    # output to html-file
    output_file("color_scatter.html", title="color_scatter.py example", mode="cdn")

    # retrieves a map which serves as a background for the plot.
    tile_provider = get_provider(CARTODBPOSITRON)

    # create a new plot with the specified tools, and explicit ranges
    TOOLS = "pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
    p = figure(x_range=(400000, 500000), y_range=(6700000, 7000000),
           x_axis_type="mercator", y_axis_type="mercator")
    font = 1

    # adds the background to the plot
    p.add_tile(tile_provider)

    # creates a line, representing a traject for each of the given trajects
    colors = ['red', 'yellow', 'green', 'black', 'blue', 'orange', 'purple', 'pink', 'lawngreen', 'teal', 'saddlebrown', 'gold', 'magenta', 'silver']
    for values in trajects.values():
        x_list = []
        y_list = []
        for item in values:
            if item in map.stations:
                new_coord = create_coordinates(float(map.stations[item].x), float(map.stations[item].y))
                x_list.append(float(new_coord[1]))
                y_list.append(float(new_coord[0]))
        color = colors.pop(0)
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

    df = pd.read_csv()

    # show the results
    show(p)
