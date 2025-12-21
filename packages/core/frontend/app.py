import streamlit as st
import pandas as pd
import joblib
import spacy
import re
import nltk
from nltk.corpus import stopwords

# streamlit: python scripts -> websites
# pandas: data manipulation
# joblib: saves Python objects to disc, loads them back (used for model)
# spacy: NLP library
# re: regex
# nltk: Natural Language Toolkit -> used for stopwords

@st.cache_resource
def load_assets():
    # English language model
    try:
        nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])
    except OSError:
        from spacy.cli import download
        download("en_core_web_sm")
        nlp = spacy.load("en_core_web_sm", disable=['parser,' 'ner'])
    # load stopwords
    nltk.download('stopwords', quiet=True)
    stop_words= set(stopwords.words('english'))
    custom_stopwords = {'game', 'play', 'played', 'hour', 'time', 'steam'}
    stop_words.update(custom_stopwords)
    # load the svm model
    model = joblib.load('steam_sentiment_model.pkl')
    return nlp, stop_words, model

nlp, stop_words, model = load_assets()

def preprocess_text(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    doc = nlp(text)
    cleaned_tokens = []
    for token in doc:
        if token.text not in stop_words and not token.is_space:
            cleaned_tokens.append(token.lemma_)
    return " ".join(cleaned_tokens)

st.title("Steam Review Predictor")
st.write("Enter a review: ")
user_review = st.text_area("Enter a review: ", height=150, placeholder="Example: This game is absolute trash...")
with st.expander("Adjust Author Stats (Optional)"):
    st.write("The model was trained on these stats. Averages will be used if you don't change them.")
    col1, col2 = st.columns(2)
    with col1:
        playtime = st.number_input("Playtime (mins): ", value=642.0)
        num_games = st.number_input("Games Owned: ", value=48)
        num_reviews = st.number_input("Number of Reviews: ", value=14)
    with col2:
        votes_funny = st.number_input("Votes Funny: ", value=0)
        weighted_score = st.slider("Weighted Vote Score: ", 0.0, 1.0, 0.85)

    steam_purchase = st.checkbox("Purchased on Steam?", value=False)
    received_free = st.checkbox("Received Item for Free?", value=False)
    early_access = st.checkbox("Written in Early Access?", value=False)

if st.button("Analyze Sentiment"):
    if not user_review.strip():
        st.warning("Write a review first!")
    else:
        cleaned_text = preprocess_text(user_review)
        input_data = pd.DataFrame({
            'cleaned_review': [cleaned_text],
            'author_playtime_at_review': [playtime],
            'author_num_games_owned': [num_games],
            'author_num_reviews': [num_reviews],
            'votes_funny': [votes_funny],
            'weighted_vote_score': [weighted_score],
            'steam_purchase': [1 if steam_purchase else 0],
            'received_for_free': [1 if received_free else 0],
            'written_during_early_access': [1 if early_access else 0] 
        })
    try:
        prediction = model.predict(input_data)[0]
        confidence = model.decision_function(input_data)[0]
        st.subheader("Prediction: ")
        if prediction == 1:
            st.success(f"Positive Review")
            st.caption(f"Confidence Score: {confidence}")
        else:
            st.error(f"Negative Review")
            st.caption(f"Confidence Score: {confidence}")
    except Exception as e:
        st.error("An error occured: {e}")