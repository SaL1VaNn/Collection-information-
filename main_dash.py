import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

app = dash.Dash(__name__)

data = {
    'Графік 1 (24.02.2022 - 31.03.2022)': {
        'countries': ['США', 'Велика Британія', 'Канада', 'Польща', 'Хорватія', 'Австралія', 'Латвія', 'Литва', 'Німеччина'],
        'help_amounts': [500_000_000, 356_000_000, 775_000_000, 150_000_000, 16_500_000, 50_000_000, 25_000_000, 20_000_000, 40_000_000]
    },
    'Графік 2 (03.04.2022 - 03.06.2022)': {
        'countries': ['Велика Британія', 'США', 'Нідерланди', 'Норвегія', 'Канада', 'Польща', 'Болгарія', 'Німеччина', 'Естонія'],
        'help_amounts': [110_000_000, 800_000_000, 500_000_000, 50_000_000, 500_000_000, 466_000_000, 25_000_000, 230_000_000, 20_000_000]
    },
    'Графік 3 (05.06.2022 - 07.08.2022)' : {
        'countries' : ['Литва', 'США', 'Нідерланди', 'Німеччина', 'Франція', 'Польща', 'Болгарія', 'Фінляндія', 'Японія', 'Іспанія'],
        'help_amounts' : [60_000_000, 1_550_000_000, 500_500_000, 102_500_000, 285_000_000, 630_000_000, 185_000_000, 240_000_000, 200_000_000, 80_000_000]
    },
    'Графік 4 (08.08.2022 - 15.10.2022)' : {
        'countries' : ['Велика Британія', 'США', 'Німеччина', 'Норвегія', 'Канада', 'Польща', 'Болгарія', 'Тайвань', 'Латвія', 'Словаччина', 'Данія', 'Турція', 'Словенія', 'Литва', 'Фінляндія', 'Японія'],
        'help_amounts' : [560_000_000, 1_500_000_000, 516_500_000, 50_000_000, 110_000_000, 50_000_000, 70_000_000, 256_000_000, 300_000_000, 272_000_000, 110_000_000, 33_000_000, 55_000_000, 101_000_000, 50_000_000, 150_000_000]
    },
    'Графік 5 (16.10.2022 - 30.12.2022)' : {
        'countries' : ['Італія', 'США', 'Нідерланди', 'Німеччина', 'Литва', 'Швеція', 'Болгарія', 'Фінляндія', 'Данія', 'Японія', 'Іспанія'],
        'help_amounts' : [400_000_000, 4_582_000_000, 220_000_000, 725_000_000, 40_000_000, 287_000_000, 80_000_000, 65_000_000, 53_000_000, 100_000_000, 100_000_000]
    },
    'Графік 6 (01.01.2023 - 24.02.2023)' : {
        'countries' : ['Велика Британія', 'США', 'Португалія', 'Марокко', 'Канада', 'Латвія', 'Естонія', 'Данія', 'Литва', 'Фінляндія', 'Норвегія', 'Італія', 'Японія'],
        'help_amounts' : [530_000_000, 2_700_000_000, 245_000_000, 40_000_000, 300_000_000, 410_000_000, 213_000_000, 143_000_000, 43_000_000, 400_000_000, 240_000_000, 780_000_000, 150_000_000]
    },
    'Графік 7 (всі країни разом: по окремому періоду та за рік)' : {
        'period' : ['24.02.2022 - 31.03.2022', '03.04.2022 - 03.06.2022', '05.06.2022 - 07.08.2022', '08.08.2022 - 15.10.2022', '16.10.2022 - 30.12.2022', '01.01.2023 - 24.02.2023', 'За весь рік'],
        'help_amounts' : [1_847_500_000, 2_683_000_000, 3_547_000_000, 4_033_500_000, 6_552_000_000, 5_774_000_000, 24_436_500_000]
    },
    'Графік 8 (Донат кожної країни поокремо)' : {
        'countries' : ['США','Велика Британія', 'Канада', 'Польща', 'Хорватія','Австралія','Нідерланди', 'Норвегія', 'Болгарія', 'Литва','Німеччина','Франція','Фінляндія','Японія','Турція', 'Данія','Словаччина', 'Латвія', 'Тайвань', 'Словенія', 'Італія', 'Швеція', 'Марокко','Португалія', 'Естонія', 'Іспанія'],
        'help_amounts' : [11_000_000_000, 1_430_000_000, 1_360_000_000, 350_000_000, 16_500_000, 550_000_000, 883_000_000, 694_000_000, 250_000_000, 100_000_000, 912_000_000, 102_000_000, 955_000_000, 600_000_000, 33_000_000, 249_000_000, 272_000_000, 340_000_000, 256_000_000, 55_000_000, 780_000_000, 287_000_000, 40_000_000, 45_000_000, 133_000_000, 180_000_000]
    }
}

def create_graph(selected_graph):
    graph_data = data[selected_graph]
    
    if selected_graph != 'Графік 7 (всі країни разом: по окремому періоду та за всі)':
        trace = go.Bar(x=graph_data['countries'], y=graph_data['help_amounts'])
        xaxis_title = 'Країни'
    else:
        trace = go.Bar(x=graph_data['period'], y=graph_data['help_amounts'])
        xaxis_title = 'Період'
    
    layout = go.Layout(
        title=f'Допомога країн Україні за {selected_graph}',
        xaxis=dict(title=xaxis_title),
        yaxis=dict(title='Сума допомоги (мільйони у доларах)'),
        margin=dict(l=40, r=40, t=80, b=40),
    )
    
    fig = go.Figure(data=[trace], layout=layout)
    
    return fig


app.layout = html.Div([
    html.H1("Графіки допомоги країн Україні за різні періоди"),
    dcc.Dropdown(
        id='graph-dropdown',
        options=[{'label': key, 'value': key} for key in data.keys()],
        value=list(data.keys())[0]
    ),
    dcc.Graph(id='graph')
])

@app.callback(
    Output('graph', 'figure'),
    Input('graph-dropdown', 'value')
)
def update_graph(selected_graph):
    return create_graph(selected_graph)

if __name__ == "__main__":
    app.run_server(debug=True)