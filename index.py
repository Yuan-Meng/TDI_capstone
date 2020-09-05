from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app, server
from tabs import intro, outcome, infection, author

style = {'maxWidth': '960px', 'margin': 'auto'}

app.layout = html.Div([
    dcc.Markdown('# Reopen Navigator'),
    dcc.Markdown('##### Predict Your COVID-19 Infection Risk and Outcome Severity'),
    dcc.Tabs(id='tabs', value='tab-intro', children=[
        dcc.Tab(label='About This App', value='tab-intro'),
        dcc.Tab(label='Infection Risk', value='tab-infection'),
        dcc.Tab(label='Outcome Severity', value='tab-outcome'),
        dcc.Tab(label='Contact Author', value='tab-author'),
    ]),
    html.Div(id='tabs-content'),
], style=style)

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-intro': return intro.layout
    elif tab == 'tab-outcome': return outcome.layout
    elif tab == 'tab-infection': return infection.layout
    elif tab == 'tab-author': return author.layout

if __name__ == '__main__':
    app.run_server(debug=True)
