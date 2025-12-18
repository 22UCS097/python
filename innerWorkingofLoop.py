f=open('loop.py')

# for line in f:
#     print(line,end=' ')

# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line,end='')


I=iter(f) # file me iter jo memory ko poins kart hay
I.__next__()

myList=[1,2,5,3]
I=iter(myList)
I.__next__()


#for the file iter(f) and f is same but not for list
iter(f) is f #yes
iter(myList) is myList #no

