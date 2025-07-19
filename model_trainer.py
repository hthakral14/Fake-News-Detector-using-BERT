from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os
import pandas as pd

def build_pipeline():
    return Pipeline([
        ('tfidf' ,TfidfVectorizer(max_features=5000) ),
        ('clf', LogisticRegression())
    ])

def train_save_model(df):
    from sklearn.model_selection import train_test_split

    X = df['text']
    y = df['subject']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('clf', LogisticRegression())
    ])

    pipeline.fit(X_train, y_train)

    os.makedirs('outputs', exist_ok=True)
    joblib.dump(pipeline, 'outputs/model.pkl')
    print("Model saved in outputs/model.pkl")

    return pipeline, X_test, y_test

if __name__ == "__main__":
    print("Running model trainer...")
    df = pd.read_csv('data/fake_or_real_news.csv')
    print("Data loaded:", df.shape)

    model, X_test, y_test = train_save_model(df)
    print("Done training.")
