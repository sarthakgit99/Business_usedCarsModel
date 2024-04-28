import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

# Load the data
file_path = "cardekho_dataset.csv"
df = pd.read_csv(file_path)

# Display the first 5 rows of the DataFrame
print(df.head())

# Display the shape of the DataFrame
print(df.shape)
print(df.info())
df.duplicated().sum()