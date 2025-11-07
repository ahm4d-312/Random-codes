# Flatten the nested JSON into a simple table
from pandas import json_normalize
import json

with open("users.json") as f:
    data = json.load(f)

users_flat = json_normalize(data)

print("=== Flattened JSON (first 5 rows) ===")
print(users_flat.head(), "\n")

print("=== Summary of Flattened Data ===")
print(users_flat.info(), "\n")
