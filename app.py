import streamlit as st
from icecream import ic
from pymongo import MongoClient
import datetime

# mongo client
mongo_client = MongoClient(st.secrets["MONGO_URI"])
db = mongo_client["curator_001"]
collection = db["meals"]
