import streamlit as st
import pandas as pd
import numpy as np

number=st.sidebar.slider('Pick a Num',0,100)
st.sidebar.write(f'number:{number}')


left_col,center_col,right_col = st.columns(2)
left_col.slider('Pick a Num in Left',0,100)
right_col.write('Right Column!!')

