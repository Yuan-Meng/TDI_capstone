from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Contact Me

Thanks for checking out my web app and hope it helped inform your decisions during this pandemic! 

My name is Yuan Meng, a PhD candidate in Psychology at UC Berkeley and a Summer 2020 Fellow at The Data Incubator.
If you have any questions about how I built this app, please feel free to shoot me an email ([yuan_meng@berkeley.edu](yuan_meng@berkeley.edu))!

*&copy; 2020 Yuan Meng*

""")]
