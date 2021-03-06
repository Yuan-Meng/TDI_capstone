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

    dcc.Markdown(""" ### "If I get COVID-19, how bad will it be?" """),

    dcc.Markdown('---'),

    dcc.Markdown('#### Your predicted outcome severity'),

    html.Div(id='outcome-prediction', style={'fontWeight': 'bold'}),

    html.Div([
        dcc.Markdown('###### Biological Sex'),
        dcc.Markdown("""Please select your biological sex 
            (due to limited data, we cannot predict for other biological sexes at this moment):"""),
        dcc.Dropdown(
            id='sex',
            options=[
                {'label': 'Male', 'value': 1},
                {'label': 'Female', 'value': 0}
                ]),
        ], style=style),

    html.Div([
        dcc.Markdown('###### Age Group'),
        dcc.Markdown('Please select the age group that you belong to:'),
        dcc.Dropdown(
            id='age_group',
            options=[
                {'label': "0-9 Years", 'value': "0_9"},
                {'label': "10-19 Years", 'value': "10_19"},
                {'label': "20-29 Years", 'value': "20_29"},
                {'label': "30-39 Years", 'value': "30_39"},
                {'label': "40-49 Years", 'value': "40_49"},
                {'label': "50-59 Years", 'value': "50_59"},
                {'label': "60-69 Years", 'value': "60_69"},
                {'label': "70-79 Years", 'value': "70_79"},
                {'label': "80+ Years", 'value': "80_99"},
                ]),
        ], style=style),

    html.Div([
        dcc.Markdown('###### Race/Ethnicity'),
        dcc.Markdown('Please select the race/ethnicity that you most identify with:'),
        dcc.Dropdown(
            id='race',
            options=[
                {'label': "Asian, Non-Hispanic", 'value': "asian"},
                {'label': "White, Non-Hispanic", 'value': "white"},
                {'label': "Black, Non-Hispanic", 'value': "black"},
                {'label': "Multiple/Other, Non-Hispanic", 'value': "multi"},
                {'label': "Hispanic/Latino", 'value': "hispanic"},
                {'label': "Native Hawaiian/Pacific Islander", 'value': "pacific"},
                {'label': "American Indian/Alaska Native", 'value': "native"},
                ]),
        ], style=style),

    html.Div([
        dcc.Markdown('###### Medical Condition'),
        dcc.Markdown("""Please select "Yes" if you have diabetes, hypertension, asthma, COPD,
            chronic heart and kidney diseases, or other diseases that may intensify COVID-19 symptoms
            (Not sure? You can check out [CDC guidelines](https://www.cdc.gov/coronavirus/2019-ncov/need-extra-precautions/people-with-medical-conditions.html)!):"""),
        dcc.Dropdown(
            id='medcond',
            options=[
                {'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0}
                ]),
        ], style=style),

    dcc.Markdown('---'),

    dcc.Markdown("""#### Factors contributing to severity"""),

    dcc.Markdown("""

        While most COVID-19 patients didn't experience severe outcomes such as ICU stays or death, some
        went through hell. What predicts who has what outcome?

        """),

    html.Img(src=app.get_asset_url('outcome.png'), height=350),

    dcc.Markdown("""

        If you read the news, chances are you often hear a series of factors contribute to
        severe outcomes of COVID-19, such as advanced age, having certain pre-existing 
        medical conditions (e.g., diabetes, COPD, cancer, heart and kidney diseases, etc.), being biologically male, coming
        from a disadvantaged social group, and so on.
        However, intuitions alone cannot go so far to tell us the relative importance of these factors, let alone
        the degree to which each factor worsens the outcome.
 
        Using [Shapley values](https://christophm.github.io/interpretable-ml-book/shapley.html), we can figure out more precisely
        how much each feature matters to the final prediction and in what way. As can be seen from the figure below, being over 70 
        and 80 and having a pre-existing medical condition are major contributors to COVID-19 outcome severity. 

        """),

    html.Img(src=app.get_asset_url('feature_imps.png'), height=500),

    dcc.Markdown('*&copy; 2020 Yuan Meng*')

])

# --- 3. Predict outcome severity --- #
# Organize user answers
@app.callback(
    Output('outcome-prediction', 'children'),
    [Input('sex', 'value'),
     Input('age_group', 'value'),
     Input('race', 'value'),
     Input('medcond', 'value')])
def predict_outcome(sex, age_group, race, medcond):

    df_user = pd.DataFrame(
        columns=[
        "sex_Male",
        "age_group_0_9",
        "age_group_10_19",
        "age_group_20_29",
        "age_group_30_39",
        "age_group_40_49",
        "age_group_50_59",
        "age_group_60_69",
        "age_group_70_79",
        "age_group_80_99",
        "race_asian",
        "race_black",
        "race_hispanic",
        "race_multi",
        "race_native",
        "race_pacific",
        "race_white",
        "medcond_Yes",
        ],
        index=[0],
        )

    for col in df_user.columns:
        df_user[col] = 1 if (str(age_group) in col or str(race) in col) else 0

    df_user["sex_Male"] = 1 if sex == 1 else 0

    df_user["medcond_Yes"] = 1 if medcond == 1 else 0

    with open("model/lgb_clf.pkl", "rb") as file:
        model = dill.load(file)

    new_pred = model.predict_proba(df_user)

    results = f"Your probability of having severe outcomes is {round(new_pred.tolist()[0][1] * 100, 2)}% if contracted COVID-19."

    return results