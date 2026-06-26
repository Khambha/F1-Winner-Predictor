# regenerate_features.py

import pickle

with open(
    "models/f1_post_quali_model.pkl",
    "rb"
) as f:
    model = pickle.load(f)

features = list(
    model.feature_names_in_
)

with open(
    "models/f1_post_quali_features.pkl",
    "wb"
) as f:
    pickle.dump(features, f)

print("Saved")