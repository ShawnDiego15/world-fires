import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get longitude, latitude, brightness.
    lats, lons, brights = [], [], []
    for row in reader:
        lat = float(row[0])
        lon = float(row[1])
        bright = float(row[2])
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

# Map the fires.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'color': brights,
        'colorscale': 'Hot',
        'colorbar': {'title': 'Brightness'}
    },
}]
my_layout = Layout(title="World Fire Data")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='output/world_fires.html')
