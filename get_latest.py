import pandas as pd
import plotly.express as px
import streamlit as st


def get_latest(base_currency):
    #data management
    df = pd.read_json(f'https://api.exchangerate.host/latest?base={base_currency}')
    df = df.reset_index()
    df.drop([0,1], axis=0, inplace=True)
    df.drop(columns=['motd', 'success'])
    df = df.rename(columns={'index': 'Currency', 'rates': 'Exchange Rate', 'base':'Base'}) 
    
    #create 2 cols
    xcol1, xcol2 = st.columns(2)
    
    #display the data
    xcol1.dataframe(df[["Currency", "Base","Exchange Rate"]].reset_index(drop=True))
    xcol1.download_button("Press to Download", df[["Currency", "Base","Exchange Rate"]].reset_index(drop=True).to_csv().encode('utf-8'),"file.csv","text/csv",key='download-csv')
    xcol2.success(f" 1 {base_currency} = {(df.loc[df.Currency=='USD']).reset_index(drop=True)['Exchange Rate'][0]} USD")
    xcol2.success(f" 1 {base_currency} = {(df.loc[df.Currency=='EUR']).reset_index(drop=True)['Exchange Rate'][0]} EUR")
    xcol2.success(f" 1 {base_currency} = {(df.loc[df.Currency=='INR']).reset_index(drop=True)['Exchange Rate'][0]} INR")
    xcol2.success(f" 1 {base_currency} = {(df.loc[df.Currency=='JPY']).reset_index(drop=True)['Exchange Rate'][0]} JPY")
    xcol2.success(f" 1 {base_currency} = {(df.loc[df.Currency=='AUD']).reset_index(drop=True)['Exchange Rate'][0]} AUD")
    xcol2.success(f" 1 {base_currency} = {(df.loc[df.Currency=='BTC']).reset_index(drop=True)['Exchange Rate'][0]} BTC")
    

    #generate the plot
    fig = px.bar(df, x="Currency", y="Exchange Rate", title=f'Excahnge Rates in {base_currency}')
    st.plotly_chart(fig, use_container_width=True)

