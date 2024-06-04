import streamlit as st
from icecream import ic
from pymongo import MongoClient
from datetime import datetime

# mongo client
mongo_client = MongoClient(st.secrets["MONGO_URI"])
db = mongo_client["curator_001"]
collection = db["meals"]


# get the meals from the db
meals = collection.find({})

for meal in meals:
    ic(meal)

    st.header(f"[{meal['title']}]({meal['url']})", divider="rainbow")

    st.write(f"{meal['eaten_on'].strftime('%B %d, %Y')}")

    tag_text = ""
    for tag in meal["tags"]:
        tag_text += f":blue-background[{tag}] "

    st.markdown(tag_text)

    st.markdown(meal["summary"])

    with st.expander("Full meal"):
        st.markdown(meal["text"])
