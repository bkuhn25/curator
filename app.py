import streamlit as st
import requests
from pydantic import BaseModel
import marvin
from icecream import ic


class SourceData(BaseModel):
    title: str
    summary: str
    tags: list[str]


@marvin.fn
def analyze_source_data(source_text: str) -> SourceData:
    """
    Analyze the 'source_text' and return the following information:
    'title' of the information
    a succint 'summary' to give a potential reader the key points and high level overview of what the 'source_text' contains (keep it rich but brief)
    accurate and helpful 'tags' to categorize the 'source_text'. Max of 7 tags, but try to use at least 5.
    """


link = st.text_input("Article URL", placeholder="Enter URL here big guy")

if st.button("Analyzazer the link"):

    with st.spinner("Extracting text..."):
        st.write("Link:", link)

        # extract text using Jina AI
        extracted_text_res = requests.get(f"https://r.jina.ai/{link}")

        if extracted_text_res.status_code != 200:
            st.write(extracted_text_res.status_code)
            st.write(extracted_text_res.text)

        st.write("Here is the text from the link yo")
        st.write(extracted_text_res.text)

    with st.spinner("Analyzing..."):
        analysis = analyze_source_data(extracted_text_res.text)

        st.write("Here is the analysis")
        st.write(analysis)

    with st.spinner("Saving to db..."):

        # save to db

        st.write("Saved to db")
