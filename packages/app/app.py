import streamlit as st 


pages = [
    st.Page("pages/home_page.py", title="Home", icon="🏠"),
    st.Page("pages/predictor_page.py", title="Predictor", icon="👀"), 
    st.Page("pages/performance_page.py", title="Performance", icon="📊")]

pg = st.navigation(pages=pages)

st.set_page_config(page_title="Player Sentiment Prediction", layout="wide", page_icon="🎃")
pg.run()

