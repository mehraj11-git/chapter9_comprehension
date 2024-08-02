# l = [[1,2,3], [1,2,3], [1,2,3]]

new_list =[[i for i in range(1,4)] for i in range(0,3)]
print(new_list)
#   here we ahve to do looping for two time 
# and select the range as you want

new =[]
for i in range(3):
  new.append([1,2,3])

print(new)
