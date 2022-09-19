# Python Data Types
# There are different types of data types in Python. Some built-in Python data types are:
#
# 1) python data type - Numeric    ,----> Python numeric data type is used to hold numeric values like: int, float, complex
# 2) python data type - String     ,----> str , Python supports Unicode characters
# 3) python data type - List       ,----> It is the same as the array , it can simultaneously hold different types of data
# 4) python data type - Tuple      ,----> It is another data type which is a sequence of data similar to a list and it is written using () and , .
# 5) python data type - Dictionary ,----> It is similar to the hash table type , it is an unordered sequence of data of key-value pair form


###########################    LIST DATA TYPE    ###########################

# List is a data type that allows multiple data and can be different data types

data = [45, 20, 15.5, "Team"]

print(data)               # o/p -->[45, 20, 15.5, 'Team']
print(data[0])            # o/p --> 45
print(data[1])            # o/p --> 20
print(data[2])            # o/p --> 15.5
print(data[3])            # o/p --> Team

print(data[-1])  # o/p --> Team  ( "[-1]" refers to last index of the list)
print(data[1:3])  # o/p --> [20, 15.5]  (Sub list value)

# If we want to insert anything in the middle or anywhere in the list ,we can do in the list by using keyword "insert"

data.insert(4, "zucitech")
print(data)  # o/p --> [45, 20, 15.5, 'Team', 'zucitech']

data.insert(3, 4)
print(data)  # o/p --> [45, 20, 15.5, 4, 'Team', 'zucitech']

# if we want to add the data or values in the End, we can use keyword "Append"

data.append("Employees")
print(data)  # o/p --> [45, 20, 15.5, 4, 'Team', 'zucitech', 'Employees']

# if we want to update the data or value

data[4] = "TEAM"
print(data)  # o/p --> [45, 20, 15.5, 4, 'TEAM', 'zucitech', 'Employees']

# if we want to delet the data simply we can use keyword called "del"

del data[0]
print(data)  # o/p --> [20, 15.5, 4, 'TEAM', 'zucitech', 'Employees']


###########################    TUPLE DATA TYPE    ###########################

# List and Tuple does the same thing ,But only difference is list data type is mutable and tuple is immutable.

value = (1, 6.5, "chethan", 20)
print(value)                          # o/p --> (1, 6.5, 'chethan', 20)
print(value[0])                       # o/p --> 1
print(value[1])                       # o/p --> 6.5
print(value[2])                       # o/p --> chethan
print(value[3])                       # o/p --> 20

# value[2] = "shetty"
# print(value)

###########################    DICTIONARY DATA TYPE    ###########################

# Dictionaries are written within curly braces ("{}")in the form "key:value"

dic = {"a": 1, 4: "b", "Name": "Chethan KP"}

print(dic["a"])  # o/p --> 1
print(dic[4])  # o/p --> b
print(dic["Name"])  # o/p --> Chethan KP

# Create Dictionaries at run time and add data into it

dict = {}

dict["Firstname"] = "Chethan"
dict["Lastname"] = "KP"
dict["age"] = "10"

print(dict)
print(dict["Firstname"])
