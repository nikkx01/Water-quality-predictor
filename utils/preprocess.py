import pandas as pd

def load_data():
    df = pd.read_csv("data/waterQualityPrediction.csv")
    return df

def clean_data(df):
    # Convert all columns to numeric
    df = df.apply(pd.to_numeric, errors='coerce')

    # Handle target column separately
    # Drop rows where target is missing
    df = df.dropna(subset=["is_safe"])

    # Fill missing values in features only
    features = df.drop("is_safe", axis=1)
    features = features.fillna(features.mean())

    # Combine back
    df = pd.concat([features, df["is_safe"]], axis=1)

    return df

def split_data(df):
    X = df.drop("is_safe", axis=1)
    y = df["is_safe"]
    
    return X, y