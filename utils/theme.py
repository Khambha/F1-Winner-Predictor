import streamlit as st
import base64


def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(
            f.read()
        ).decode()


def load_css():

    bg = get_base64(
        "assets/background.jpg"
    )

    st.markdown(
        f"""
        <style>

        .stApp {{
            background:
            linear-gradient(
                rgba(0,0,0,0.82),
                rgba(0,0,0,0.94)
            ),
            url("data:image/jpg;base64,{bg}");

            background-size:cover;
            background-position:center;
            background-attachment:fixed;
        }}

        section[data-testid="stSidebar"] {{
            background:#0a0a0a;
        }}

        h1,h2,h3,h4,h5 {{
            color:white !important;
        }}

        div[data-testid="stMetric"] {{

            background:
            rgba(255,255,255,.06);

            border:
            1px solid rgba(
                255,255,255,.08
            );

            border-radius:18px;

            padding:15px;
        }}

        .stProgress > div > div > div {{
            background:#ff1801;
        }}

        .leaderboard-row {{

            background:
            rgba(255,255,255,.05);

            border-radius:14px;

            padding:12px;

            margin-bottom:8px;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )