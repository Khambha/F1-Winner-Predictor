from utils.models import load_models
from utils.loader import load_data

models = load_models()
data = load_data()

print("Models Loaded")

print(models.keys())

print()

print("Data Loaded")

for key in data:
    print(
        key,
        data[key].shape
    )