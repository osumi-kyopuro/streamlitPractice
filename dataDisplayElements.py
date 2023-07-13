import streamlit as st
import pandas as pd
st.title('Smaple App')

df=pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[-1,-2,-3,-4]
})

st.dataframe(df.style.highlight_max(axis=1))

st.json({
    'data':{
        'name':'abc',
        'age':'23'
    }
})