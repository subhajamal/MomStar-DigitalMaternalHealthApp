# streamlit_app/app.py

# --- IMPORTS ---
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from langchain_openai import ChatOpenAI

# --- SET PAGE CONFIG ---
# Mobile-friendly centered layout with custom title
st.set_page_config(page_title="MomStar: Maternal Health App", layout="wide")

# --- TITLE & HEADER ---
st.title("🤰 MomStar: Digital Maternal Health Companion")
st.markdown("A wearable-powered dashboard for tracking pregnancy health in real time.")

# --- LOAD DATA ---
# Read simulated wearable data from cleaned CSV
df = pd.read_csv("cleaned_data/maternal_vitals.csv")
df['date'] = pd.to_datetime(df['date'])

# --- SIDEBAR: AI HEALTH TIP ---
st.sidebar.header("🧠 AI Health Tip")

# Generate a friendly, personalized health tip using latest patient data
try:
    llm = ChatOpenAI(openai_api_key=st.secrets["OPENAI_API_KEY"])
    latest_all = df.sort_values("date").groupby("patient_id").last().reset_index()
    any_latest = latest_all.iloc[0]  # Use any recent patient to generate a tip
    prompt = f"""
    Based on this patient's vitals: glucose = {any_latest['glucose_mg_dl']}, systolic BP = {any_latest['systolic_bp']}, 
    diastolic BP = {any_latest['diastolic_bp']}, heart rate = {any_latest['heart_rate']}, 
    sleep = {any_latest['sleep_hours']}, give a warm, friendly health tip for a pregnant patient.
    """
    tip = llm.invoke(prompt)
    st.sidebar.success(tip)
except Exception as e:
    st.sidebar.warning("Could not load health tip. Check your OpenAI API key in secrets.")

# --- PATIENT SELECTION ---
st.subheader("🩺 Select Patient")
patients = df["patient_id"].unique()
selected_patient = st.selectbox("Choose a Patient", patients)
patient_data = df[df["patient_id"] == selected_patient].sort_values("date")
latest = patient_data.iloc[-1]  # Most recent entry

# --- ALERT FUNCTION ---
def alert_text(label, value, threshold, unit):
    """Display alert if value exceeds threshold."""
    if value > threshold:
        return f"❗ **{label}:** `{value} {unit}` — ⚠️ High!"
    return f"**{label}:** `{value} {unit}`"

# --- DISPLAY LATEST VITALS + ALERTS ---
st.subheader("📋 Latest Vitals with Alerts")
st.markdown(f"""
- **Date:** `{latest['date'].date()}`
- {alert_text('Glucose', latest['glucose_mg_dl'], 140, 'mg/dL')}
- {alert_text('Systolic BP', latest['systolic_bp'], 130, 'mmHg')}
- {alert_text('Diastolic BP', latest['diastolic_bp'], 85, 'mmHg')}
- **Heart Rate:** `{latest['heart_rate']} bpm`
- **Sleep Hours:** `{latest['sleep_hours']} hrs`
""")

# --- VITAL TRENDS CHARTS ---
st.subheader("📈 Health Trends Over Time")

# First row: glucose and sleep
col1, col2 = st.columns(2)

with col1:
    st.markdown("**🩸 Glucose Over Time**")
    fig, ax = plt.subplots()
    sns.lineplot(data=patient_data, x="date", y="glucose_mg_dl", ax=ax)
    ax.set_ylabel("Glucose (mg/dL)")
    ax.grid(True)
    st.pyplot(fig)

with col2:
    st.markdown("**😴 Sleep Hours Over Time**")
    fig, ax = plt.subplots()
    sns.lineplot(data=patient_data, x="date", y="sleep_hours", ax=ax)
    ax.set_ylabel("Sleep Hours")
    ax.grid(True)
    st.pyplot(fig)

# Second row: blood pressure
col3, col4 = st.columns(2)

with col3:
    st.markdown("**🫀 Systolic BP Over Time**")
    fig, ax = plt.subplots()
    sns.lineplot(data=patient_data, x="date", y="systolic_bp", ax=ax)
    ax.set_ylabel("Systolic BP (mmHg)")
    ax.grid(True)
    st.pyplot(fig)

with col4:
    st.markdown("**🫀 Diastolic BP Over Time**")
    fig, ax = plt.subplots()
    sns.lineplot(data=patient_data, x="date", y="diastolic_bp", ax=ax)
    ax.set_ylabel("Diastolic BP (mmHg)")
    ax.grid(True)
    st.pyplot(fig)

# --- MULTI-PATIENT COMPARISON ---
st.subheader("🧑‍⚕️ Compare Glucose Trends Across Patients (Last 30 Days)")
compare_df = df[df["date"] > df["date"].max() - pd.Timedelta(days=30)]

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=compare_df, x="date", y="glucose_mg_dl", hue="patient_id", ax=ax)
ax.set_title("Glucose Comparison by Patient")
ax.set_ylabel("Glucose (mg/dL)")
ax.grid(True)
st.pyplot(fig)

# --- FOOTER ---
st.caption("📊 Built with Streamlit | 🤖 AI tips powered by OpenAI + LangChain")

