import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.bar_chart(df)

btn = st.multiselect(
    "Some text", [2, 4, 6, 8, 10], format_func=lambda x: str(x) + ":option " + str(x)
)

btn
#20260119