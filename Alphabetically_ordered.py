#Alphabetically_ordered
#https://www.codewars.com/kata/5a8059b1fd577709860000f6

def is_alphabetical(word: str) -> bool:
    ordered = sorted(word)
    product = word == "".join(ordered)
    return product

print(is_alphabetical("Dominoes"))  
print(is_alphabetical("Money"))   
print(is_alphabetical("Bees"))   
print(is_alphabetical("Air"))   

#This function returns a booleon value of "true" or "false" for every string based on it's alphabetical order.
#For each string, the characters in each word are sorted in alphabetical order.
#This newly sorted set is turned back into a string.
#Finally, the function reveals whether the original characters are in alphabetical order or not.