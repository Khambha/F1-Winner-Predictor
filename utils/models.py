import pickle

def load_models():

    with open("models/f1_post_quali_model.pkl", "rb") as f:
        post_model = pickle.load(f)

    with open("models/f1_pre_quali_model.pkl", "rb") as f:
        pre_model = pickle.load(f)

    with open("models/f1_position_model.pkl", "rb") as f:
        position_model = pickle.load(f)

    with open("models/f1_post_quali_features.pkl", "rb") as f:
        post_features = pickle.load(f)

    with open("models/f1_pre_quali_features.pkl", "rb") as f:
        pre_features = pickle.load(f)

    with open("models/f1_position_features.pkl", "rb") as f:
        position_features = pickle.load(f)

    return {
        "post_model": post_model,
        "pre_model": pre_model,
        "position_model": position_model,
        "post_features": post_features,
        "pre_features": pre_features,
        "position_features": position_features
    }