# convert string list to int list:

s=['1','2','3','4']

res=map(int,s)
# map(function,iterable)
print(list(res))


# double each   element of list:
li=[1,2,3,4]

def double(ele):
    return  ele*2

res=map(double,li)
# map(double, li) applies double() to 
# each element in li.
print(list(res))


a=[1,2,3,4]

ans=map(lambda x: x*2,a)
print(list(ans))


# ----
a=[1,2,3]
b=[4,5,2]

def addUp(a1,b1):
       return a1+b1
        

ans=map(lambda x,y:x+y,a,b)
# or we can write
# ans=map(addUp,a,b)

print(list(ans))


# Converting strings to Uppercase------------------
s=["ravi","navi","kavi","avi"]

def toUpper(ele):
      return ele.upper()

ans=map(lambda x: x.upper(),s)
res=map(toUpper,s)

print(list(ans))
print(list(res))

# Extracting first character from strings------------

words=["shiv","shambhu","narayan","mahadev"]

res=map(lambda s:s[0],words)

# Removing whitespaces from strings--------

data=['  hello  ','Ravi  ',' aa ']

res=map(str.strip,data)

# print(list(res))

# Calculate fahrenheit from celsius---------

cel=[0,12,100,32]

res=map(lambda c:c*9/+32,cel)

print(list(res))


# --------------------------------------------------------

# filter function in py

def start_a(w):
      return w.startswith("a")

li=["apple","banana","avocado","cherry","apricot"]
res=filter(start_a,li)

print(list(res))

ll=[1,2,-4,25,-8]

def negative(ele):
      if ele<0:
            return ele
      
neg=filter(negative,ll)   
# we will pass function  not call the function   
print(list(neg))

l1=[1,2,7,80,5,3,41]

even=list(filter(lambda x:x%2==0,l1))

print(even)

double=list(map(lambda x: x*2,even))

print(double)


#  Filtering Strings------------------

a=['apple','banana','cherry','kiwi']

def funcLen(w):
      if(len(w)>5):
             return w

b=list(filter(funcLen,a))

print(b)

# reduce function in py-----------------------------

l1=[1,2,3,4]
from functools import reduce
ans=reduce(lambda x,y:x+y,l1,10)
# x+y,list,startingSum(bydefault 0)

print((ans))


s=["hello","ravi","!!"]

bind=reduce(lambda x,y:x+" "+y,s)

print(bind)

# accumulate----------------------------
from itertools import accumulate
from operator import add
a=[1,2,3,4]

res=accumulate(a,add)

print(list(res))





