import streamlit as st
import pandas as pd

# Настройка страницы
st.set_page_config(page_title="Marketing Optimizer", page_icon="🚀", layout="wide")

st.title("🚀 Marketing Unit Economics & Insights")
st.markdown("Введите свои показатели слева, чтобы найти узкие места в воронке.")

# --- SIDEBAR: ВВОД ДАННЫХ ---
st.sidebar.header("📥 Входные данные")
budget = st.sidebar.number_input("Бюджет на таргет ($)", min_value=0.0, value=1000.0)
impressions = st.sidebar.number_input("Показы", min_value=0, value=50000)
clicks = st.sidebar.number_input("Клики", min_value=0, value=1500)
leads = st.sidebar.number_input("Лиды", min_value=0, value=150)
sales = st.sidebar.number_input("Продажи", min_value=0, value=15)
avg_check = st.sidebar.number_input("Средний чек ($)", min_value=0.0, value=200.0)

# --- РАСЧЕТЫ ---
# Предотвращаем деление на ноль
ctr = (clicks / impressions) * 100 if impressions > 0 else 0
cpc = budget / clicks if clicks > 0 else 0
cpl = budget / leads if leads > 0 else 0
cac = budget / sales if sales > 0 else 0
cr_lead_to_sale = (sales / leads) * 100 if leads > 0 else 0
revenue = sales * avg_check
romi = ((revenue - budget) / budget) * 100 if budget > 0 else 0

# --- ОТОБРАЖЕНИЕ МЕТРИК ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("CAC (Стоимость клиента)", f"${cac:,.2f}")
col2.metric("CPL (Стоимость лида)", f"${cpl:,.2f}")
col3.metric("ROMI", f"{romi:,.0f}%")
col4.metric("Конверсия в продажу", f"{cr_lead_to_sale:,.1f}%")

st.divider()

# --- АНАЛИЗ УЗКИХ МЕСТ ---
st.subheader("🔍 Анализ воронки и гипотезы")

bottleneck = ""
hypothesis = ""

if ctr < 1.0:
    bottleneck = "Низкий CTR (Кликабельность)"
    hypothesis = "Ваши креативы не цепляют аудиторию. Попробуйте сменить оффер или визуальную подачу."
elif cr_lead_to_sale < 5.0:
    bottleneck = "Низкая конверсия из лида в продажу"
    hypothesis = "Проблема в отделе продаж или качестве лидов. Проверьте скрипты или настройки таргета на целевую аудиторию."
elif cac > avg_check:
    bottleneck = "Отрицательная юнит-экономика"
    hypothesis = "Привлечение стоит дороже, чем приносит клиент. Нужно либо повышать средний чек (LTV), либо радикально снижать стоимость клика."
else:
    bottleneck = "Воронка работает стабильно"
    hypothesis = "Масштабируйте бюджет, пока метрики сохраняют стабильность."

st.info(f"**Узкое место:** {bottleneck}")
st.success(f"**Гипотеза:** {hypothesis}")