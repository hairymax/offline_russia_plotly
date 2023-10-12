import pandas as pd
from map_figure import mapFigure, convert_crs
import plotly.graph_objects as go

russia_map = mapFigure()
vs = pd.read_csv('data/vertices.csv')
es = pd.read_csv('data/edges.csv')

vs['x'], vs['y'] = convert_crs(vs.lon, vs.lat)
df = es.set_index('v1').join(vs).set_index('v2').join(vs, lsuffix='_1', rsuffix='_2')

for index, row in df.iterrows():
    russia_map.add_trace(
        go.Scatter(
            x=[row['x_1'], row['x_2']],
            y=[row['y_1'], row['y_2']],
            line={'color': row['color']}
        ))

russia_map.add_trace(
    go.Scatter(
        x=vs.x,
        y=vs.y,
        text=vs.city,
        hoverinfo="text", showlegend=False, mode='markers',
        marker_color=vs.state
    ))
russia_map.write_html('html/index.html')
