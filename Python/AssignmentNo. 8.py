#!/usr/bin/env python
# coding: utf-8

# # 1.Write a Python program to print yesterday, today, tomorrow.

# In[4]:


import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print("Today",today)
print("Yesterday", yesterday)
print("Tomorrow", tomorrow)


# # 2.Write a Python program to print next n days starting from today.

# In[7]:


import datetime
N = int(input("Enter your next n days:- "))
base = datetime.datetime.today()
for i in range(0,N):
    print(base + datetime.timedelta(days = i))


# # 3.WAP to demonstrate all the methods in datetime module
# 
# -> datetime
#       - year
#       - month
#       - day
#       - timedelta
#       - strftime
#       - datetime.strptime
# -> time
#      - hour
#      - minute
#      - second

# In[30]:


# Importing date class from datetime module
from datetime import datetime

# Creating the date obejct of today's date
Current_Year = date.today()

# print the Current year.
print("Current Year", Current_Year.year)
print("-"*80)

# Print the Current Month.
print("Currnet Year", Current_Year.month)
print("-"*80)

#Print the Current Day.
print("Current Year", Current_Year.day)
print("-"*80)

#The strftime method returns a string representing date and time.
# Using date, time or datetime object.
# Print the year by using Strftime.
Year = Current_Year.strftime("%Y") #Captial "Y" for year.
print("Year", Year)
print("-"*80)
#Print the Month by using strftime.
Month = Current_Year.strftime("%B") # Captial for full form and Small for short form.
print("Month", Month)
print("-"*80)

# datetime.strptime
from datetime import datetime

# Assigning the string to Variable.
date_string = "21 June, 2018"

# Using strptime module.
date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)
print("type of date_object =", type(date_object))
print("-"*80)

# TIME
Now = datetime.now()
Current_Time = Now.strftime("%H : %M : %S") # %H for Hours , %M for Minutes , %S for Seconds  
print("Current Time = ",Current_Time)


# # 4.Explain the following methods in maths module with an example.
#      - sqrt
#      - pow
#      - factorial
#      - floor
#      - ceil
#      - pi

# #  Sqaure Root  .sqrt(N1)

# In[6]:


# The math.sqrt() method returns the square root of a number.
# Python program to demostrate the 
# sqrt() Module
num = int(input("Enter your Number:- "))
#Import the math module
import math

# Print the Square root of 4
print(math.sqrt(num))


# # Power .pow(N1,N2)

# In[5]:


#Definition and Usage
# The pow() function returns the value of x to the power of y (xy).

# If a third parameter is present, it returns x to the power of y, modulus z.
          # Return the value of 4 to the power of 3, modulus 5 (same as (4 * 4 * 4) % 5):
Num2 = int(input("Enter your number: "))
Num3 = int(input("Enter your number: "))
print(math.pow(Num2,Num3))


# # Factorial .factorial(N1).

# In[7]:


Num5 = int(input("Enter your Numbers : "))
print(math.factorial(Num5))


# # Floor .floor().

# In[12]:


# floor() method in Python returns the floor of x i.e., the largest integer not greater than x. 
print("math.floor(-23.11 : ", math.floor(-23.11))
print("math.floor(300.16 : ", math.floor(300.16))
print("math.floor(300.72 : ", math.floor(300.72))


# # Ceil .ceil()

# In[15]:


# The method ceil() in Python returns a ceiling value of x i.e., Smallest integer not less than x.
print ("math.ceil(-23.11) : ", math.ceil(-23.11))
print ("math.ceil(300.16) : ", math.ceil(300.16))
print ("math.ceil(300.72) : ", math.ceil(300.72))


# # pi 

# In[18]:


# The math.pi constant returns the value of PI: 3.141592653589793.

# Note: Mathematically PI is represented by π.

# Print the value of pi
print (math.pi)


# # 5.Explain the following methods in statistics module with an example
# 
# - mean
# - median
# - mode
# - variance

# # Mean

# # Python is a very popular language when it comes to data analysis and statistics. 
# ## Luckily, Python3 provide statistics module, which comes with very useful functions like mean(), median(), mode() etc.
# 
# ## mean() function can be used to calculate mean/average of a given list of numbers. 
# ## It returns mean of the data set passed as parameters.

# Syntax : mean([data-set])
# 
# Parameters :
# [data-set] : List or tuple of a set of numbers.
# 
# Returns : Sample arithmetic mean of the provided data-set.
# 
# Exceptions :
# TypeError when anything other than numeric values are passed as parameter. 

# In[20]:


# Python program to demonstrate mean()
# function from the statistics module
  
# Importing the statistics module
import statistics

# list of positive integer numbers
data1 = [1, 3, 4, 5, 7, 9, 2]
  
x = statistics.mean(data1)
  
# Printing the mean
print("Mean is :", x)


# # MEDIAN()
# 
# ### median() function in the statistics module can be used to calculate median value from an unsorted data-list. The biggest advantage of using median() function is that the data-list does not need to be sorted before being sent as parameter to the median() function.

# Syntax : median( [data-set] )
# 
# Parameters :
# [data-set] : List or tuple or an iterable with a set of numeric values
# 
# Returns : Return the median (middle value) of the iterable containing the data
# 
# Exceptions : StatisticsError is raised when iterable passed is empty or when list is null.

# In[22]:


# Python code to demonstrate the  
# working of median() function.
  
# importing statistics module
import statistics
  
# unsorted list of random integers
data1 = [2, -2, 3, 6, 9, 4, 5, -1]
  
# Printing median of the
# random data-set
print("Median of data-set is : % s "
        % (statistics.median(data1)))


# # MODE.
# 
# ### The mode() of a set of data values is the value that appears most often. It is the value at which the data is most likely to be sampled. A mode of a continuous probability distribution is often considered to be any value x at which its probability density function has a local maximum value, so any peak is a mode.

# Syntax :
# mode([data-set])
# 
# Parameters : 
# [data-set] which is a tuple, list or a iterator of 
# real valued numbers as well as Strings.
# 
# Return type : 
# Returns the most-common data point from discrete or nominal data.
# 
# Errors and Exceptions : 
# Raises StatisticsError when data set is empty.

# In[23]:


# Python code to demonstrate the
# use of mode() function

# mode() function a sub-set of the statistics module
# We need to import the statistics module before doing any work
import statistics

# declaring a simple data-set consisting of real valued
# positive integers.
set1 =[1, 2, 3, 3, 4, 4, 4, 5, 5, 6]

# In the given data-set
# Count of 1 is 1
# Count of 2 is 1
# Count of 3 is 2
# Count of 4 is 3
# Count of 5 is 2
# Count of 6 is 1
# We can infer that 4 has the highest population distribution
# So mode of set1 is 4

# Printing out mode of given data-set
print("Mode of given data set is % s" % (statistics.mode(set1)))


# # VARIANCE().
# 
# ###  variance() is one such function. This function helps to calculate the variance from a sample of data (sample is a subset of populated data).
# 
# ### variance() function should only be used when variance of a sample needs to be calculated. There’s another function known as pvariance(), which is used to calculate the variance of an entire population.

# Syntax : variance( [data], xbar )
# 
# Parameters :
# [data] : An iterable with real valued numbers.
# xbar (Optional) : Takes actual mean of data-set as value.
# 
# Returnype : Returns the actual variance of the values passed as parameter.
# 
# Exceptions :
# StatisticsError is raised for data-set less than 2-values passed as parameter.
# Throws impossible values when the value provided as xbar doesn’t match actual mean of the data-set.

# In[24]:


# Python code to demonstrate the working of
# variance() function of Statistics Module

# Importing Statistics module
import statistics

# Creating a sample of data
sample = [2.74, 1.23, 2.63, 2.22, 3, 1.98]

# Prints variance of the sample set

# Function will automatically calculate
# it's mean and set it as xbar
print("Variance of sample set is % s"
	%(statistics.variance(sample)))


# In[ ]:




