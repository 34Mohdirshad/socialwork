#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = int(input("enter the number:="))
b = int(input("enter the number:="))

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")


# In[2]:


num = 0

while num < 6:
    print(num)
    num += 1


# In[3]:


for num in range(6):
    if num != 3:
        print(num)


# In[4]:


string = "mango"

for char in string:
    print(char)


# In[5]:


for num in range(7):
    print(num)


# In[6]:


for num in range(5, 26, 5):
    print(num)


# In[7]:


def getinfo(first_name, last_name, age):
    print("My name is", first_name, last_name + ". I am", age, "years old.")

# Example usage
getinfo("mohd", "irshad", 20)


# In[8]:


def sum_of_three(num1, num2, num3):
    return num1 + num2 + num3

# Example usage
result = sum_of_three(5, 10, 15)
print(result)


# In[9]:


def sum_of_three(num1, num2=0, num3=0):
    return num1 + num2 + num3

# Example usage
result = sum_of_three(5)
print(result)


# In[ ]:




