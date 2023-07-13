import streamlit as st
import pandas as pd
import numpy as np

if st.checkbox('Click Me!!'):
    st.button('Click Me!!!!')

options = st.multiselect(
    'What are your favorite colors',
    ['Green','Yellow','Red','Blue'],
    ['Yellow','Red']
)

st.write(f'選択肢:{options}')

number=st.slider('Pick a Num',0,100)
st.write(f'number:{number}')


