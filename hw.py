# https://www.w3schools.com/python/pandas/default.asp
# 
import pandas as pd

print(pd.__version__)

df = pd.read_csv("data.csv")
print(df.to_string()) 

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)


a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)


a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
print(myvar["y"])


## Panda Series
## A Pandas Series is like a column in a table.

print("#################################################")
print("##")
print("## Panda Series")
print("##")

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

# Add labels

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

# Dictionary

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

# only use day1 and day2 in the series
myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

# dataFrame

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df.loc[0])
# give each row a name
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)

# read from a file
df = pd.read_csv('data.df.csv')

print("FASTBG 1")
print(df)

# why is df back to the old value
print("FASTBG 2")
print(df.to_string())

print(pd.options.display.max_rows) 
pd.options.display.max_rows = 9999

print("FASTBG 3 json")
dfjson = pd.read_json('data.json')

print(dfjson.to_string()) 


dfcsv = pd.read_csv('data.df.csv')
print(dfcsv.head(10))
print(dfcsv.head())
print(dfcsv.tail())
print(dfcsv.info())


print("FASTBG 4 drop blank and update original df")
df = pd.read_csv('data.df.csv')

df.dropna(inplace = True)

print(df.to_string())

# replace empty cells with a value
df.fillna(130, inplace = True)

# only replace empty cells in one of the columns
df["Calories"].fillna(130, inplace = True)

#Calculate the MEAN, and replace any empty values with it:

df = pd.read_csv('data.df.csv')
x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

# mean = average
# Median = the value in the middle, after you have sorted all values ascending.
# Mode = the value that appears most frequently.


df = pd.read_csv('data.df.csv')
x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)



# replace empty values with mode
df = pd.read_csv('data.df.csv')
x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)


