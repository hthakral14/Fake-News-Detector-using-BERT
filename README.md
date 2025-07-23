This project is a Fake News Detection web application built using Python, Hugging Face Transformers, and Streamlit. The app takes a news title and article body as input and predicts whether the news is FAKE or REAL, using a pre-trained BERT model.

Features
Real-time fake news classification using a BERT-based model.

Simple and clean user interface made with Streamlit.

Displays confidence score for each prediction.

Uses the Hugging Face model: jy46604790/Fake-News-Bert-Detect.

Tech Stack
Python

Transformers by Hugging Face

Streamlit

Torch

Installation
Clone the repository
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector
Create and activate virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # macOS/Linux
Install required libraries
pip install -r requirements.txt
Or manually:
pip install streamlit transformers torch
How to Run
To start the Streamlit app, run:
streamlit run app.py
Usage
Enter the news title.

Paste the news article body.

Click on the "Check" button.

The app will show whether the news is FAKE or REAL along with a confidence score.

Example
Input Title:
Russia warns NATO deterrence plan risks triggering World War III
Input Body:
Russian officials claim that NATO’s new Baltic strategy could escalate tensions dramatically.
Output:

Prediction: REAL
Confidence: 0.95
Folder Structure

fake-news-detector/
├── app.py              # Streamlit frontend and backend
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies

Model Info
The project uses a pre-trained BERT model from Hugging Face:
https://huggingface.co/jy46604790/Fake-News-Bert-Detect

Author
Himanshi
GitHub: hthakral14

License
This project is licensed under the MIT License.
