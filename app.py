import streamlit as st
import pandas as pd

st.title("📊 Любими неща - класна анкета")

# Инициализация на данните
if "colors" not in st.session_state:
    st.session_state.colors = {
        "Адриан": 0,
        "Сашо": 0,
        "Ачо": 0,
        "Синан": 0,
        "Берко": 0
    }

if "sports" not in st.session_state:
    st.session_state.sports = {
        "Шестица": 0,
        "Петица": 0,
        "Четворка": 0,
        "Тройка": 0,
        "Двойка": 0
    }

st.subheader("Избери любими неща")

color = st.selectbox("Любим човек:", list(st.session_state.colors.keys()))
sport = st.selectbox("Любима храна:", list(st.session_state.sports.keys()))

if st.button("Запази избора"):
    st.session_state.colors[color] += 1
    st.session_state.sports[sport] += 1
    st.success("Добър избор!")

st.divider()

st.subheader("📈 Резултати")

# Графика за цветовете
st.write("Любими хора")
colors_df = pd.DataFrame.from_dict(
    st.session_state.colors, orient="index", columns=["Брой"]
)
st.bar_chart(colors_df)

# Графика за спортовете
st.write("Любими храни")
sports_df = pd.DataFrame.from_dict(
    st.session_state.sports, orient="index", columns=["Брой"]
)
st.bar_chart(sports_df)
