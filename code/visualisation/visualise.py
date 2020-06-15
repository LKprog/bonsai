import numpy as np
import csv
import sys
import random
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Label, LabelSet
from bokeh.tile_providers import CARTODBPOSITRON, get_provider
from ..classes.station import Station
from pyproj import Proj, transform

# prepare some data

def create_coordinates(long_arg,lat_arg):
    in_wgs = Proj('epsg:4326')
    out_mercator = Proj('epsg:3857')
    long, lat = long_arg, lat_arg
    mercator_x, mercator_y = transform(in_wgs, out_mercator, long, lat)
    return mercator_x, mercator_y


def visualise(map, trajects):

# Stations data
    csv_longitude = []
    csv_latitude = []
    stations = []
    for station in map.stations:
        stations.append(map.stations[station].name)
        new_coord = create_coordinates(float(map.stations[station].x), float(map.stations[station].y))
        csv_longitude.append(float(new_coord[1]))
        csv_latitude.append(float(new_coord[0]))
    longitude = np.array(csv_longitude)
    latitude = np.array(csv_latitude)
    N = 4000



    source = ColumnDataSource(data=dict(latitude=latitude, longitude=longitude, stations=stations))
    # output to static HTML file (with CDN resources)
    output_file("color_scatter.html", title="color_scatter.py example", mode="cdn")

    TOOLS = "pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
    tile_provider = get_provider(CARTODBPOSITRON)
    # create a new plot with the tools above, and explicit ranges
    p = figure(x_range=(400000, 500000), y_range=(6700000, 7000000),
           x_axis_type="mercator", y_axis_type="mercator")
    p.add_tile(tile_provider)
    font = 1


    colors = ['red', 'yellow', 'green', 'black', 'blue', 'orange']
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

    p.legend.location = 'top_left'
    p.legend.click_policy="hide"


    # add a circle renderer with vectorized colors and sizes
    p.circle(latitude, longitude)
    labels = LabelSet(x='latitude', y='longitude', text='stations', text_font_size='5pt', level='overlay',
                  x_offset=5, y_offset=5, source=source, render_mode='canvas')
    p.add_layout(labels)

    # show the results

    show(p)
