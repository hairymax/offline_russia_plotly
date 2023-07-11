import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


fo_list = list(regions['federal_district'].unique())

class mapFigure(go.Figure):
    """ Шаблон фигуры для рисования поверх карты России
    """
    def __init__(self, 
        data=None, layout=None, frames=None, skip_invalid=False, # дефолтные параметры фигуры plotly
        **kwargs # аргументы (см. документацию к plotly.graph_objects.Figure())
    ):
        # создаём plotlу фигуру с дефолтными параметрами
        super().__init__(data, layout, frames, skip_invalid, **kwargs)
        
        # палитра цветов
        colors = px.colors.qualitative.Plotly

        # прорисовка регионов
        for i, r in regions.iterrows():
            self.add_trace(go.Scatter(x=r.x, y=r.y,
                                      name=r.region,
                                      text=f'<b>{r.region}</b><br>{r.federal_district}<br>Население: {r.population}',
                                      hoverinfo="text",
                                      line_color='grey',
                                      fill='toself',
                                      line_width=2,
                                      fillcolor=colors[fo_list.index(r.federal_district)],
                                      showlegend=False
            ))
        
        # не отображать оси, уравнять масштаб по осям
        self.update_xaxes(visible=False)
        self.update_yaxes(visible=False, scaleanchor="x", scaleratio=1)

        # чтобы покрасивее вписывалась карта на поверхность фигуры, значения можно будет переопределять
        self.update_layout(showlegend=False, dragmode='pan',
                           width=800, height=450, 
                           margin={'l': 10, 'b': 10, 't': 10, 'r': 10})  # отступы по умолчанию слишком большие