# list comprehension is it related to list 
# with this method we can create list  in line
#  creating a simple list containg square 
# 
# simple way
square_list = []
for i in  range(1,11):
    square_list.append(i**2)
print(square_list)    

# comprehension method 
# think first what you have to append ,i mean in this ex we are gonna make the square of the number ,
# hence, think you have to make the square of the i 
# after that you have to write the for loop condition and close the bracket
# we use square bracket in this comprehension method
# (1)
square = [i**2 for i in range(1,11)]
print(square)
# (2)
# we have to create the list containing negative value
# simple method
negative = []
for i in range(1,11):
    negative.append(-i)
print(negative)    

# comprehension method 
negative1 = [-i for i in range(1,11)]
print(negative1)

# (3)
# in this ex we print the first letter of each Name 
names = "merhaj" ,"sharat" , "hameed"
# simple method 
name = []
for i in names:
    name.append(i[0])
print(name)    

# comprehension method 
name2 = [i[0] for i in names]
print(name2)