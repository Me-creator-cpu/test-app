import streamlit as st
import pandas as pd
import calendar
import sys

def read_csv(PATH: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(PATH)
    except:
        sys.exit('Unable to read the data, kindly verify the source and try again')

    abbr = dict(enumerate(calendar.month_abbr))
    abbr.pop(0)
    df['MONTH'] = pd.Categorical(
        df['MONTH'], categories=list(abbr.values()), ordered=True)

    return df


with st.sidebar:
    st.info('This is my first web application with streamlit')


PATH = 'https://raw.githubusercontent.com/Lamy237/hello-world/main/pay.csv'

df = read_csv(PATH)
monthly_pay_df = df.pivot_table(values='PAY', index='MONTH', columns='YEAR')

# changing back to regular df
monthly_pay_df = monthly_pay_df.reset_index().rename_axis(None, axis='columns')

st.dataframe(monthly_pay_df, use_container_width=True)