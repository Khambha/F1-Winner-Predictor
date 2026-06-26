import os
import streamlit as st

from utils.data_loader import (
    load_predictions,
    load_races
)

from utils.race_utils import (
    get_race_predictions
)

from utils.theme import load_css


TEAM_COLORS = {
    "mercedes": "#00D2BE",
    "ferrari": "#DC0000",
    "mclaren": "#FF8700",
    "red_bull": "#1E5BC6",
    "aston_martin": "#006F62",
    "williams": "#005AFF",
    "alpine": "#0090FF",
    "haas": "#B6BABD",
    "rb": "#6692FF",
    "sauber": "#52E252"
}


st.set_page_config(
    page_title="Next Race Winner",
    page_icon="🏁",
    layout="wide"
)

load_css()

# ------------------------------------------------

c1, c2, c3 = st.columns([1,2,1])

with c2:
    st.image(
        "assets/f1_logo.png",
        width=350
    )

st.title("🏁 Formula 1 Winner Predictor")

st.caption(
    "Machine Learning Based Grand Prix Winner Prediction"
)

# ------------------------------------------------

pred_df = load_predictions()
races_df = load_races()

# ------------------------------------------------

race_lookup = {}

for _, row in races_df.iterrows():

    race_key = (
        f"{row['year']}_{row['round']}"
    )

    race_lookup[race_key] = (
        f"{row['year']} - {row['name']}"
    )

race_list = sorted(
    pred_df["race_id"].unique()
)

display_options = {
    race_lookup.get(race, race): race
    for race in race_list
}

selected_display = st.selectbox(
    "🏎️ Select Grand Prix",
    list(display_options.keys())
)

selected_race = display_options[
    selected_display
]

# ------------------------------------------------

race_df = get_race_predictions(
    selected_race,
    pred_df
)

winner = race_df.iloc[0]

podium = race_df.head(3)

top10 = race_df.head(10)

# ------------------------------------------------
# Winner Section
# ------------------------------------------------

st.divider()

st.subheader("🏆 Predicted Winner")

left, right = st.columns([1,2])

driver_img = (
    f"assets/drivers/"
    f"{winner['driver_id']}.png"
)

constructor_img = (
    f"assets/constructors/"
    f"{winner['constructor_id']}.png"
)

with left:

    if os.path.exists(driver_img):

        st.image(
            driver_img,
            use_container_width=True
        )

with right:

    c1, c2 = st.columns([3,1])

    with c1:

        st.metric(
            "Driver",
            winner["driver_id"]
            .replace("_"," ")
            .title()
        )

        st.metric(
            "Constructor",
            winner["constructor_id"]
            .replace("_"," ")
            .title()
        )

        st.metric(
            "Win Probability",
            f"{winner['win_probability']:.2%}"
        )

        st.progress(
            float(
                winner["win_probability"]
            )
        )

    with c2:

        if os.path.exists(
            constructor_img
        ):
            st.image(
                constructor_img,
                width=120
            )

# ------------------------------------------------
# Podium
# ------------------------------------------------

st.divider()

st.subheader(
    "🥇 Predicted Podium"
)

left, center, right = st.columns(
    [1,1.4,1]
)

podium_order = [
    (1, podium.iloc[1], left),
    (0, podium.iloc[0], center),
    (2, podium.iloc[2], right)
]

medals = {
    0:"🥇",
    1:"🥈",
    2:"🥉"
}

for pos, driver, col in podium_order:

    with col:

        st.markdown(
            f"## {medals[pos]}"
        )

        img = (
            f"assets/drivers/"
            f"{driver['driver_id']}.png"
        )

        if os.path.exists(img):

            st.image(
                img,
                use_container_width=True
            )

        st.markdown(
            f"### {driver['driver_id'].title()}"
        )

        team_logo = (
            f"assets/constructors/"
            f"{driver['constructor_id']}.png"
        )

        if os.path.exists(team_logo):

            st.image(
                team_logo,
                width=90
            )

        st.progress(
            float(
                driver[
                    "win_probability"
                ]
            )
        )

        st.write(
            f"**{driver['win_probability']:.2%}**"
        )

# ------------------------------------------------
# Chart
# ------------------------------------------------

st.divider()

st.subheader(
    "📈 Win Probability Distribution"
)

chart_df = top10.copy()

chart_df["Driver"] = (
    chart_df["driver_id"]
    .str.title()
)

chart_df["Probability"] = (
    chart_df["win_probability"] * 100
)

st.bar_chart(
    chart_df.set_index(
        "Driver"
    )["Probability"]
)

# ------------------------------------------------
# Standings
# ------------------------------------------------

st.divider()

st.subheader(
    "🏎️ Predicted Race Standings"
)

for pos, (_, row) in enumerate(
    top10.iterrows(),
    start=1
):

    cols = st.columns(
        [0.6,1,0.8,3,2]
    )

    with cols[0]:
        st.markdown(
            f"### {pos}"
        )

    with cols[1]:

        img = (
            f"assets/drivers/"
            f"{row['driver_id']}.png"
        )

        if os.path.exists(img):

            st.image(
                img,
                width=70
            )

    with cols[2]:

        logo = (
            f"assets/constructors/"
            f"{row['constructor_id']}.png"
        )

        if os.path.exists(logo):

            st.image(
                logo,
                width=60
            )

    with cols[3]:

        st.markdown(
            f"""
            **{row['driver_id'].title()}**
            """
        )

        st.caption(
            row[
                "constructor_id"
            ]
            .replace("_"," ")
            .title()
        )

    with cols[4]:

        st.progress(
            float(
                row[
                    "win_probability"
                ]
            )
        )

        st.write(
            f"{row['win_probability']:.2%}"
        )

# ------------------------------------------------

st.divider()

st.caption(
    "Formula 1 Winner Predictor • Powered by Machine Learning"
)