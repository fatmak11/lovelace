from google.colab import files
uploaded = files.upload()
from zipfile import ZipFile

file_name = "HeartDataCE101.zip"
with ZipFile(file_name, 'r') as zip:
  zip.extractall()
  print('Done')
import pandas as pd

heart_data = pd.read_csv("heart.csv")

heart_data.head()
import pandas as pd

heart_data = pd.read_csv("heart.csv", index_col=0)

heart_data.head()
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid')
import plotly.graph_objs as go
import plotly.offline as py

df = pd.read_csv("heart.csv")
#df.head()
df.columns = ['Age', 'Sex', 'Chest_pain_type', 'Resting_bp',
              'Cholesterol', 'Fasting_bs', 'Resting_ecg',
              'Max_heart_rate', 'Exercise_induced_angina',
              'ST_depression', 'ST_slope', 'Num_major_vessels',
              'Thallium_test', 'Condition']
df.head()
df.describe()
df.info()
print()
print(f'Shape of the dataset')
print(f'Number of features: {df.shape[1]}')
print(f'Number of obserservations: {df.shape[0]}')

df.isnull().sum()
