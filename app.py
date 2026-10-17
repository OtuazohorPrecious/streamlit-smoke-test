# app.py
import os
import streamlit as st

st.title("Smoke test")

if prompt := st.chat_input("Say something"):
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        st.markdown(f"You said: {prompt}")

# Part B: shows a button only once the database secret exists.
if os.getenv("READONLY_DB_URL") and st.button("Test database connection"):
    import psycopg
    with psycopg.connect(os.environ["READONLY_DB_URL"]) as conn, conn.cursor() as cur:
        cur.execute("SELECT count(*) FROM machines")
        st.success(f"Database reachable: {cur.fetchone()[0]} machines")
