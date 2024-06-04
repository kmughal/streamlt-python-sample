import pandas as pd
import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

st.title("Healthcare Chatbot")
st.write("This is a healthcare chatbot that can answer your queries related to health.")
question_text = st.sidebar.text_area("Enter your question here")
ask_question = st.sidebar.button("Ask question")

if ask_question:
    st.write("You asked: ", question_text)
    f = pd.read_csv('data.csv')
    encoder = SentenceTransformer("all-mpnet-base-v2")
    vectors = encoder.encode(f["Question"])
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)

    svector = encoder.encode(question_text)
    svec = np.array(svector).reshape(1, -1)
 
    dis,r = index.search(svec, k=2)
    st.write("Your questions are similar to")
    st.table(f.iloc[r[0]])