def decorator(func):
    def wrapper():
        print("befor calling the function.")
        func()
        print("after calling the function")
    return wrapper    





def greet():
    print("hello")
greet=decorator(greet)    

greet()
