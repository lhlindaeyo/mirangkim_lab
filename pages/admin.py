import streamlit as st
from utils.db import insert_data

def show_admin():
    st.title("🔑 Admin Mode")

    st.subheader("Add Teaching")
    title = st.text_input("Title")
    semester = st.text_input("Semester")
    desc = st.text_area("Description")
    link = st.text_input("Link")

    if st.button("Save Teaching"):
        insert_data("teaching", {
            "title": title,
            "semester": semester,
            "description": desc,
            "link": link
        })
        st.success("Saved!")
