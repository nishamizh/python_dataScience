# Importing the required libraries
import numpy as np
print(np.__version__)
import pandas as pd
print(pd.__version__)
import matplotlib.pyplot as plt
#print(matplotlib.__version__)
import seaborn as sns
print(sns.__version__)
 
# Ingore harmless warnings
import warnings
warnings.filterwarnings('ignore')

# Import penguin data from seaborn
data = sns.load_dataset('penguins')

# sample data
data.head()

# Data dimensions
print(f'The data has {data.shape[0]} rows and {data.shape[1]} columns.')

# check for null values
# data.isnull().sum()                   # Number of missing values
round(data.isnull().mean()*100, 2)      # Percentage of missing values

# Remove the missing values
data.dropna(inplace=True)

# percentage missing value after removing it
round(data.isnull().mean()*100, 2)

# scatter plot b/w towo numerical variable
sns.scatterplot(x='flipper_length_mm',
                y='body_mass_g',
                data=data, color='green')
plt.show()