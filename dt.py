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

# Mean & Standered Deviation
mean = data.mean()   # Mean
print(mean)

std=data.std()       # Standered Deviation
std

# Average monthly temperature in Delhi from 1997 to 2016
df = pd.read_csv("testsetf.csv")  # read data
df = pd.read_csv("testsetf.csv", parse_dates= ["datetime_utc"]) # Date formet
df.head(2)
data = pd.DataFrame(list(df['_tempm']), index=df['datetime_utc'], columns=['temp']) # taking date and time only
avg_month = data.resample('m').mean()
avg_month.head(4)


df = pd.read_csv("testsetf.csv")  # Read data from CSV file
# Read data again with 'datetime_utc' parsed as datetime objects
df = pd.read_csv("testsetf.csv", parse_dates= ["datetime_utc"])
# Create a new DataFrame 'data' with 'datetime_utc' as the index and '_tempm' as the temperature column
data = pd.DataFrame(list(df['_tempm']), index=df['datetime_utc'], columns=['temp'])
# Resample data to monthly frequency and calculate the mean temperature for each month
avg_month = data.resample('m').mean()                           
jan = avg_month['1997-01':'2016':12]  # Select average temperatures for each month over the years 1997-2016
feb = avg_month['1997-02':'2016':12]
mar = avg_month['1997-03':'2016':12]
apr = avg_month['1997-04':'2016':12]
may = avg_month['1997-05':'2016':12]
jun = avg_month['1997-06':'2016':12]
jul = avg_month['1997-07':'2016':12]
aug = avg_month['1997-08':'2016':12]
sep = avg_month['1997-09':'2016':12]
oct_ = avg_month['1997-10':'2016':12]
nov = avg_month['1997-11':'2016':12]
dec = avg_month['1997-12':'2016':12]
A = jan.mean()  # Calculate the mean temperature for each month
B = feb.mean()
C = mar.mean()
D = apr.mean()
E = may.mean()
F = jun.mean()
G = jul.mean()
H = aug.mean()
I = sep.mean()
J = oct_.mean()
K = nov.mean()
L = dec.mean()
data = np.vstack((A, B, C, D, E, F, G, H, I, J, K, L)) # Stack the monthly averages into a single array
monthly_averages = np.mean(data, axis=1)  # Calculate the average temperature for each month across all years
# Define the month labels
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
fig, ax = plt.subplots(figsize=(24, 8))
ax.bar(months, monthly_averages)
# Set the labels and title for the chart
ax.set_xlabel('Months')
ax.set_ylabel('Average Temperature(C)')
ax.set_title('Average Monthly Temperatures in Delhi Over Two Decades (1997-2016)')
plt.show()


df = pd.read_csv("testsetf.csv")                        # Load the dataset
df['datetime_utc'] = pd.to_datetime(df['datetime_utc']) # Convert the 'datetime_utc' column to datetime objects
data = pd.DataFrame(list(df['_tempm']), index=df['datetime_utc'], columns=['temp']) # Create a new DataFrame 'data' with the '_tempm' column as temperature values and 'datetime_utc' as the index
avg_month = data.resample('m').mean()                   # Resample the data to monthly frequency and calculate the mean temperature for each month
# List of years for labeling the x-axis
year = ['97', '98', '99', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16']
A = avg_month['1997-01':'2016-12':12]  # All Jan  #Extract average temperatures for each month across all years
B = avg_month['1997-02':'2016-12':12]  # All Feb
C = avg_month['1997-03':'2016-12':12]         
D = avg_month['1997-04':'2016-12':12]
E = avg_month['1997-05':'2016-12':12]
F = avg_month['1997-06':'2016-12':12]
G = avg_month['1997-07':'2016-12':12]
H = avg_month['1997-08':'2016-12':12]
I = avg_month['1997-09':'2016-12':12]
J = avg_month['1997-10':'2016-12':12]
K = avg_month['1997-11':'2016-12':12]  # All Nov
L = avg_month['1997-12':'2016-12':12]  # All Dec
a = A.temp   # Extract temperature values for each month
b = B.temp
c = C.temp
d = D.temp
e = E.temp
f = F.temp
g = G.temp
h = H.temp
o = I.temp
j = J.temp
k = K.temp
l = L.temp
# Stack the monthly temperatures for each year, normalized by dividing by 12
data = np.vstack((a / 12, b / 12, c / 12, d / 12, e / 12, f / 12, g / 12, h / 12, o / 12, j / 12, k / 12, l / 12))
# Labels and colors for each month
labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan', 'mediumblue', 'darkgreen']
fig, ax = plt.subplots(figsize=(16, 8))  # Create a figure and axis for the plot
ax.bar(year, data[0], color=colors[0], label=labels[0])  # Plot the bar chart for each month
for i in range(1, len(data)):
    ax.bar(year, data[i], bottom=np.sum(data[:i], axis=0), color=colors[i], label=labels[i])
ax.set_xlabel('Years')           # Set the x-axis label
ax.set_ylabel('Temperature(C)')
ax.set_title('Yearly Average Temperatures in Delhi with Monthly Breakdown (1997-2016)')
ax.legend()                      # Add a legend to the plot
plt.show()

# Temp v/s Days
df = pd.read_csv("testsetf.csv")
df['datetime_utc'] = pd.to_datetime(df['datetime_utc'])
data = pd.DataFrame(list(df['_tempm']), index=df['datetime_utc'], columns=['temp'])
avg_day = data.resample('d').mean()
plt.figure(figsize= (24,8))
# Labels and title
plt.xlabel('Day')
plt.ylabel('Temperature(C)')
plt.title('Temperature in Delhi from 1996 to 2017 w.r.t Day(in X-axis)')
sns.lineplot(x=avg_day.index, y=avg_day['temp'])

# In main data 1996 and 2017 whole month data is not collected so in lower these years are removed
avg_year = data.resample('Y').mean()
plt.figure(figsize= (24,8))
# Labels and title
plt.xlabel('Day')
plt.ylabel('Temperature(C)')
plt.title('Temperature in Delhi from 1996 to 2017 w.r.t Year(in X-axis)')
sns.lineplot(x=avg_year.index, y=avg_year['temp'])
