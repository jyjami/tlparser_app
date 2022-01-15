import os
import traceback
import pandas
import sys
from datetime import datetime
import streamlit as st
import base64
import io

def get_details_from_log(line):

    # Lines = line.readlines()

    times = []
    for line in line[1:]:
        st.write(line)
        for i in range(len(line)-1):
            if line[i]==':' and line[i+1]!=' ':
                times.append(line[i-2:i+5])

    def timediff(x, y):
        t1 = datetime.strptime(x.upper().strip(), '%I:%M%p')
        t2 = datetime.strptime(y.upper().strip(), '%I:%M%p')
        return (t2-t1).seconds

    def number_of_hrs(times):
        total = 0
        for i in range(0,len(times)-1,2):
            try:
                total += timediff(times[i], times[i+1])
            except Exception:
                st.write('line {} has issue'.format(i+1))
        hrs = total/3600
        return hrs

    
    
    num_hrs = number_of_hrs(times)
    st.write("Total Number of hours in time logs from file : {}".format(num_hrs))
    return num_hrs


if __name__== "__main__":
    st.title("Web Application built on streamlit")
    main_bg = "image.jpg"
    main_bg_ext = "jpg"
    st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
    new_title = '<p style="font-family:sans-serif; color:white; font-size: 20px;">@streamlit</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center;">Time Log Parser App </h2>
    </div>
    """
    st.sidebar.selectbox("Credentials",("Login","sign In"))
    st.markdown(html_temp,unsafe_allow_html=True)
    file = st.file_uploader(" Upload the TimeLog file here")
    with st.expander("Description"):
        st.success("tl parser generation")
    if st.button("Generate"):
        line = str(file.read(),"utf-8")
        get_details_from_log(line)