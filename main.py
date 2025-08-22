import streamlit as st
from streamlit_option_menu import option_menu
from pages import admin, alumni, projects, members, home

st.set_page_config(page_title="Our Lab", page_icon="🔬", layout="wide")

def main():
    # 사이드바 네비게이션
    with st.sidebar:
        selected = option_menu(
            "Navigation",
            ["Home", "Projects", "Members", "Alumni", "Admin"],
            icons=["house", "book", "rocket", "people", "lock"],
            menu_icon="cast",
            default_index=0,
        )

    if selected == "Home":
        home.show_home()

    elif selected == "Members":
        members.show_members()

    elif selected == "Projects":
        projects.show_projects()

    elif selected == "Alumni":
        alumni.show_alumni()

    elif selected == "Admin":
        admin.show_admin()

if __name__ == "__main__":
    main()
