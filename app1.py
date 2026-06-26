import streamlit as st

from utils.theme import load_css

st.set_page_config(
    page_title="F1 Winner Predictor",
    page_icon="🏎️",
    layout="wide"
)

load_css()

st.markdown(
    """
    <div class='main-title'>
        🏎️ Formula 1 Winner Predictor
    </div>

    <div class='subtitle'>
        Machine Learning Powered Race Predictions
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([2,1])

with col1:

    st.markdown(
        """
        <div class='glass-card'>
        <h2>Predict Future Grand Prix Winners</h2>

        Analyze race outcomes using historical
        Formula 1 race data, driver performance,
        constructor strength and machine learning.
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.image(
        "assets/f1_logo.png",
        use_container_width=True
    )

st.markdown("")

st.info(
    "⬅ Select 'Next Race Winner' from the sidebar."
)