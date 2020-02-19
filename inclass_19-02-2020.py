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



import numpy as np
def testnumpy():
    a = np.array([0,1,2,3])
    b = np.array([[0,1,2],[3,4,5]])
    print(a)
    print(b)
    print(b.shape)

def function_matrix():
    a = np.arange(1,9,2)
    print(a)
    b = np.linspace(0,1,6)
    print(b)
    c = np.linspace(0,1,5, endpoint=False)
    print(c)


def common_arrays():
    a = np.ones((3,3))
    print(a)
    b = np.zeros((2,2))
    print(b)

def identity_matrix():
    a = np.eye(3)
    print(a)
    b = np.diag(np.array([1,2,3,4]))
    print(b)
    c = np.diag(np.array([0.2,0.4,0.6,0.8]))
    print(c)
    d = np.diag(np.linspace(0.2,1,4, endpoint=False))
    print(d)


import matplotlib.pyplot as plt

def basic_visualization():
    x = np.linspace(0,3,20)
    y = np.linspace(0,9,20)
    plt.plot(x,y,"o")
    plt.plot(x,y,color="green",marker="o",linestyle="dashed",linewidth=2,markersize=10)
    image=np.random.rand(30,30)
    plt.plot(image)
    image=np.random.rand(30,30)
    plt.imshow(image,cmap=plt.cm.hot)
    plt.colorbar()
    
