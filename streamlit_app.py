import os
import streamlit as st
from functions import *
# openai.api_key = "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"


def main():
    st.set_page_config(page_title="GPT PDF Özetleyici")
    st.title("GPT PDF Özetleyici")
    api_key_input = st.text_input("Open AI API Key'inizi buraya yazınız, sonrasında Enter'a basınız:")
    uploaded_file = st.file_uploader("Bir PDF dosyası seçiniz", type="pdf")
    if uploaded_file is not None:
        if st.button("PDF'i taratın"):
            save_uploaded_file(uploaded_file)
            st.write("Lütfen PDF okunurken bekleyin.")
            learn_pdf(uploaded_file.name)
            st.write("PDF'iniz taratıldı. Lütfen mesajınızı giriniz")
            os.remove(uploaded_file.name)
    user_input = st.text_input("Mesajınızı girin, sonrasında Enter'a basın:")
    openai.api_key = api_key_input


    if st.button("Yanıt alın"):
        st.write("Sorunuz:", user_input)
        response = Answer_from_documents(user_input)
        st.write("GPT-3.5-Turbo Yanıtı: "+response)


if __name__ == "__main__":

    main()
