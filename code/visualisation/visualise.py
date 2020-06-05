import numpy as np
import csv
import sys
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Label, LabelSet

# prepare some data

with open(sys.argv[1], 'r') as input_file:
    reader = csv.DictReader(input_file)
    csv_x = []
    csv_y = []
    stations = []
    for row in reader:
        stations.append(row['station'])
        csv_x.append(float(row['x']))
        csv_y.append(float(row['y']))
N = 4000

x = np.array(csv_x)
y = np.array(csv_y)

source = ColumnDataSource(data=dict(x=x, y=y, stations=stations))
# output to static HTML file (with CDN resources)
output_file("color_scatter.html", title="color_scatter.py example", mode="cdn")

TOOLS = "wheel_zoom,box_zoom,reset,box_select,lasso_select"

# create a new plot with the tools above, and explicit ranges
p = figure(tools=TOOLS, x_range=(51.5, 53.5), y_range=(4.2, 5.2))
font = 1
# add a circle renderer with vectorized colors and sizes
p.circle(x, y)
labels = LabelSet(x='x', y='y', text='stations', text_font_size='7pt', level='glyph',
              x_offset=5, y_offset=5, source=source, render_mode='canvas')
p.add_layout(labels)

# show the results

show(p)
