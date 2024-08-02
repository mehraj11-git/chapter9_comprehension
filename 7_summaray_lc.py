# what is comprehension 
# it  means we can create list in one line 
# for  ex:
# we are now print the square of the numbers 

square = [i**2 for i in range(11)]
print(square)

# first,think what we have to do ,we have t0 do append of created(i,w,name,etc..)
# list in that we have to do  a square.
# and start loop 

#  if method 
# this method check the condition 
# for ex: we gonna take the even number from 50 numbers

even_number = [i for i in range(51) if i%2==0]
print(even_number)

# if with else condition 
# in this condition we add for loop in the last position 
natural = [i*2 if i%2==0 else -i for i in range(21)]
print(natural)

# nested list comprehension 
# nested list means list inside list 
# for ex: we want wo create list 
# l =[[1,2,3],[1,2,3],[1,2,3]] 
# in this we have do looping in word that we done append with that 

nested_list = [[i for i in range(1,4)] for i in range(3)]
print(nested_list)