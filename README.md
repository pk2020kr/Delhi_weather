# Delhi Temperature Trends Analysis (Summer Project 2023)

## Overview
This project analyzes temperature trends in Delhi, India using historical weather data from 1996 to 2016. The analysis focuses on identifying patterns, seasonal variations, and long-term temperature trends through data visualization and statistical analysis.

## Dataset
The analysis uses the "testsetf.csv" dataset which contains hourly weather measurements for Delhi including:
- Temperature data
- Humidity
- Dew point
- Visibility
- Wind speed
- Pressure
- Weather conditions

## Analysis Performed
The notebook includes the following analyses:

1. **Data Preprocessing**
   - Loading and cleaning the dataset
   - Converting date/time strings to datetime objects
   - Setting up the datetime as the index for time-series analysis

2. **Temporal Aggregations**
   - Monthly average temperatures
   - Yearly average temperatures
   - Daily maximum, minimum, and average temperatures

3. **Trend Analysis**
   - Long-term temperature trends over the 20-year period
   - Year-over-year comparisons
   - Seasonal patterns identification

4. **Visualizations**
   - Line plots for temperature trends
   - Time series visualizations
   - Statistical summaries

## Key Findings
- The analysis shows temperature patterns and trends in Delhi over a 20-year period
- Visualizations help identify seasonal variations and potential warming trends
- Statistical summaries provide insights into temperature distributions and extremes

## Requirements
To run this notebook, you'll need:
- Python 3.8
- Pandas
- NumPy
- Matplotlib
- Seaborn

## How to Use
1. Ensure all required libraries are installed
2. Place the "testsetf.csv" file in the same directory as the notebook
3. Run the notebook cells sequentially to reproduce the analysis

## License
This project is available for educational and research purposes. 
