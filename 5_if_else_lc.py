#in this example we gonna make odd numbers with negative value
numbers = [1,2,3,4,5,5,6,8,9]
new_list = []
for i in numbers:
    if i%2==0:
        new_list.append(i*2)

    else:
        new_list.append(-i)
print(new_list)


new_list2 = [i*2 if i % 2 ==0 else -i for i in numbers]
print(new_list2)

