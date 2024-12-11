import streamlit as st
import subprocess
import os
import platform

# Streamlit 페이지 설정
st.set_page_config(page_title="TALA Game", layout="centered")

# 페이지 타이틀
st.title("🎮 TALA Game - Start the Game 🎮")

# 프로젝트 개요
st.subheader("📚 Project Overview")
st.markdown("""
- **Project Name:** TALA (The Alphabet – Loving Anaconda)  
- **Target Audience:** 어린이 (유아 및 초등학생)  
- **Goal:** 알파벳 스펠링을 배우며 스네이크 게임을 통해 자연스럽게 단어를 익히는 재미있는 게임
""")

# 게임 설명
st.subheader("🎯 게임 설명")
st.write("""
TALA는 스네이크 게임 형식을 통해 어린이들이 영단어의 스펠링을 재미있게 배우는 게임입니다.  
단어를 완성하며 반복 학습을 유도하고, 자연스럽게 영어에 대한 흥미를 유발합니다. 📖
""")

# 게임 시작 버튼
if st.button("🚀 Start Game"):
    try:
        # 운영체제에 맞는 python 명령어 설정
        python_cmd = "python3" if platform.system() != "Windows" else "python"

        # subprocess로 main.py 실행
        result = subprocess.run([python_cmd, "main.py"], cwd="src", capture_output=True, text=True)

        if result.returncode == 0:
            st.success("🎉 게임이 성공적으로 시작되었습니다! 🎉")
        else:
            st.error(f"❌ 게임 시작 중 오류가 발생했습니다.\n\n**Error Output:** {result.stderr}")
    except FileNotFoundError:
        st.error("⚠️ 'main.py' 파일을 찾을 수 없습니다. 파일이 src 폴더 안에 있는지 확인해 주세요.")
    except Exception as e:
        st.error(f"⚠️ 알 수 없는 오류가 발생했습니다: {str(e)}")

# 기능 요구 사항
st.subheader("⚙️ 기능 요구사항")
st.write("""
1. **게임 창 닫기 버튼 (❌)** : 게임 창을 종료할 수 있는 버튼  
2. **게임 소리 설정 (🔊/🔇)** : 게임 소리를 켜거나 끌 수 있는 버튼  
3. **화면 확대/축소 (🔍)** : 화면을 확대하거나 축소할 수 있는 기능  
4. **게임 설명 버튼 (ℹ️)** : 게임에 대한 간략한 설명을 제공하는 버튼  
5. **스코어와 레벨 표시 (🏆)** : 게임 진행 중 실시간 스코어와 레벨을 표시  
6. **도장판 (📒)** : 최고 스코어와 학습 진도를 기록할 수 있는 도장판  
""")
