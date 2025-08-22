"""
# db에서 데이터 구조
{
  "name": "Kim Mirang",
  "role": "PhD Student",
  "bio": "My research focuses on AI for education and NLP.",
  "email": "mirangkim@university.edu",
  "photo": "https://example.com/images/mirang.jpg",
  "website": "https://scholar.google.com/mirangkim",
  "join_year": 2023
}

"""
import streamlit as st
from utils.db import get_all

def show_members():
    st.title("👩‍🔬 Members")

    members = get_all("members")

    if not members:
        st.info("아직 등록된 멤버가 없습니다.")
        return

    for m in members:
        cols = st.columns([1, 3])
        with cols[0]:
            if m.get("photo"):
                st.image(m["photo"], width=120)
        with cols[1]:
            st.subheader(m.get("name", "Unknown"))
            st.write(f"🎓 {m.get('role', '')}")
            st.write(m.get("bio", ""))
            if m.get("email"):
                st.write(f"📧 {m['email']}")
            if m.get("website"):
                st.markdown(f"[🔗 Website]({m['website']})")
        st.markdown("---")
