import pandas as pd

def load_data(csv):
    df = pd.read_csv(csv)
    return df

def to_datetime(df):
    df["date"] = pd.to_numeric(df["date"])
    return df

def new_feature(something):
    return "amazing work! you did something"