import pandas as pd

def load_data():

    results = pd.read_csv(
        "data/results_2008_2026.csv"
    )

    qualifying = pd.read_csv(
        "data/qualifying_2008_2026.csv"
    )

    races = pd.read_csv(
        "data/races.csv"
    )

    circuits = pd.read_csv(
        "data/circuits.csv"
    )

    return {
        "results": results,
        "qualifying": qualifying,
        "races": races,
        "circuits": circuits
    }