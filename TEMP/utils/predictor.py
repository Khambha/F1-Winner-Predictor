import pickle
import pandas as pd

with open(
    "models/f1_post_quali_model.pkl",
    "rb"
) as f:
    MODEL = pickle.load(f)

FEATURES = list(
    MODEL.feature_names_in_
)

def predict_winner(
    race_df
):

    temp = race_df.copy()

    temp["win_probability"] = (
        MODEL.predict_proba(
            temp[FEATURES]
        )[:,1]
    )

    winner = (
        temp
        .sort_values(
            "win_probability",
            ascending=False
        )
        .iloc[0]
    )

    return winner