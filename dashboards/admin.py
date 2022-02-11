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
    options_role_dropdown = [{"label":"Admin", "value":"admin"}, {"label":"jefe", "value":"jefe"}, {"label":"analista", "value":"analista"}, {"label":"cliente", "value":"cliente"}]
    layout = html.Div([
                        html.Div(id='none',children=[],style={'display': 'none'})
                        , dbc.Row([html.H1("Admin Sinba", id="title-admin", style={"color":"#1b2b58", "font-size":"28px"})],
                                justify = 'center')
                        , dbc.Col(
                                [html.Label("Llena los campos para crear un nuevo usuario", className="label")
                                , dbc.Row(
                                            [
                                            dbc.Col(dbc.Input(type="text", id="admin-create-user-name", placeholder="Ingresa nombre del usuario", className="admin-name-input"), width=3, style={"marginTop":"2.5px", "marginBottom":"2.5px"})
                                            , dbc.Col(dbc.Input(type="text", id="admin-create-user-username", placeholder="Ingresa correo del usuario", className="admin-username-input"), width=3, style={"marginTop":"2.5px", "marginBottom":"2.5px"})
                                            , dbc.Col(dbc.Input(type="password", id="admin-create-user-password", placeholder="Ingresa contraseña", className="admin-password-input"), width=3, style={"marginTop":"2.5px", "marginBottom":"2.5px"})
                                            , dbc.Col(utils.dropdown(id="admin-dropdown-role", value=None, options=options_role_dropdown, placeholder="Selecciones rol del usuario"), width=3, style={"marginTop":"2.5px", "marginBottom":"2.5px"})
                                            , dbc.Col(utils.dropdown(id="admin-dropdown-view", options=[{"value":"admin", "label":"admin"}, {"value":"procesamiento1", "label":"Procesamiento 1"}], multi=True, placeholder="Selecciona vistas asociadas"), width=3, style={"marginTop":"2.5px", "marginBottom":"2.5px"})
                                            , dbc.Col(html.Button("Crear usuario", id="btn-admin-create-user", n_clicks=0), width=3, style={"marginTop":"2.5px", "marginBottom":"2.5px"})
                                            ]
                                        )]
                                    )
                        ], className = "dash-inside-container")
    return layout
