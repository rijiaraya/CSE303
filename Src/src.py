import pandas as pd
import numpy as np

## Printing the bike sales dataset
data = pd.read_excel("E:\Assignment\Dataset\Bike Sales Dashboard.xlsx")
print(data)

## Income Mean, Median, Variance and Standard deviation 
income_mean = data["Income"].mean()
print("Income Mean: \n")
print(income_mean)

income_median = data["Income"].median()
print("Income Median: \n")
print(income_median)

income_var = data["Income"].var()
print("Income Variance: \n")
print(income_var)

income_std = data["Income"].std()
print("Income Standard Deviation: \n")
print(income_std)

## Age Mean, Median, Variance and Standard deviation
age_mean = data["Age"].mean()
print("Age Mean: \n")
print(age_mean)

age_median = data["Age"].median()
print("Age Median: \n")
print(age_median)

age_var = data["Age"].var()
print("Age Variance: \n")
print(age_var)

age_std = data["Age"].std()
print("Age Std: \n")
print(age_std)


##Determining the frequency and percentage of each type of all categorical and discrete values.
children_freq = data["Children"].value_counts()
print("children frequency: \n")
print(children_freq)

##Percentage of children type
print("Percentage of children type: \n")
print(f"{(children_freq/len(data["Children"]))*100}")

##Cars Frequency
cars_freq = data["Cars"].value_counts()
print("Cars Frequency: \n")
print(cars_freq)

##Percentage of cars type
print("Percentage of cars type: \n")
print(f"{(cars_freq/len(data["Cars"]))*100}")

##Categorical Column: Purchased Bike
purchased_bike = data["Purchased Bike"].value_counts()
print("Categorical Column Purchased Bike: \n")
print(purchased_bike)

##Percentage of purchased bike 
print("Percentage of purchased bike: \n")
print(f"{(purchased_bike/len(data["Purchased Bike"]))*100}")