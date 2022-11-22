from text_process import *
from model_eval import *
import streamlit as st
from io import StringIO 
st.title('Detección de metáforas')
st.subheader('Inserte el par adjetivo sustantivo para saber si es metáfora')
text = st.text_input('escriba el texto aquí')
if text is not None:
    translated=translate(text)
    prediction = predict([embeddings(translated.split())])[0][1]
    st.write(prediction[2])
    st.write(prediction[3])
st.subheader('Inserte el archivo con pares del helper')
uploaded_file = st.file_uploader("seleccione un archivo")
if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data=uploaded_file.getvalue().decode("utf-8").split('\n')
    for line in string_data:
        sentence, mets = line.split('$')
        mets = mets.split('|')
        st.write(sentence+'\t')
        for text in mets:
            st.write(text)
            translated=translate(text)
            prediction = predict([embeddings(translated.split())])[0][1]
            st.write(prediction[2])
            st.write(prediction[3])
                
#overall pipeline
# while True:
#     text = input('a')
#     translated=translate(text)
#     a = predict([embeddings(translated.split())])
#     print(text,translated,a)