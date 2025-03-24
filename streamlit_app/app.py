# streamlit_app/app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("cleaned_data/maternal_vitals.csv")
df['date'] = pd.to_datetime(df['date'])

st.set_page_config(page_title="MomStar: Maternal Health App", layout="wide")

st.title("🤰 MomStar: Digital Maternal Health Companion")
st.markdown("Welcome! This app helps track key maternal health vitals using wearable data.")

# Patient selection
patients = df["patient_id"].unique()
selected_patient = st.selectbox("Choose a Patient", patients)

patient_data = df[df["patient_id"] == selected_patient].sort_values("date")

# Latest vitals display
latest = patient_data.iloc[-1]
st.subheader("📋 Latest Vitals")
st.markdown(f"""
- **Date:** {latest['date'].date()}
- **Glucose:** {latest['glucose_mg_dl']} mg/dL
- **Blood Pressure:** {latest['systolic_bp']}/{latest['diastolic_bp']} mmHg
- **Heart Rate:** {latest['heart_rate']} bpm
- **Sleep:** {latest['sleep_hours']} hours
""")

# Visualizations
st.subheader("📈 Health Trends Over Time")

fig, axs = plt.subplots(2, 2, figsize=(14, 10))

sns.lineplot(data=patient_data, x='date', y='glucose_mg_dl', ax=axs[0][0])
axs[0][0].set_title("Glucose (mg/dL)")

sns.lineplot(data=patient_data, x='date', y='systolic_bp', ax=axs[0][1])
axs[0][1].set_title("Systolic BP")

sns.lineplot(data=patient_data, x='date', y='diastolic_bp', ax=axs[1][0])
axs[1][0].set_title("Diastolic BP")

sns.lineplot(data=patient_data, x='date', y='sleep_hours', ax=axs[1][1])
axs[1][1].set_title("Sleep Hours")

for ax in axs.flat:
    ax.set_xlabel("Date")
    ax.set_ylabel("")
    ax.grid(True)

plt.tight_layout()
st.pyplot(fig)
