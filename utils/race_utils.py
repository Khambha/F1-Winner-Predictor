def get_race_predictions(
    race_id,
    df
):

    race_df = df[
        df["race_id"] == race_id
    ].copy()

    race_df = race_df.sort_values(
        "win_probability",
        ascending=False
    )

    return race_df