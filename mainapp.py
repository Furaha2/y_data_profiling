import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
from ydata_profiling import ProfileReport

st.title("Welcome Data Profiling")
data = st.file_uploader("Choose File only csv/excel")

if data is not None:
    file_extension = data.name.split(".")[-1].lower()

    if file_extension == "csv":
        data1 = pd.read_csv(data)
    elif file_extension in ["xls","xlsx"]:
        data1 = pd.read_excel(data)
    else:
        st.write("Error:Unsupported file format")
        data1=None
        
    if data1 is not None and not data1.empty:
        ok = st.button("Generate Report")
        
        if ok:
            profile = ProfileReport(data1, title="Pandas Profiling Report")
            with st.spinner("Genrating Report....\nplease wait...."):
                st.write("## Report")
                st.components.v1.html(profile.to_html(), width=1000, height=1200, scrolling=True)    
    else:
        st.write("Please upload excel or CSV format file")
