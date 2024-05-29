#find most frequent characters

data = input("enter value:") 

result = {}

for i in data:
    if i in result:
        result[i] = result[i] + 1
    else:
        result[i] = 1
print("most frequent characters :", max(result, key=result.get))
