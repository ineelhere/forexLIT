import streamlit as st
import pandas as pd
from get_glossary import *

def get_exchange(from_cur, to_cur):
    df = pd.read_json(f'https://api.exchangerate.host/convert?from={from_cur}&to={to_cur}')
    df = df.reset_index()
    df.drop([0,1], axis=0, inplace=True)
    df = df.reset_index(drop=True)
    df = df.drop(columns=['motd', 'success', 'info', 'historical','date'])

    xcol1, xcol2, xcol3, xcol4 = st.columns(4)
    xcol1.info(f'**{df["query"][0]} ({get_glossary(df["query"][0])})**')
    xcol2.warning(f'**{df["query"][2]}**')
    xcol3.success(f'**{df["query"][1]} ({get_glossary(df["query"][1])})**')
    xcol4.error(f'**{df["result"][0]}**')

