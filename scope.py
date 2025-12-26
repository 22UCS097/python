
username="ravi kumar"

def func():
    # username="hello"
    print(username)

print(username)    
func()

x=99

# def func2(y):
#     # x=10
#     z=x+y
#     return z

# print(func2(5))

'''
def func3():
    global x  #avoid this b/c goin to overwrite globalvalue:
    x=12
    
func3()
print(x)    
'''

def f1():
    x=88
    def f2():
        print(x) 
    return f2
myresult=f1()  
myresult()


def chaiaurcode(num):
    def actual(x):
        return x ** num
    return actual

f=chaiaurcode(2)
g=chaiaurcode(3)











