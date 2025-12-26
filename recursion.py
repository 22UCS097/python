from functools import reduce
# function inside same function:----------------

# factorial

def factorial(n):
    # base case
     if n==1:
          return 1
     return n*factorial(n-1)

# ans=factorial(4)

# print(ans)

# fibonacci series:

def fibonacci(n):
     if n==0:
          return 0
     if n==1:
          return 1
     return fibonacci(n-1)+fibonacci(n-2)

# n=int(input("enter n"))
# ans=fibonacci(n)
# print(ans)


# *arg Vs **kwargs:----------------------------

def showargs(*args):
     print(type(args))
     for ele in args:
          print(ele,end=" ")
     print()
     return sum(args)

def multiply(*args):
     ans=1
     for ele in args:
          ans=ans*ele
     return ans


          

ans=showargs(1,2,3,4,5)
res=multiply(1,8,2)
# print(res)

# print(ans)


# **kwargs:

def showkwargs(**kwargs):
     print(type(kwargs))
     for key,value in kwargs.items():
          print(key,value)

# showkwargs()

# lambda------------------------------

s1="helloravi"
s2 =lambda func:func.upper()
cube=lambda x:x**3
squar=lambda x:x*x

# print(s2(s1))
# print(cube(2))
print(squar(2))

# use case of lambda function in pythn 

# 1-------
check=lambda x:'positive' if x>0 else 'negative' if x<0 else 'zero'

print(check(-1))
print(check(0))
print(check(9))

# 2------
checkEvenorOdd=lambda x:'even' if x%2==0 else 'odd'

print(checkEvenorOdd(20))

# filter ----------------------------------

n=[1,2,3,4,5,6]

even=filter(lambda x:x%2==0,n)
print(list(even))

# map----------------------------------------
ele=map(lambda x:x*2,n)

print(list(ele),n)

#reduce----------------------------------

li=[1,2,3]
ans=reduce(lambda x,y:x*y,li)
# old,updated

print(ans)


# note-->
# Difference Between lambda and def Keyword

# In Python, both lambda and def can be used to define functions
# , but they serve slightly different purposes. 
# While def is used for creating standard reusable functions, 
# lambda is mainly used for short, anonymous functions 
# that are needed only temporarily.

