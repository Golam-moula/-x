print ("hello world")


x = input ("we are starting the count from >> ")
x = int  (x)  #makes the input string of x to int


y = input ("we are ending our count at >> ")
y = int (y)  #makes the input strint of y to int


def deleting_extars():
    l = ( (x*(x-1))/ 2)
    l = int (l)
    pass

deleting_extars()

def make_the_others_count():
     p = ((y*(y-1))/2)
     p = int (p)
     print (p)
     pass
make_the_others_count()

def final_func():
    print (p-l)


final_func()
