import streamlit as st

st.set_page_config(page_title="Project LOOP")
st.title("Project LOOP - AI Feedback Intelligence")
st.write("Zudio Internship - Month 1 Project")

feedback = st.text_area("Customer Feedback:", "I love this product")

if st.button("Analyze Feedback"):
    text = feedback.lower()
    if "love" in text or "good" in text or "best" in text:
        st.success("Sentiment: Positive")
    elif "bad" in text or "worst" in text:
        st.error("Sentiment: Negative")
    else:
        st.info("Sentiment: Neutral")
    st.balloons()

st.write("By Krishnaji00")
