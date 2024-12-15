# Import the necessary libraries for data manipulation and visualization
import numpy as np              # Library for numerical operations
import pandas as pd             # Library for data manipulation and analysis
import matplotlib.pyplot as plt # Library for creating static, animated, and interactive visualizations
import seaborn as sns

# Read .csv file
df = pd.read_csv('testsetf.csv') #df = pd.read_csv("/kaggle/input/delhi-weather-data/testset.csv") sourse from where I bring data        
df.head()                        # Display the rows of the dataframe

# Set the Time column as the index of the dataframe
df.set_index(['datetime_utc'], inplace=True) # Set the 'datetime_utc' column as the index of the dataframe
df.head(2)

# Fatch only 2 set time & temp
# taking only temperature feature as values and datetime feature as index in the dataframe 
df = pd.read_csv('testsetf.csv')
data = pd.DataFrame(list(df['_tempm']), index=df['datetime_utc'], columns=['temp'])
data.head(4)
