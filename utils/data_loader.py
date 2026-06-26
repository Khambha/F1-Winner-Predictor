import pandas as pd

def load_predictions():
    return pd.read_csv(
        "data/race_predictions.csv"
    )

def load_races():
    return pd.read_csv(
        "data/races.csv"
    )