import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

# 📌 설문 질문 리스트 (감정 분석 관련)
questions = [
    "지금 기분이 전반적으로 즐겁다.",
    "오늘 하루 동안 웃는 일이 많았다.",
    "주변 사람들과 긍정적인 관계를 유지하고 있다.",
    "이유 없이 불안하거나 초조한 기분이 든다.",
    "집중이 잘되지 않거나 산만하다.",
    "몸이 긴장되어 있거나 근육이 뻣뻣하게 느껴진다.",
    "몸이 무겁거나 쉽게 피로감을 느낀다.",
    "최근 고민이 많고 압박감을 느낀다.",
    "쉬어도 피곤함이 해소되지 않는다.",
    "평소에 좋아하던 일에도 흥미가 없다."
]

# 📌 음식 추천 함수
def recommend_food(taste):
    food_options = {
        "단맛": ["초콜릿", "바나나", "고구마"],
        "매운맛": ["떡볶이", "김치볶음밥"],
        "짠맛": ["김치찌개", "감자칩"],
        "신맛": ["레몬차", "요거트"]
    }
    return random.choice(food_options[taste])

# 🌟 Streamlit UI 시작
st.title("📊 감정 진단 설문조사")
st.write("아래 질문에 1~5로 응답해주세요. (1: 전혀 아니다, 5: 매우 그렇다)")

# 📌 설문 응답 저장 리스트
responses = []

# ✅ 사용자 설문 응답 받기
for i, question in enumerate(questions):
    score = st.slider(f"Q{i+1}. {question}", 1, 5, 3)
    responses.append(score)

# ✅ 설문 완료 버튼
if st.button("📩 설문 제출"):
    # 🔹 결과 분석
    total_score = sum(responses)

    if total_score >= 40:
        emotion_state = "전반적으로 긍정적인 감정 상태 😊"
        recommended_taste = "신맛"
    elif total_score >= 30:
        emotion_state = "일반적으로 안정적인 상태 🙂"
        recommended_taste = "단맛"
    elif total_score >= 20:
        emotion_state = "약간의 스트레스나 피로가 있음 😐"
        recommended_taste = "짠맛"
    else:
        emotion_state = "감정 기복이 크거나 스트레스·우울 상태 😞"
        recommended_taste = "매운맛"

    recommended_food = recommend_food(recommended_taste)

    # 🔹 결과 출력
    st.subheader("📊 감정 진단 결과")
    st.write(f"총점: {total_score}점")
    st.write(f"현재 상태: {emotion_state}")
    st.write(f"🍽️ 추천 맛: **{recommended_taste}**")
    st.write(f"🥘 추천 음식: **{recommended_food}**")

    # 🔹 설문 결과 데이터 저장
    df = pd.DataFrame([responses], columns=[f"Q{i+1}" for i in range(len(questions))])
    df.to_csv("survey_results.csv", mode="a", header=False, index=False)

    # 🔹 응답 시각화 (막대 그래프)
    st.subheader("📊 응답 분포")
    fig, ax = plt.subplots()
    ax.bar([f"Q{i+1}" for i in range(len(questions))], responses, color="royalblue")
    ax.set_ylim(0, 5)
    st.pyplot(fig)

    st.success("✅ 설문이 제출되었습니다!")
