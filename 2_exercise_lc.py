# def a fun that take a list of stirng 
# you have the print the reverse of the string 

# simple method
l = ["abc","arm","xyz"]
reverse_list = []
for i in l:
    reverse_list.append(i[::-1])
print(reverse_list)

# comprehension method
listing = [i[::-1] for i in l]
print(listing)

# def a func and do simple method

def reverse_word(l1):
    new_list = []
    for i in l1:
        new_list.append(i[::-1])
    return new_list    
print(reverse_word(["mno","xyz","abd"]))    

# def a func and do comprehension method

def reverse_string(l):
        return [i[::-1] for i in l]
print(reverse_string(["mno","xyz","abd"]))