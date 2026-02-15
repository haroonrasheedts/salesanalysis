import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # For plotting graphs
import seaborn as sns

plt.rcParams["figure.figsize"] = [20, 8]
custom_palette = ['red', 'blue', 'green', 'orange' , 'cyan' , 'purple' , 'indigo' , 'magenta' , 'yellow' , 'black' , 'navy' , 'darkorange' , 'brown' , 'pink' , 'gray' , 'olive']

df = pd.read_csv('/home/khaleefa/Documents/Python/PANDAS/Data Analysis Project/datafiles/Diwali_Sales_Data.csv', encoding = 'unicode_escape')
df.drop(['Status','unnamed1'], axis = 1, inplace=True)
df.dropna(inplace=True)

"""
print(df)
print(df.info())

#there are two columns which are empty, hence we will delete them
df.drop(['Status','unnamed1'], axis = 1, inplace=True)
print(df.info())

#check for all the null values in the file
print(pd.isnull(df).sum())

#drop the null values
print(df.shape)
df.dropna(inplace=True)
print(df.shape)
print(pd.isnull(df).sum())

#change the datatype of Amount column as int
df['Amount'] = df['Amount'].astype('int')
print(df['Amount'].dtypes)

#Rename the column Marital_Status as Nikah
df.rename(columns={'Marital_Status' : 'Nikah'}, inplace=True)
print(df)

#Describe the DataFrame
print(df.describe())

#Data Analysis begins here
#1. Plot a graph for Male and Female ratio using sns

mf = sns.countplot(x = 'Gender', data=df)

for bars in mf.containers:
  mf.bar_label(bars)
plt.show()



#2. Check the total amount based on gender and sort in descending order

salesvalue = df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
salesplot = sns.barplot(x = 'Gender', y = 'Amount', data = salesvalue)
salesplot.bar_label(salesplot.containers[0])
plt.show()

#from both the above graphs we can see that Female has spent more amount for puchasing than Male

#3. Check for the age group who spent most of the amount

mf = sns.countplot(x = 'Age Group', data=df, hue = 'Gender')

for bars in mf.containers:
  mf.bar_label(bars)
plt.show()


#4. Check for the Toal Amount spent vs the Age Group

salesage = df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
salesplot = sns.barplot(x = 'Age Group', y = 'Amount', data = salesage, palette=custom_palette, hue = 'Age Group', legend=False)
for container in salesplot.containers:
  salesplot.bar_label(container, fmt='{:,.0f}')
plt.show()



#5. Total number of orders from top 10 states
salesstate = df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
salesplot = sns.barplot(x = 'State', y = 'Orders', data = salesstate, palette=custom_palette, hue = 'State', legend=False)
for container in salesplot.containers:
  salesplot.bar_label(container, fmt='{:,.0f}')
plt.show()


#6. Total Amount for top 10 states
salesstate = df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
salesplot = sns.barplot(x = 'State', y = 'Amount', data = salesstate, palette=custom_palette, hue = 'State', legend=False)
for container in salesplot.containers:
  salesplot.bar_label(container, fmt='{:,.0f}')
plt.show()


#7. Marital Status

ms = sns.countplot(x = 'Marital_Status', data=df, palette=custom_palette, hue = 'Marital_Status', legend=False)

for bars in ms.containers:
  ms.bar_label(bars)
plt.show()


#8. Amount spent based on the Marital Status and Gender
maritalstatus = df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
salesplot = sns.barplot(x = 'Marital_Status', y = 'Amount', data = maritalstatus, palette=custom_palette, hue = 'Gender')
for container in salesplot.containers:
  salesplot.bar_label(container, fmt='{:,.0f}')
plt.show()


#9. Occupation

oc = sns.countplot(x = 'Occupation', data=df, palette=custom_palette, hue = 'Occupation', legend=False)

for bars in oc.containers:
  oc.bar_label(bars)
plt.show()


#10. Purchasing power based on occupation

occupation = df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
salesplot = sns.barplot(x = 'Occupation', y = 'Amount', data = occupation, palette=custom_palette, hue = 'Occupation')
for container in salesplot.containers:
  salesplot.bar_label(container, fmt='{:,.0f}')
plt.show()


#11. Product Category

pc = sns.countplot(x = 'Product_Category', data=df, palette=custom_palette, hue = 'Product_Category', legend=False)

for bars in pc.containers:
  pc.bar_label(bars)
plt.show()

"""
#12. Purchasing power based on product category

productcategory = df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
salesplot = sns.barplot(x = 'Product_Category', y = 'Amount', data = productcategory, palette=custom_palette, hue = 'Product_Category')
for container in salesplot.containers:
  salesplot.bar_label(container, fmt='{:,.0f}')
plt.show()

"""

#13. Top Selling products

productid = df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
salesplot = sns.barplot(x = 'Product_ID', y = 'Orders', data = productid, palette=custom_palette, hue = 'Product_ID')
for container in salesplot.containers:
  salesplot.bar_label(container, fmt='{:,.0f}')
plt.show()

"""