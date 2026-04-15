def transform_data(df):
    # remove nulls
    df = df.dropna()

    # convert amount to numeric
    df["amount"] = df["amount"].astype(float)

    # aggregate revenue by country
    result = df.groupby("country")["amount"].sum().reset_index()

    return result