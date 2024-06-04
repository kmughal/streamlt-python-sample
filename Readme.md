# Healthcare Chatbot

This is a healthcare chatbot that can answer your queries related to health. It uses the SentenceTransformer model from the sentence_transformers library to encode questions into vectors, and the faiss library to find the most similar questions in a dataset.

## Installation

Before running the app, you need to install the required Python libraries. You can do this with pip:

```bash
pip install pandas streamlit sentence_transformers faiss-cpu numpy
```

Running the App
To run the app, use the following command:

```bash
streamlit run app.py
```

py
This will start the Streamlit server and open the app in your web browser.

Using the App
To use the app, enter your question in the sidebar and click the "Ask question" button. The app will find the most similar questions in the dataset and display them in the main area.

Dataset
The app uses a CSV file named 'data.csv' as the dataset. This file should have a column named "Question" that contains the questions.

Model
The app uses the "all-mpnet-base-v2" model from the sentence_transformers library to encode the questions into vectors. This model is downloaded automatically when you run the app for the first time.

