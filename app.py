import streamlit as st
import psycopg2
import pandas as pd


@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])


conn = init_connection()


@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


rows = run_query("SELECT * FROM banks")

data = pd.DataFrame(rows)
data.columns = ["bank_id", "bank_name",
                "bank_routing_number", "mortgage_lending"]
st.write("Bank_db")
st.table(data)
