import pandas as pd
import json

# Step 1: Load the JSON file
with open("users.json", "r") as file:
    data = json.load(file)

# Step 2: Normalize JSON (flatten nested fields)
df = pd.json_normalize(data, sep="_")

# Step 3: Display the first 5 rows (with company names visible)
print("=== First 5 Rows of the JSON Dataset ===")
print(df[["id", "name", "username", "email", "company_name"]].head())

# Step 4: Show a summary of columns
print("\n=== Summary of Columns ===")
print(df.info())
