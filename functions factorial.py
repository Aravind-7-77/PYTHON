def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print("factorial of 4 is:",factorial(4))
print("factorial of 6 is:",factorial(6))



#even odd
def even_odd(num):
 if num%2==0:
    print(num,"is even number")
 else:
    print(num,"is odd number")
even_odd(10)
even_odd(13)

#arthimatic operators
def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=calc(100,45)
print("the result are")
for i in t:
    print(i)
        
