import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
def add(a,b):
    print("ADDITION")
    print(a,"+",b,"=",a+b)
    print("*-*-*-*-*-*-*-*-*-*")
def sub(a,b):
    print("SUBTRACTION")
    print(a,"-",b,"=",a-b)
    print("*-*-*-*-*-*-*-*-*-*")
def mul(a,b):
    print("MULTIPLICATION")
    print(a,"*",b,"=",a*b)
    print("*-*-*-*-*-*-*-*-*-*")
def div(a,b):
    if b==0:
        print("SORRY DIVISION IS NOT POSSIBLE")
        print("*-*-*-*-*-*-*-*-*-*")
    else:
        print("DIVISION")
        print(a,"/",b,"=",a/b)
        print("*-*-*-*-*-*-*-*-*-*")
add(i,j)
sub(i,j)
mul(i,j)
div(i,j)