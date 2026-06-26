# verify_features.py

import pickle

with open(
    "models/f1_post_quali_model.pkl",
    "rb"
) as f:
    model = pickle.load(f)

print(
    len(model.feature_names_in_)
)

print(
    list(model.feature_names_in_)
)