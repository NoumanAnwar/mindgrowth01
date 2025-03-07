#streamlit
import streamlit as st

st.set_page_config(page_title="growth mindset project", project_icon="🌱")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🌠Welcome to my Growth Journey")
st.write("Embrace Challenges: View obstacles as opportunities to learn rather than as setbacks. This AI-powered app helps us build a growth mindset with reflection,challenges and achievements!")

#quote section
st.header("🌞Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts.-Winstorm")

st.header("🔒What's Your Challenge Today?")
user_input=st.text_input("Describe a challenge you're facing:")


#condition
if user_input:
    st.success(f"⌚you are facing: {user_input}. Keep pushing forward towards your goal!⌛")
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"Greet Insight! Your Reflection: {reflection}")
else:
    st.info("Reflection on past experience help you grow! Share your difficulties")

#achievements

st.header("🌼Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished")

if achievement:
    st.success(f"🌟 Amazing! You achieved:{achievement}")

else:
    st.info("Big or small, every achievement counts! Share one now😍")

#footer
st.write("- - -")
st.write("Keep believing in yourself. Growth is a journey, not a destination!⭐")
st.write("**⛔ Created by Nouman Anwar**")
