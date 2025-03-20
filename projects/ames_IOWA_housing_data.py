import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import zipfile
import io

url = 'https://github.com/mattharrison/datasets/raw/master/data/ames-housing-dataset.zip'
resposne = requests.get(url)
resposne.raise_for_status

with zipfile.ZipFile(io.BytesIO(resposne.content)) as z:
    csv_name = [name for name in z.namelist() if name.endswith(".csv")]
    print(csv_name)

    with z.open(csv_name[0]) as csv:
        data = pd.read_csv(csv)

print(data.head())