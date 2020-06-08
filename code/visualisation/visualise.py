import numpy as np
import csv
import sys
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Label, LabelSet

# prepare some data

with open('StationsHolland.csv', 'r') as input_file:
    reader = csv.DictReader(input_file)
    csv_longitude = []
    csv_latitude = []
    stations = []
    for row in reader:
        stations.append(row['station'])
        csv_longitude.append(float(row['x']))
        csv_latitude.append(float(row['y']))
N = 4000

longitude = np.array(csv_longitude)
latitude = np.array(csv_latitude)


source = ColumnDataSource(data=dict(latitude=latitude, longitude=longitude, stations=stations))
# output to static HTML file (with CDN resources)
output_file("color_scatter.html", title="color_scatter.py example", mode="cdn")

TOOLS = "wheel_zoom,box_zoom,reset,box_select,lasso_select"

# create a new plot with the tools above, and explicit ranges
p = figure(tools=TOOLS, y_range=(51.5, 53.5), x_range=(4.2, 5.2))
font = 1
# add a circle renderer with vectorized colors and sizes
p.circle(latitude, longitude)
labels = LabelSet(x='latitude', y='longitude', text='stations', text_font_size='7pt', level='glyph',
              x_offset=5, y_offset=5, source=source, render_mode='canvas')
p.add_layout(labels)

# show the results

show(p)
