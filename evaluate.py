from sklearn.metrics import classification_report

def evaluate_model(model,X_test,y_test , output_path='outputs/classification_report.txt'):
    y_pred = model.predict(X_test)
    report = classification_report(X_test,y_pred)
    with open(output_path, 'w') as f:
        f.write(report)
    return report