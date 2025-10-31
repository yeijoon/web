#자신이 만든 레포지토리(저장소)에 streamlit_app.py 만들고 다음 내용 복붙해서 집어넣기

import streamlit as st
import pandas as pd

# --- 1. 페이지 기본 설정 ---
st.set_page_config(
    page_title="Streamlit 마법 교실",
    page_icon="??",
    layout="wide"
)

# --- 2. 페이지 타이틀 ---
st.title("Streamlit 마법 교실 ??")
st.subheader("HTML/CSS를 활용해 멋진 효과를 만들어 봐요!")
st.markdown("---") # 구분선

# --- 3. 모든 커스텀 CSS ---
# st.markdown 내부에 <style> 태그를 사용하여 CSS를 전역으로 주입합니다.
# 학생들에게 각 CSS 클래스가 어떤 효과를 주는지 설명하기 좋습니다.
st.markdown("""
<style>
/* 섹션 1: 움직이는 그라데이션 텍스트
  - background: 4가지 색상의 선형 그라데이션을 만듭니다.
  - background-size: 배경을 4배 키워서 움직일 공간을 만듭니다.
  - background-clip: text; : 배경을 텍스트 모양으로 잘라냅니다.
  - text-fill-color: transparent; : 텍스트 색을 투명하게 만들어 배경 그라데이션이 보이게 합니다.
  - animation: 'gradient' 애니메이션을 5초 동안 무한 반복합니다.
*/
@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.gradient-text {
    font-size: 40px;
    font-weight: bold;
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a
