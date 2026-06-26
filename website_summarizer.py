import streamlit as st
import requests

st.set_page_config(page_title="AI Web Summarizer", page_icon="📰", layout="centered")

st.title("📰 :rainbow[Web Article Summarizer]")
st.markdown("Paste any website URL link below to instantly generate a concise AI summary.")

target_url = st.text_input("Enter Web Article URL:", placeholder="https://example.com")

if st.button("Generate Summary"):
    if not target_url.strip():
        st.error("Please enter a valid website link first.")
    else:
        with st.spinner("Scraping webpage text and analyzing content..."):
            try:
                backend_url = "http://127.0.0.1:8000/summarize"
                payload = {"url": target_url}
                response = requests.get(url=backend_url, params=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    summary_text = data["summary"]
                    st.success("Summary Generated Successfully!")
                    st.write(summary_text)
                    st.balloons()
                else:
                    st.error(f"Backend Server Error (Status {response.status_code})")
            except Exception as e:
                st.error(f"Failed to communicate with your FastAPI Cloud Backend: {e}")
