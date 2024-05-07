import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

def load_data(directory_paths):
    texts, labels = [], []
    for dialect, directory in directory_paths.items():
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read().strip()
                text = re.sub(r'\d+', '', text)  # Remove numbers
                texts.append(text)
                labels.append(dialect)
    return texts, labels


def preprocess_texts(texts):
    # Define a tokenizer function
    def tokenize(text):
        # Simple tokenization based on whitespace
        return text.split()

    # Initialize a TF-IDF Vectorizer without using stop words
    vectorizer = TfidfVectorizer(tokenizer=tokenize)
    features = vectorizer.fit_transform(texts)
    return features, vectorizer



def train_model(features, labels):
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, preds))
    print("Classification Report:\n", classification_report(y_test, preds))



# Main function to run the process
def main():
    # Define your directory paths correctly
    directory_paths = {
        # 'other': '../language_resources/dialects_mixed_txt/other_quechua/',
        'qub': '../language_resources/dialects_mixed_txt/qub',
        'quf': '../language_resources/dialects_mixed_txt/quf',
        'quh': '../language_resources/dialects_mixed_txt/quh',
        'quk': '../language_resources/dialects_mixed_txt/quk',
        'qul': '../language_resources/dialects_mixed_txt/qul',
        'qup': '../language_resources/dialects_mixed_txt/qup',
        'quw': '../language_resources/dialects_mixed_txt/quw',
        'qux': '../language_resources/dialects_mixed_txt/qux',
        'quy': '../language_resources/dialects_mixed_txt/quy',
        'quz': '../language_resources/dialects_mixed_txt/quz', 
        'qvc': '../language_resources/dialects_mixed_txt/qvc',
        'qve': '../language_resources/dialects_mixed_txt/qve',  
        'qvi': '../language_resources/dialects_mixed_txt/qvi',
        'qvm': '../language_resources/dialects_mixed_txt/qvm',
        'qvn': '../language_resources/dialects_mixed_txt/qvn',
        'qvo': '../language_resources/dialects_mixed_txt/qvo',
        'qvw': '../language_resources/dialects_mixed_txt/qvw',
        'qvz': '../language_resources/dialects_mixed_txt/qvz',
        'qwh': '../language_resources/dialects_mixed_txt/qwh',
        'qxl': '../language_resources/dialects_mixed_txt/qxl',
        'qxh': '../language_resources/dialects_mixed_txt/qxh',
        'qxn': '../language_resources/dialects_mixed_txt/qxn',
        'qxo': '../language_resources/dialects_mixed_txt/qxo',
        'qxr': '../language_resources/dialects_mixed_txt/qxr'
        # 'southern': '../language_resources/dialects_mixed_txt/southern_quechua'
    }

    texts, labels = load_data(directory_paths)
    features = preprocess_texts(texts)
    train_model(features, labels)

if __name__ == '__main__':
    main()
