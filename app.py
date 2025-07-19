import streamlit as st
from transformers import pipeline

# Load model
@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="jy46604790/Fake-News-Bert-Detect",
        tokenizer="jy46604790/Fake-News-Bert-Detect"
    )

model = load_model()

# Page config
st.set_page_config(page_title="Fake News Detection", layout="centered")

# Custom CSS Styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 36px;
            color: #1f4e79;
            margin-bottom: 5px;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #444444;
            margin-bottom: 30px;
        }
        .badge-fake {
            background-color: #e74c3c;
            color: white;
            padding: 5px 12px;
            border-radius: 5px;
            font-weight: bold;
        }
        .badge-real {
            background-color: #2ecc71;
            color: white;
            padding: 5px 12px;
            border-radius: 5px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'> Fake News Detector</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Detect whether a news article is Real or Fake using BERT</div>", unsafe_allow_html=True)

# Input fields
title = st.text_input("Title")
body = st.text_area("Article Body", height=200)
text = f"{title.strip()}\n\n{body.strip()}"

# Prediction button
if st.button(" Check"):
    if not text.strip():
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing..."):
            result = model(text)[0]
            label = result["label"]
            score = round(result["score"], 2)

            if label == "LABEL_0":
                st.markdown(f"<div class='badge-fake'>FAKE NEWS</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='badge-real'>REAL NEWS</div>", unsafe_allow_html=True)

            st.write(f"**Confidence Score:** `{score}`")
            st.progress(score)

            with st.expander(" Explanation"):
                if label == "LABEL_0":
                    st.warning(" The model predicts this content as possibly *fake*. Please verify the information from trusted sources.")
                else:
                    st.success("The content appears to be real. But always double-check major claims.")

# Footer
st.markdown("---")
st.markdown("<center><small>Made with 🤖 using Hugging Face & Streamlit</small></center>", unsafe_allow_html=True)
