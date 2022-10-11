import streamlit as st
from footer import *

st.balloons()
st.header("ForexLIT")

st.markdown('''
* This is a light-weight web application that fetches realtime data for several Foreign and Crypto currency exchange ratesand allows user to find the realtime status of the same and perform currency conversions. 
* The Data is fetched from the freely avaialble [ExchangeRate API](https://exchangerate.host/#/).
* This webapp is coded with [Streamlit](https://streamlit.io/) in Python 3.8.
* For the purpose of data ingestion, cleaning and visualisation; libraries like `pandas` and `plotly` have been used.
* Source codes are available in [GitHub](https://github.com/ineelhere/forexlit).
* This webapp is deployed on [Streamlit Comunity Cloud](https://share.streamlit.io/).
* This webapp is also available on [dockerhub](https://hub.docker.com/r/ineelhere/forexlit) as a docker image - `ineelhere/forexlit:latest`
* For any queries and feedback please reach out to [Indraneel](https://www.linkedin.com/in/indraneelchakraborty/).
''')

footer()