import pandas as pd

def calculate_driver_championship(pred_df):

    standings = (
        pred_df
        .groupby("driver_id")["predicted_points"]
        .sum()
        .reset_index()
        .sort_values(
            "predicted_points",
            ascending=False
        )
        .reset_index(drop=True)
    )

    standings.index += 1

    standings.rename(
        columns={
            "predicted_points": "points"
        },
        inplace=True
    )

    return standings

def calculate_constructor_championship(pred_df):

    standings = (
        pred_df
        .groupby("constructor_id")["predicted_points"]
        .sum()
        .reset_index()
        .sort_values(
            "predicted_points",
            ascending=False
        )
        .reset_index(drop=True)
    )

    standings.index += 1

    standings.rename(
        columns={
            "predicted_points": "points"
        },
        inplace=True
    )

    return standings