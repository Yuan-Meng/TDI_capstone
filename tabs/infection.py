# --- 1. Library imports --- #
# Dash libraries 
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

# Data handling 
import dill 
import numpy as np
import pandas as pd

from app import app

# --- 2. Get user input --- #
# Questions
style = {'padding': '1.5em'}

layout = html.Div([

    html.Br(),

    dcc.Markdown(""" ### "How likely may I get COVID-19?" """),

    dcc.Markdown('---'),

    dcc.Markdown('#### Your predicted infection risk'),

    html.Div(id='infection-prediction', style={'fontWeight': 'bold'}),

    html.Div([
        dcc.Markdown('###### State of Residence'),
        dcc.Markdown("""Which state do you currently live in? Please use [2-letter abbreviation](https://about.usps.com/who-we-are/postal-history/state-abbreviations.htm)
            (e.g., "CA" for "California") to indicate:"""),
        dcc.Input(id="state", type="text", placeholder="", value="CA"),
        ], style=style),

    html.Div([
        dcc.Markdown('###### Social Bubble Size'),
        dcc.Markdown("""Over the past 2 weeks, how many people have you had
             contact with for one hour or longer?"""),
        dcc.Input(id="bubble", type="number", placeholder="", value=10),
        ], style=style),

    dcc.Markdown('---'),

    dcc.Markdown('#### How risk grows with social bubble'),

    dcc.Markdown("""It goes without saying that the more people you socialize with, 
        the more likely you may be infected by one person or another.
        However, with our mere imagination, it's hard to tell how quickly infection risk grows
        with social bubble size. The figure below visualizes this relationship under 3 different infection rates."""),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': np.arange(1, 101), 'y': 1 - ((1 - 0.01 * 0.081) ** np.arange(1, 101)), 'type': 'line', 'name': 'Infection Rate = 1%'},
                {'x': np.arange(1, 101), 'y': 1 - ((1 - 0.05 * 0.081) ** np.arange(1, 101)), 'type': 'line', 'name': 'Infection Rate = 5%'},
                {'x': np.arange(1, 101), 'y': 1 - ((1 - 0.1 * 0.081) ** np.arange(1, 101)), 'type': 'line', 'name': 'Infection Rate = 10%'},
            ],
            'layout': {
                'title': 'Infection Risk as a Function of Social Bubble Size',
                'xaxis':{
                    'title':'Social Bubble',
                },
                'yaxis':{
                    'title':'Probability of Infection'
                },
            }
        }
    )

    ])

# --- 3. Predict outcome severity --- #
# Organize user answers
@app.callback(
    Output('infection-prediction', 'children'),
    [Input('state', 'value'),
     Input('bubble', 'value')])
def predict_infection(state, bubble):

    # Positive viral test rate in given state
    with open("model/pos_rate.pkl", "rb") as file:
        df = dill.load(file)
    
    state_pos = df.loc[df["state"] == str(state).upper(), "pos_rate"].values

    p_pos = state_pos[0] if len(state_pos) > 0 else 0.05

    # Infectivity of a random COVID-19 carrier
    p_infect = (0.6 * np.median([0.8, 15.4]) + 0.4 * np.median([0.8, 15.4])) / 100

    # Infect risk given social bubble size
    p_infected = 1 - (1 -(p_pos * p_infect)) ** int(bubble)

    results = f"Your probability of contracting COVID-19 from social contacts is {round(p_infected, 2) * 100}%."

    return results