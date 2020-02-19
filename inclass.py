def circle_area(radius=0):
    return 3.14 * x **2

def setx(y):
    x = 12
    print('x is ',x)

def information():
    name = input("Enter : ")
    salart = input("Enter : ")
    company = input("company : ")
    print("information")
    print("name","salart","company")
    print(name,salart,company)



def plus():
    first = int(input("Enter first number : "))
    second = int(input("Enter second number : "))
    sum = first + second
    print(sum)

def nameandage():
    name,age = input ("Enter name and age").split()
    print("name ",name)
    print("age ",age)

def text():
    text = input("Enter text : ")
    print('{:<50}'.format(text))
    print('{:>50}'.format(text))
    print('{:^50}'.format(text))

def justification():
    text = input("Enter text : ")
    print("Left justification : ",text.ljust(60,"*"))
    print("Right justification : ",text.rjust(60,"*"))
    print("Center justification : ",text.center(60,"*"))


def ipfloat():
    number = float(input("Enter float number : "))
    print("Normal Float : {:f}".format(number))
    print("Float with fixed pading : {:.2f}".format(number))
    print("Normal Float : {:e}".format(number))

