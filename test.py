from utils.preprocess import load_data, clean_data, split_data

df = load_data()
df = clean_data(df)

X, y = split_data(df)

print("X shape:", X.shape)
print("y shape:", y.shape)