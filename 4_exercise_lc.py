# def a func that  contian a list ,this list contian any type of data 
# for ex string,number,floating point ect
# we have to make a separate list of numbers and flaoting point in the form of string 
 
# comprehension method
def mix_list(l):
    return[str(i) for i in l if type(i)==int or type(i) ==float]
    
print(mix_list(["mehraj",1,2,3.4,[1,2,3],"khan"]))

# simple method

def mix_string(m):
    
    for i in m:
        mix = []
        mix.append(str(i))
        if type(i) == int or type(i) ==float:
         return mix
print(mix_string(["mehraj",1,2,3.4,[1,2,3],"khan"]))
