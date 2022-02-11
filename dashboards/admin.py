import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
from flask import request, session, json
from utils import utils_google, utils
import pandas as pd
import requests

def serve_layout():
    options_role_dropdown = [{"label":"admin", "value":"admin"}, {"label":"jefe", "value":"jefe"}, {"label":"analista", "value":"analista"}, {"label":"cliente", "value":"cliente"}]
    layout = html.Div([
                        html.Div(id='none',children=[],style={'display': 'none'})
                        , dbc.Row([html.H1("Admin Sinba", id="title-admin", style={"color":"#1b2b58", "font-size":"28px"})],
                                justify = 'center')
                        , dbc.Col(
                                [html.Label("Llena los campos para crear un nuevo usuario", className="label")
                                , dbc.Row(
                                            [
                                            dbc.Col(dbc.Input(type="text", id="admin-create-user-name", placeholder="Nombres", className="admin-name-input"), width=3, style={"marginTop":"2.5px", "marginBottom":"2.5px"}, className="input-col")
                                            , dbc.Col(dbc.Input(type="text", id="admin-create-user-username", placeholder="Correo", className="admin-username-input"), width=3, style={"marginTop":"2.5px", "marginBottom":"2.5px"}, className="input-col")
                                            , dbc.Col(dbc.Input(type="password", id="admin-create-user-password", placeholder="Contraseña", className="admin-password-input"), width=3, style={"marginTop":"2.5px", "marginBottom":"2.5px"}, className="input-col")
                                            , dbc.Col(utils.dropdown(id="admin-dropdown-role", value=None, options=options_role_dropdown, placeholder="Rol"), width=3, style={"marginTop":"2.5px", "marginBottom":"2.5px"}, className="input-col")
                                            , dbc.Col(utils.dropdown(id="admin-dropdown-view", options=[{"value":"Admin", "label":"admin"}, {"value":"procesamiento1", "label":"Procesamiento 1"}], multi=True, placeholder="Vistas"), width=3, style={"marginTop":"2.5px", "marginBottom":"2.5px"}, className="input-col")
                                            , dbc.Col(html.Button("Crear usuario", id="btn-admin-create-user", n_clicks=0), width=3, style={"marginTop":"2.5px", "marginBottom":"2.5px"}, className="input-col")
                                            ]
                                        )]
                                    )
                        ], className = "dash-inside-container")
    return layout
