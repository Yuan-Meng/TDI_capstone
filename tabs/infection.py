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

    dcc.Markdown(""" ### "How likely may I get COVID-19?" """),

    dcc.Markdown("""Please answer the 2 questions below to predict
        how likely you may contract COVID-19."""),

    dcc.Markdown('#### Your prediction:'),

    html.Div(id='infection-prediction', style={'fontWeight': 'bold'}),

    html.Div([
        dcc.Markdown('###### State of Residence'),
        dcc.Markdown("""Which state do you currently live in? Please use [2-letter abbreviations](https://about.usps.com/who-we-are/postal-history/state-abbreviations.htm)
            (e.g., "CA" for "California") to indicate:"""),
        dcc.Input(id="state", type="text", placeholder="", value="CA"),
        ], style=style),

    html.Div([
        dcc.Markdown('###### Social Bubble Size'),
        dcc.Markdown("""Over the past 2 weeks, how many people have you had
             contact with for one hour or longer?"""),
        dcc.Input(id="bubble", type="number", placeholder="", value=10),
        ], style=style),

    ])

# --- 3. Predict outcome severity --- #
# Organize user answers
@app.callback(
    Output('infection-prediction', 'children'),
    [Input('state', 'value'),
     Input('bubble', 'value')])
def predict_infection(state, bubble):

    with open("model/pos_rate.pkl", "rb") as file:
        df = dill.load(file)

    state_pos = df.loc[df["state"] == str(state), "pos_rate"].values

    p_pos = state_pos[0] if len(state_pos) > 0 else 0.05

    p_infect = (0.6 * np.median([0.8, 15.4]) + 0.4 * np.median([0.8, 15.4])) / 100

    p_infected = 1 - (1 -(p_pos * p_infect)) ** int(bubble)

    results = f"Your probability of contracting COVID-19 from your social contacts is {round(p_infected, 2) * 100}%."

    return results