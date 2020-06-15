import numpy as np
import csv
import sys
import random
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Label, LabelSet
from ..classes.station import Station

# prepare some data
def visualise_all(map, trajects):

# Stations data
    csv_longitude = []
    csv_latitude = []
    stations = []
    for station in map.stations:
        stations.append(map.stations[station].name)
        csv_longitude.append(float(map.stations[station].x))
        csv_latitude.append(float(map.stations[station].y))
    longitude = np.array(csv_longitude)
    latitude = np.array(csv_latitude)
    N = 4000



    source = ColumnDataSource(data=dict(latitude=latitude, longitude=longitude, stations=stations))
    # output to static HTML file (with CDN resources)
    output_file("color_scatter.html", title="color_scatter.py example", mode="cdn")

    TOOLS = "pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"

    # create a new plot with the tools above, and explicit ranges
    p = figure(tools=TOOLS, y_range=(51.5, 53.5), x_range=(4.1, 5.3))
    font = 1


    colors = ['red', 'yellow', 'green', 'black', 'blue', 'orange']
    for values in trajects.values():
        x_list = []
        y_list = []
        for item in values:
            if item in map.stations:
                x_list.append(float(map.stations[item].x))
                y_list.append(float(map.stations[item].y))
        color = colors.pop(0)
        p.line(y_list, x_list, line_width=2, color=color)




    # add a circle renderer with vectorized colors and sizes
    p.circle(latitude, longitude)
    labels = LabelSet(x='latitude', y='longitude', text='stations', text_font_size='7pt', level='glyph',
                  x_offset=5, y_offset=5, source=source, render_mode='canvas')
    p.add_layout(labels)

    # show the results

    show(p)
