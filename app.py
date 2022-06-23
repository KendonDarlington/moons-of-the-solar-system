from dash import Dash, dcc, html, Input, Output, dash, dash_table, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from plotly.graph_objs import *



#Import data
df = pd.read_csv('C:\\Users\\kendo\\Downloads\\MoonsOfTheSolarSystem.csv')

#Define the app and set the theme!
app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])
server = app.server

#Here is the front end
app.layout = html.Div([
    
    #Jumbotron
    html.Div(
        dbc.Container(
            [
                html.H1("Moons of the Solar System", className="display-3"),
                html.P(
                    "Learn about the planets and their moons "
                    "through the power of Python!",
                    className="lead",
                ),
                html.Hr(className="my-2"),
                html.P(
                    "Select a planet to see its moons."
                ),
                
                html.P(
                    dbc.Select(
                        id="selectPlanet",
                        style={"width": "20%"},
                        options=[
                            {"label": "Chose a Planet", "value": "1", "disabled": True},
                            {"label": "Earth", "value": "2"},
                            {"label": "Mars", "value": "3"},
                            {"label": "Jupiter", "value": "4"},
                            {"label": "Saturn", "value": "5"},
                            {"label": "Uranus", "value": "6"},
                            {"label": "Neptune", "value": "7"},
                            {"label": "Pluto", "value": "8"},
                        ],
                        value='1',
                    ), className="lead"
                ),
                
            ],
            fluid=True,
            className="py-3",
        ),
        className="h-100 p-7 text-white bg-dark rounded-3",
    ),
    
    html.Br(),  
    html.Br(),
    
    #A row with our image and dashtable
    dbc.Row(
        [
            dbc.Col(width=1),
            dbc.Col(
                html.Div(id='imageContainer', children=[
                        html.Img(src="/assets/moon1.png")
                    ]),width=3
            ),
            dbc.Col(width=1),            
            dbc.Col(
                    html.Div([
                        dash_table.DataTable(
                            id = 'dt1', 
                            columns =  [{"name": i, "id": i,} for i in (df.columns)],
                            page_action="native",
                            page_current= 0,
                            page_size= 10,
                            style_header={
                                        'backgroundColor': 'rgb(30, 30, 30)',
                                        'color': 'white'
                                    },
                            style_data={
                                'backgroundColor': 'rgb(50, 50, 50)',
                                'color': 'white',
                                'height': 'auto',
                            },    
                            style_cell={
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                                'maxWidth': 135,
                            },
                            #css=[{'selector': 'table', 'rule': 'table-layout: fixed'}],  
                        ),
                        
                    html.Div(id='datatable-interactivity-container')
                ]),width=6
                ),
            dbc.Col(width=1)
        ]
    ),

])


#Here is the back end

#When you select planets, we swap the images
@app.callback(
    Output('imageContainer', 'children'),
    [Input('selectPlanet','value')]
)
def swapImg(value):  
    if value == '2': 
        return html.Img(src="/assets/Earth.png")
    if value == '3': 
        return html.Img(src="/assets/Mars.png")
    if value == '4': 
        return html.Img(src="/assets/Jupiter.png")
    if value == '5': 
        return html.Img(src="/assets/Saturn.png")
    if value == '6': 
        return html.Img(src="/assets/Uranus.png")
    if value == '7': 
        return html.Img(src="/assets/Neptune.png")
    if value == '8': 
        return html.Img(src="/assets/Pluto.png")
    return html.Img(src="/assets/Sun.png")


#When you select planets, we filter the datatable
@app.callback(Output('dt1','data'),
            [Input('selectPlanet','value')])

def update_datatable(value):    
    #Earth
    if value == '2':
        dfRestricted = df[df['Parent']=='Earth']
        return dfRestricted.to_dict('rows')
    
    #Mars
    if value == '3':
        dfRestricted = df[df['Parent']=='Mars']
        return dfRestricted.to_dict('rows')
    
    #Jupiter
    if value == '4':
        dfRestricted = df[df['Parent']=='Jupiter']
        return dfRestricted.to_dict('rows')
    
    #Saturn
    if value == '5':
        dfRestricted = df[df['Parent']=='Saturn']
        return dfRestricted.to_dict('rows')
    
    #Uranus
    if value == '6':
        dfRestricted = df[df['Parent']=='Uranus']
        return dfRestricted.to_dict('rows')
    
    #Neptune
    if value == '7':
        dfRestricted = df[df['Parent']=='Neptune']
        return dfRestricted.to_dict('rows')
    
    #Pluto
    if value == '8':
        dfRestricted = df[df['Parent']=='Pluto']
        return dfRestricted.to_dict('rows')
    
    return df.to_dict('rows')


if __name__ == '__main__':
    app.run_server(debug=True)