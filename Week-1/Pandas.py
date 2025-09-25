### Pandas

## 4. Introduction of Python Pandas
'''
- We use Pandas - Python library for working with data sets
- With Pandas, we can
    + Load data from difere t sourrces (CSV, Excel, SQL,...)
    + Clean data (remove duplicates, fill mising values, rename columns)
    + Analyze data 
    + Visualize data (often used together with Matplotlib/Seaborn)
- The name "Pandas" references to both "Panel Data" and "Python Data Analysis"
=> Pandas is the backbone of data handling in Pyton, it helps us convert raw data into data that can be used
'''


## 25. Pandas Series
'''
 - A Pandas Series is like a column in a table
 - It is a 1-D array that can contain data of any type
'''
import pandas as pd

def create_series(value, index=None):
    return pd.Series(value, index=index)

# Create a simple Pandas Series from a list
s1 = create_series([10, 15, 20])
print("The first series from list:\n", s1)

# Create a Series by using a key/value object
s2 = create_series({"a": 100, "b": 200, "c": 300})      # The keys of dict will be the labels
print("\nThe second series from dict:\n", s2)

# Create a Series with custom labels
s3 = create_series([5, 6, 7], index=["x", "y", "z"])
print("\n Series with custom index: \n", s3)
print()

## 26, 27, 28. Pandas DataFrame, Pandas Read CSV, Pandas Read JSON
'''
- In Pandas, DataFrame is a multi-dimensional table
- If Series is like a single column then DataFrame is a whole table that contains multiple Series as its columns
'''

def create_dataframe(value, index=None):
    return pd.DataFrame(value, index=index)

# Create a simple Pandas DataFrame
data = {
    "Ex": ["Hee", "Mia", "Jane"],
    "Age": [19, 20, 20]
}
df = create_dataframe(data)
print(df)
# Pandas uses the loc attribute to return one or more specified row(s)
print(df.loc[0])        # Display the first row
print(df.loc[[0, 1]])   # Display row 0 and 1   
print()     

# Create a DataFrame with custom index
df1 = create_dataframe(data, index=['nyc1', 'nyc2', ' nyc3'])
print(df1)
print(df1.loc['nyc1'])
print()

# Load files into a DataFrame
df2 = pd.read_csv('data.csv')
print(df2.to_string())