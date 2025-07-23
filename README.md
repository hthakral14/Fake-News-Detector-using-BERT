📰 Fake News Detection App

This is a **Fake News Detection** web application built using Python, Hugging Face Transformers, and Streamlit. The app takes a news **title** and **article body** as input and predicts whether the news is **FAKE** or **REAL**, using a pre-trained **BERT** model.

---

## 🚀 Features

- 🔍 Real-time fake news classification using a BERT-based model.
- 🧠 Confidence score shown with each prediction.
- 🧼 Simple and clean UI built with Streamlit.
- 🤖 Uses Hugging Face model: [`jy46604790/Fake-News-Bert-Detect`](https://huggingface.co/jy46604790/Fake-News-Bert-Detect)

---

## 🧰 Tech Stack

- **Python 3**
- **Transformers** by Hugging Face
- **Streamlit**
- **Torch (PyTorch)**

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/hthakral14/fake-news-detector.git
cd fake-news-detector
📝 Usage
Enter the news title

Paste the news body

Click on the "Check" button

View the result: whether it’s FAKE or REAL along with a confidence score

✅ Example
Input Title:
Russia warns NATO deterrence plan risks triggering World War III

Input Body:
Russian officials claim that NATO’s new Baltic strategy could escalate tensions dramatically.

Output:

makefile
Copy
Edit
Prediction: REAL  
Confidence: 0.95
📁 Folder Structure
bash
Copy
Edit
fake-news-detector/
├── app.py              # Streamlit frontend and backend
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
🤖 Model Information
This app uses the following Hugging Face model:
🔗 jy46604790/Fake-News-Bert-Detect

👩‍💻 Author
Himanshi Thakral
GitHub: @hthakral14

📄 License
This project is licensed under the MIT License.