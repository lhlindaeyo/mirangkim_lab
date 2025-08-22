import streamlit as st
from utils.db import get_all
"""
# db에서 데이터 구조
{
  "name": "Kim Mirang",
  "period": "2018 - 2024",
  "topic": "NLP for Education",
  "current_position": "Researcher at KAIST AI Lab"
}

"""

def show_alumni():
    st.title("🎓 Alumni")

    alumni_list = get_all("alumni")  # alumni 컬렉션에서 불러오기

    if not alumni_list:
        st.info("아직 등록된 졸업생 정보가 없습니다.")
        return

    for a in alumni_list:
        st.subheader(a.get("name", "Unknown"))
        st.write(f"📅 기간: {a.get('period', '')}")
        st.write(f"📖 연구 주제: {a.get('topic', '')}")
        if a.get("current_position"):
            st.write(f"💼 현재: {a['current_position']}")
        st.markdown("---")