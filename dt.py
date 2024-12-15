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



#Group (month by month) and (year by year)
df = pd.read_csv('testsetf.csv')   # Load the dataset

# Load the dataset, parsing the 'datetime_utc' column as datetime objects
df = pd.read_csv("testsetf.csv", parse_dates= ["datetime_utc"])

# Create a new DataFrame 'data' with the '_tempm' column as the temperature values and 'datetime_utc' as the index
data = pd.DataFrame(list(df['_tempm']), index=df['datetime_utc'], columns=['temp'])
data.head(4)


avg_month = data.resample('m').mean()  # Resampling data with date frequency (month by month)
avg_month.head(4)

avg_year = data.resample('y').mean()  # Resampling data with date frequency (year by year)
avg_year.head(4)

avg_year = avg_month.resample('y').mean()  # resampling data with date frequency (year by year)
avg_year.head(4)                           # This and above are same result but this reduce timecomplexicity 

y = avg_year['1998':'2002']   # y = avg_year['1997-12-31':'2016-12-31']   # slicing
y.head()

y = avg_year['1998':'2010':4]  # y = avg_year['1997-12-31':'2016-12-31': Gap]
y

# Bar graph (Temp v/s Months)
plt.figure(figsize= (24,8))
sns.barplot(x=avg_month.index, y=avg_month['temp'])

m = avg_month['2002-01-01':'2002-12-31'] # After slicing you can see spacific years
plt.figure(figsize= (24,8))
sns.barplot(x=m.index, y=m['temp'])
