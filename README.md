# ✈️ AI Travel Planner Agent

An AI-powered agent that generates **personalized, day-wise travel itineraries** using Google's **Gemini `gemini-2.5-flash` model**.  
Users simply provide destination, duration, budget, travel style, and interests — and the agent produces a complete travel plan instantly.

---

## 🚀 Features

✔ Generates **full multi-day itinerary** (Morning • Afternoon • Evening)  
✔ Adjusts recommendations based on **budget & interests**  
✔ Includes **local travel tips & safety suggestions**  
✔ Provides **overview summary + day-wise plan**  
✔ Accepts inputs via **CLI or Streamlit UI**

---

## 🧠 Technology Stack

| Component | Technology |
|----------|-------------|
| Language | Python |
| AI Model | Gemini — `gemini-2.5-flash` |
| API | Google Generative AI API |
| Secure Credentials | `.env` + `python-dotenv` |
| (Optional) Frontend | Streamlit |

---

## 📌 Architecture Overview

User Inputs → Prompt Builder → Gemini 2.5 Flash Model → Itinerary Generation → Formatted Output

---

## 🛠 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/ai-travel-planner-agent.git
cd ai-travel-planner-agent
```

### 2️⃣ Create & activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
```

### 4️⃣ Add your API key
Create a .env file in the project root:
```bash
GEMINI_API_KEY=your_api_key_here
```

### ▶️ Run the Project
CLI Version
```bash
python travel_planner.py
```

Streamlit UI (Optional)
```bash
streamlit run app.py
```
