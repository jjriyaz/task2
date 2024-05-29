count=0
count_a=0
count_e=0
count_i=0
count_o=0
count_u=0
n="Guvi Geeks Network Private Limited"
for i in n:
    if i in ["a","e","i","o","u"]:
        count=count+1
        if (i=="a"):
           count_a= count_a+1
        elif (i=="e"):
           count_e = count_e+1
        elif (i=="i"):
           count_i=count_i+ 1
        elif (i=="o"):
           count_o =count_o+ 1
        elif (i=="u"):
           count_u=count_u +1
print("count of a:",count_a)
print("count of e:",count_e)
print("count of i:",count_i)
print("count of o:",count_o)
print("count of u:",count_u)