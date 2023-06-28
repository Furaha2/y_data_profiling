import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
from ydata_profiling import ProfileReport

st.title("Welcome Data Profiling")
data = st.file_uploader("Choose File (only .csv/.excel)")

if data is not None:
    file_extension = data.name.split('.')[-1].lower()  # no need to lower since we are checking for exact string match

    if file_extension == "csv":
        data1 = pd.read_csv(data)
    elif file_extension in ["xls", "xlsx"]:
        data1 = pd.read_excel(data)
    else:
        st.write("Error: Unsupported file format.")
        data1 = None

    if data1 is not None and not data1.Empty:   # check for empty dataframe instead of len(df) == 0
        st.write("\nData profiling report generated successfully\n")
        st.write("===========================================\n")
        ok = st.button("View Report")
        if ok:
            profile = ProfileReport(data1, title="Pandas Data Profiling Report")
            with st.spinner("Generating Report...\nPlease wait..."):
                html = profile.to_html().replace('\n', '<br>').replace('\t', '&nbsp; ')
                st.write('<div id="myDiv"></div>' + html)
        else:
            st.write("You have to click on button view the report.\n" \
                      "To run again just drag the button to top of page")
else:
    st.warning("No valid Excel sheet found in the uploaded file")
    st.input("\nDo you want exit? Press Enter key or type Y or Yes followed by enter to continue otherwise press Esc or No or any other key to exit...")
    res = input()
    if res.lower() in ['y', 'yes']:
        st.close()
    else:
        st.text("Exiting without generating the report")
