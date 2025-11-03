from india_housing_datasets import fetch_ahmedabad_housing,fetch_gurugram_housing,fetch_mumbai_housing
import pandas as pd

# Fetch dataset in sklearn-style dict
dataset =fetch_mumbai_housing()

# Extract data and target
X = dataset["data"]
y = dataset["target"]

# Print the first 5 rows
print("✅ Features (X):")
print(X.head())

print("\n✅ Target (y):")
print(y.head())

# Optional: see description
print("\n📘 Description:")
print(dataset["DESCR"])
