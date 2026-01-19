import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

def page1():
    st.title("Page 1")
    df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
    st.bar_chart(df)
    btn = st.multiselect(
        "Some text", [2, 4, 6, 8, 10], format_func=lambda x: str(x) + ":option " + str(x)
    )
    btn    

def page2() -> st.Page:
    p=st.Page("pivot.py", title="Second page", icon=":material/favorite:")
    return p

pg = st.navigation([
    st.Page(page1, title="First page", icon="🔥"),
    st.Page(page2, title="Second page", icon=":material/favorite:"),
])
pg.run()


#20260119