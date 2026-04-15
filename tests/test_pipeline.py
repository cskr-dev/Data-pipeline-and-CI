import pandas as pd
from pipeline.transform import transform_data

def test_transform():
    data = {
        "country": ["India", "India", "USA"],
        "amount": [100, 200, 300]
    }

    df = pd.DataFrame(data)
    result = transform_data(df)

    assert "country" in result.columns
    assert "amount" in result.columns
    assert result[result["country"] == "India"]["amount"].values[0] == 300