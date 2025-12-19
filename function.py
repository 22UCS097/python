import math
# syntax:
# num=int(input("enter num\n"))

# def printSquare(num):
#     print(num**2)
#     return num**2

# result=printSquare(num)    
# print(result)


#function with multipal parameter:
'''
Docstring for function
def add(a,b):
    return a+b

print(add(2,5))
'''

# mult
# def mult(a,b):
#     print(a*b)


# mult(2,"ravi")
# mult(2,8)

# area of circle
'''

def circleArea(radius):
    area= (math.pi*radius)**2
    cir=math.pi*radius*2
    return area,cir

a,c=circleArea(2)

print(a,c)
'''

# def greet(name="user"):
#     return "hello,"+name+"!"

# print(greet('chai'))


'''
# lemda function:
cube=lambda x: x**3
print(cube(3))
'''

#-------------args----------

# def sum_all(*args):
#     print(args)
#     for i in args:
#         print(i*2)
#     return sum(args)

# print(sum_all(1,5,3))
# print(sum_all(1,5,3,8,5,2))
# print(sum_all(1,5))

#----------kwargs---------------
'''
def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")



print_kwargs(name="Ravi",power="lazer")
'''

# def even_generator(limit):
#    for i in range(2,limit+1,2):
#        yield i

# I= even_generator(10)

# for i in I:
#     print(i)

'''
def fact(n):
    if n==0:
        return 1
    else:
     return n*fact(n-1)

print(fact(4))
'''




  






