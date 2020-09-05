import dash

external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/sketchy/bootstrap.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, external_scripts=[
	'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML'])

app.config.suppress_callback_exceptions = True
server = app.server

