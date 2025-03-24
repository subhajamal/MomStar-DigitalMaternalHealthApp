# 🤰 MomStar: Digital Maternal Health App

**MomStar** is a digital maternal health companion app designed to improve pregnancy outcomes by integrating wearable technology, real-time monitoring, and personalized support for expectant mothers — especially in underserved communities.

> ✨ Built with Streamlit, AI tips from OpenAI, and a wearable-style vitals dataset

---

## 📱 App Preview

| MedStar Integration | MomStar Dashboard | Patient Selector | Exit Survey |
|---------------------|-------------------|------------------|-------------|
| ![MedStar](screenshots/screen1.png) | ![Dashboard](screenshots/screen2.png) | ![Select](screenshots/screen3.png) | ![Survey]|

---

## 💡 Features

| Feature | Description |
|--------|-------------|
| 🔍 Real-time Monitoring | Track glucose, blood pressure, sleep, and more from simulated wearables |
| ⚠️ Alerts | Automatically flags high glucose or BP levels in red |
| 🧠 AI Health Tips | GPT-3.5-powered health coaching using LangChain + OpenAI |
| 🧑‍⚕️ Multi-Patient Dashboard | Compare glucose trends across all patients |
| 📱 Mobile-ready UI | Streamlit layout styled for mobile use |
| 📊 EDA Notebook | Cleaned, visualized wearable health data in a Jupyter notebook |

---

## 🗂️ Project Structure
MomStar-DigitalMaternalHealthApp/ │ ├── streamlit_app/ │ └── app.py # Main Streamlit application │ ├── cleaned_data/ │ └── maternal_vitals.csv # Simulated wearable health data │ ├── notebooks/ │ └── EDA_vitals_analysis_FULL.ipynb # Data analysis & visualization │ ├── screenshots/ │ └── screen1.png, screen2.png, ... # App UI screenshots │ ├── surveys/ │ └── entry_survey.png, exit_survey.png (or CSVs) │ ├── requirements.txt # Required Python packages └── README.md


---

## 📊 Dataset (Simulated)

**`maternal_vitals.csv`** includes:
- `patient_id`
- `date`
- `glucose_mg_dl`
- `systolic_bp`, `diastolic_bp`
- `heart_rate`
- `sleep_hours`

---

## 🔍 Exploratory Analysis

See full EDA in [`EDA_vitals_analysis_FULL.ipynb`](notebooks/EDA_vitals_analysis_FULL.ipynb):

- 📈 Glucose trends over time
- 📊 Sleep patterns and BP tracking
- 👩‍🍼 Patient-wise comparisons

---

## 🚀 Run the App

### 
1. Clone the repo
git clone https://github.com/subhajamal/MomStar-DigitalMaternalHealthApp.git
cd MomStar-DigitalMaternalHealthApp
2. Install dependencies
pip install -r requirements.txt
3. Set OpenAI API key
Create a .streamlit/secrets.toml file:


OPENAI_API_KEY = "your-openai-key-here"
4. Run the app
streamlit run streamlit_app/app.py
📝 Surveys
Surveys included in /surveys/ help capture:

Entry insights: prior experience with pregnancy apps

Exit reflections: satisfaction, comfort using wearables, improvement suggestions

🧠 Tech Stack
Streamlit – for building a rapid front-end

LangChain + OpenAI – AI-powered tips

Pandas, Seaborn, Matplotlib – for data analysis

Python – for backend logic & pipelines

📈 Future Work
🩺 Integrate real-time FHIR API for wearable syncing

🔔 Push notifications for high-risk alerts

🌐 Deploy via Streamlit Cloud or Hugging Face Spaces




