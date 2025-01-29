import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Data Analysis')
st.write('Here is our first attempt at using data to create a table:')
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })


st.line_chart(df)