n = int(input())
if  n//2 == float(n/2) :
    if 2<n<5 :
        print("Not Weird")
    elif 6<n<=20 :
        print("Weird")
    elif n>20 :
        print("Not Weird")
else :
    print("Weird")