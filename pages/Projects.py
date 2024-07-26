import streamlit as st
import base64
from streamlit_card import card
from config import *

def encode_image(filepath):
    with open(filepath, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    return "data:image/png;base64," + encoded.decode("utf-8")

st.set_page_config(page_title="Projects",
                       page_icon='assets/favicon.png',
                       layout="wide",
                       initial_sidebar_state='collapsed')
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


card_images = ["assets/gmx.png","assets/ethereum.png","assets/pragma_finance.png","assets/elections.png"]
gmx = encode_image(card_images[0])
ethereum = encode_image(card_images[1])
pragma_finance = encode_image(card_images[2])
elections = encode_image(card_images[3])



plot_cols = st.columns(3) 
with plot_cols[0]:
    hasClicked = card(
    title="GMX V1",
    text="Dashboard",
    image=gmx,
    url='https://github.com/oliinykm99/gmx-st-dashboard',
    styles = {
    "card": {
        "width": "325px", 
        "height": "325px",
        "box-shadow": "none"},
    "filter": {
        "background-color": "rgba(0, 0, 0, 0.35)" 
    }   
}) 

with plot_cols[1]:
    hasClicked = card(
    title="ETH",
    text="XGBoost Prediction",
    image=ethereum,
    url='https://github.com/oliinykm99/ETH-XGBoost-prediction',
    styles = {
    "card": {
        "width": "325px", 
        "height": "325px",
        "box-shadow": "none"},
    "filter": {
        "background-color": "rgba(0, 0, 0, 0.35)" 
    }   
}) 
    
with plot_cols[2]:
    hasClicked = card(
    title="Pragma Finance",
    text="Dashboards",
    image=pragma_finance,
    url='https://google.com',
    styles = {
    "card": {
        "width": "325px", 
        "height": "325px",
        "box-shadow": "none"},
    "filter": {
        "background-color": "rgba(0, 0, 0, 0.35)" 
    }   
}) 
    
plot_cols = st.columns(3) 
with plot_cols[0]:
    hasClicked = card(
    title="US Elections 2020",
    text="Prediction",
    image=elections,
    url='https://github.com/oliinykm99/United-States-Election-2020-Prediction',
    styles = {
    "card": {
        "width": "325px", 
        "height": "325px",
        "box-shadow": "none"},
    "filter": {
        "background-color": "rgba(0, 0, 0, 0.35)" 
    }   
}) 


if st.button("Mainpage"):
    st.switch_page("Mainpage.py")


