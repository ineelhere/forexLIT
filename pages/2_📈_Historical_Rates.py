import streamlit as st
import random
from get_random import *
st.json(get_random(random.randint(1, 6871)))
