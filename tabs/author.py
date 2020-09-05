from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [

    html.Br(),

    dcc.Markdown("""### Contact Me"""),

    dcc.Markdown("""Thanks for checking out my web app and hope it helped you navigate the post-lockdown world!
    	My name is Yuan Meng, a PhD candidate in Psychology at UC Berkeley, a Summer 2020 Fellow at The Data Incubator, and a fellow human being
    	trying to figure out their life in this pandemic."""),

    html.Img(src=app.get_asset_url('yuan_pandemic.jpg'), height=350),

    dcc.Markdown("""
    	If you have any questions regarding how I built this app or just want to chat about data science, science, and random COVID musings, 
    	do feel free to shoot me an email ([yuan_meng@berkeley.edu](yuan_meng@berkeley.edu))!
    	
    	*&copy; 2020 Yuan Meng*
    	""")
    ]
