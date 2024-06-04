import streamlit as st
import requests

link = st.text_input("Article URL", placeholder="Enter URL here big guy")

if st.button("Analyzazer the link"):

    # show loading modal
    with st.spinner("Analyzerzing..."):
        st.write("Link:", link)

        # extract text using Jina AI
        extracted_text_res = requests.get("https://r.jina.ai/https://example.com")

        if extracted_text_res.status_code != 200:
            st.write(extracted_text_res.status_code)
            st.write(extracted_text_res.text)

        st.write("Here is the text from the link yo")
        st.write(extracted_text_res.text)

        # summarize using open ai

        # tag using open ai

        # extract title

        # save to db
