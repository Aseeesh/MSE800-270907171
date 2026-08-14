from ucimlrepo import fetch_ucirepo

# Fetch dataset
iris = fetch_ucirepo(id=53)

# Data (as pandas dataframes)
X = iris.data.features
y = iris.data.targets

# Debug: Check column names
print("Columns in y:", y.columns.tolist())

# Get the first column name (it might be 'class', 'target', or something else)
target_column = y.columns[0]  # Use the first column

# 1. Total number of records
total_records = len(X)
print(f"Total number of records: {total_records}")

# 2. Total number of different flowers
unique_flowers = y[target_column].unique()
total_flower_types = len(unique_flowers)
print(f"Total number of different flowers: {total_flower_types}")

# 3. Names of all different flowers
print(f"Names of all different flowers: {list(unique_flowers)}")

# Optional: Distribution
print("\nDistribution:")
print(y[target_column].value_counts())