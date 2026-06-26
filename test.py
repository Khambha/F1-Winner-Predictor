import pickle

files = [
    "models/f1_post_quali_model.pkl",
    "models/f1_pre_quali_model.pkl",
    "models/f1_position_model.pkl",
    "models/f1_post_quali_features.pkl",
    "models/f1_pre_quali_features.pkl",
    "models/f1_position_features.pkl"
]

for file in files:
    with open(file, "rb") as f:
        obj = pickle.load(f)

    print(file)
    print(type(obj))
    print("-"*50)