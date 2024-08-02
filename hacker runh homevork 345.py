#https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
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


#https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true
n = int(input())
if 1<= n <= 20 :
    for i in range(0,n):
        i =i**2
        print(i)


#https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true
a = int(input())
b = int(input())
print(str(a//b))
print(str(a/b))



#https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
n = int(input())
if 1 <= n <= 150:
    for a in range (1,n+1):
        print(a,end='')
else:
    print(n)
