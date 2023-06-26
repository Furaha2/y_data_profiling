import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
from ydata_profiling import ProfileReport

st.title("Welcome Data Profiling")
data = st.file_uploader("Choose File")

if data is not None:
    file_extension = data.name.split(".")[-1].lower()

    if file_extension == "csv":
        data1 = pd.read_csv(data)
    else:
        data1 = pd.read_excel(data)


    ok = st.button("Generate Report")

    if ok:
        profile = ProfileReport(data1, title="Pandas Profiling Report")
        with st.spinner("Genrating Report...."):
            st.write("## Report")
            st.components.v1.html(profile.to_html(), width=1000, height=1200, scrolling=True)    
            
        