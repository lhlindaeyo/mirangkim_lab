"""
# db에서 데이터 구조
{
  "title": "~~~~",
  "members": ["kim", "lee"],
  "description": "Using ML for ~~",
  "link": "https://github.com/finance-project"
}
"""

import streamlit as st
from utils.db import get_all

def show_projects():
    st.title("🚀 Projects")

    projects = get_all("projects")  # projects 컬렉션에서 불러오기

    if not projects:
        st.info("아직 등록된 프로젝트가 없습니다.")
        return

    for p in projects:
        st.subheader(p.get("title", "Untitled"))
        st.write(f"👥 팀원: {', '.join(p.get('members', []))}")
        st.write(f"📝 설명: {p.get('description', '')}")
        if p.get("link"):
            st.markdown(f"[🔗 링크]({p['link']})")
        st.markdown("---")
