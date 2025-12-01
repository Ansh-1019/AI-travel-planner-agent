import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME = "gemini-2.5-flash"

def build_prompt(destination, days, budget, traveller_type, interests, style):
    system_instructions = """
You are an expert travel planner.

Given:
- Destination
- Trip dates OR number of days
- Budget
- Traveller type
- Interests

You must return a detailed, day-wise itinerary.

Rules:
- Start with a short overview paragraph.
- Then create a section: "Summary of Trip".
- Then create: "Day-wise Itinerary".
  For each day include: Morning, Afternoon, Evening.
- Mention approximate budget level per day: (Low / Medium / High).
- End with a "Tips & Recommendations" section.
- Respond in clear bullet points and headings.
"""
    user_message = f"""
User Details:
Destination: {destination}
Number of Days: {days}
Budget: {budget}
Traveller Type: {traveller_type}
Interests: {interests}
Travel Style: {style}

Now create a personalized itinerary.
"""
    return system_instructions + "\n\n" + user_message

def generate_itinerary(destination, days, budget, traveller_type, interests, style):
    prompt = build_prompt(destination, days, budget, traveller_type, interests, style)
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("✈️ AI Travel Planner Agent")
st.write("Get a personalized travel itinerary using Generative AI.")

with st.form("travel_form"):
    destination = st.text_input("Destination", "Manali, India")
    days = st.number_input("Number of Days", min_value=1, max_value=30, value=4)
    budget = st.selectbox("Budget", ["Low", "Medium", "High"])
    traveller_type = st.selectbox("Traveller Type", ["Solo", "Couple", "Family", "Friends"])
    interests = st.text_area("Interests", "Nature, mountains, cafes, light adventure")
    style = st.selectbox("Travel Style", ["Relaxed", "Balanced", "Packed/Adventurous"])
    
    submitted = st.form_submit_button("Generate Itinerary")

if submitted:
    with st.spinner("Generating your itinerary..."):
        itinerary = generate_itinerary(destination, days, budget, traveller_type, interests, style)
    st.subheader("🗺 Your Personalized Itinerary")
    st.markdown(itinerary)
