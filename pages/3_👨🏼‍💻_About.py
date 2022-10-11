import streamlit as st
from footer import *

st.balloons()
st.header("ABOUT ForexLIT")
st.sidebar.success("The purpose and development setup of ForexLIT")

st.markdown('''
* This is a light-weight web application that provides realtime data for several Foreign and Crypto currency exchange rates and allows user to find the realtime status of the same along with the ability to perform currency conversions. 
* The Data is fetched from the freely avaialble [ExchangeRate API](https://exchangerate.host/#/).
* This webapp is coded with [Streamlit](https://streamlit.io/) in Python.
* For the purpose of data ingestion, cleaning and visualisation; libraries like `pandas` and `plotly` have been used.
* Source codes are available in [GitHub](https://github.com/ineelhere/forexlit).
* This webapp is deployed on [Streamlit Comunity Cloud](https://share.streamlit.io/).
* This webapp is also available on [dockerhub](https://hub.docker.com/r/ineelhere/forexlit) as a docker image - `ineelhere/forexlit:latest`
* For any queries and feedback please reach out to [Indraneel](https://www.linkedin.com/in/indraneelchakraborty/).
''')

st.sidebar.markdown('''
<div style="padding-top:100.000%;position:relative;"><iframe src="https://gifer.com/embed/bf6" width="100%" height="100%" style='position:absolute;top:0;left:0;' frameBorder="0" allowFullScreen></iframe></div><p><a href="https://gifer.com">via GIFER</a></p>
''', unsafe_allow_html=True)
footer()