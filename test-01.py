import streamlit as st
from streamlit_option_menu import option_menu

import pydeck as pdk

import streamlit as st
import pandas as pd
import numpy as np

INITIAL_VIEW_STATE = pdk.ViewState(latitude=35.4799, longitude=-79.1803, zoom=12, max_zoom=24, pitch=0, bearing=0)

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 2


def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "MDD", "Quality", "Fire", "Material", "I-Hydrant"],  # required
                icons=["house", "shield-check", "brilliance", "water", "pass", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "MDD", "Quality", "Fire", "Material", "I-Hydrant"],  # required
            icons=["house", "shield-check","brilliance", "water","pass", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "MDD", "Quality", "Fire", "Material", "I-Hydrant"],  # required
            icons=["house", "shield-check","brilliance", "water","pass", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)


pipe_layer = pdk.Layer(
    "MVTLayer",
    data="https://a.tiles.mapbox.com/v4/hazensawyer.cx9utjpr/{z}/{x}/{y}.vector.pbf?access_token=pk.eyJ1IjoiaGF6ZW5zYXd5ZXIiLCJhIjoiY2xmNGQ3MDgyMTE3YjQzcnE1djRpOGVtNiJ9.U06GItbSVWFTsvfg9WwQWQ",
    get_line_color=[0, 163, 108],
    get_fill_color=[155, 0, 100],
    line_width_min_pixels=2,
    pickable=True,
   
)

hydrant_layer = pdk.Layer(
    "MVTLayer",
    data="https://a.tiles.mapbox.com/v4/hazensawyer.abnchmyr/{z}/{x}/{y}.vector.pbf?access_token=pk.eyJ1IjoiaGF6ZW5zYXd5ZXIiLCJhIjoiY2xmNGQ3MDgyMTE3YjQzcnE1djRpOGVtNiJ9.U06GItbSVWFTsvfg9WwQWQ",
    minZoom= 12.5,
    maxZoom= 23,
    filled= True,
    getIconAngle= 0,
    getIconColor= [0, 0, 0, 255],
    getIconPixelOffset= [-2, 2],
    getIconSize= 3,
    #getText: (f) => f.properties.FACILITYID,
    getPointRadius= 8, 
    get_fill_color='[180, 0, 200, 140]',
    # getTextAlignmentBaseline= "center",
    # getTextAnchor= "middle",
    # getTextAngle= 0,
    # getTextBackgroundColor= [0, 0, 0, 255],
    # getTextBorderColor= [0, 0, 0, 255],
    # getTextBorderWidth= 0,
    # getTextColor= [0, 0, 0, 255],
    # getTextPixelOffset= [-12, -12],
    # getTextSize= 20,
    pointRadiusMinPixels= 2,
    pickable=True,
    autoHighlight= True,
    pointType= "circle+text",
)

tooltip = ({
        "html": "<b>Diameter:</b> {Diameter}",
        "style": {"backgroundColor": "red", "color": "white"}
    })



# Create the deck.gl map
r = pdk.Deck(
    height=900, 
    width=1200, 
    layers=[pipe_layer, hydrant_layer],
    initial_view_state=INITIAL_VIEW_STATE,
    map_style="mapbox://styles/hazensawyer/clnlt5te9003l01p5fta3hjc8", 
    api_keys={"mapbox": "pk.eyJ1IjoiaGF6ZW5zYXd5ZXIiLCJhIjoiY2xmNGQ3MDgyMTE3YjQzcnE1djRpOGVtNiJ9.U06GItbSVWFTsvfg9WwQWQ"},
    tooltip=tooltip, 
)


if selected == "Home":
    st.pydeck_chart(r)
    st.write("Click on features to see tooltip information")
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")