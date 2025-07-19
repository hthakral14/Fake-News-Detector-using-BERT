import pandas as pd 
from sklearn.model_selection import train_test_split

def load_and_split_data(filepath):
    filepath=(r"C:\Users\ashish thakral\OneDrive\Desktop\fake-news-detector\data\fake_or_real_news.csv")
    df =pd.read_csv(filepath)
    df = df[['text', 'subject']] 
    df['subject'] = df['subject'].map({'REAL': 1, 'FAKE': 0})
    return train_test_split(df['text'], df['subject'], test_size=0.2, random_state=42)