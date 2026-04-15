import pandas as pd 
import os

data = {
    'id': [1,2,3,4],
    'country': ['India', 'USA', 'India', 'USA'],
    'amount' : [100,200,150,300]
} 
df = pd.DataFrame(data)
print(df)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
file_path = os.path.join(data_dir, 'sales.csv')

df.to_csv(file_path, index=False)
