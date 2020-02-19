def testreturn(x,y):
    return x+y


def testusereturn():
    ip = input("Ente : ")
    ip2 = input("Enter :")
    x = testreturn(int(ip),int(ip2))
    print(x)

def oneplus(x,y):
    
    i = x % y
    count = 0
    while i != y:
        i += 1
        count += 1
    return count
##testusereturn()
def byteCal(x):
    y = x % 4
    z = 0
    while(y != 4):
        y+=1
        z+=1
    return z

def converter(x,y):
    return x%y
 
def bintodec():
    ipnum = float(input("Enter num : "))
    ipbase = float(input("Enter base :"))
    lst = []
    while float(ipnum) != 0:
        x = converter(int(ipnum),int(ipbase))
        print(str(int(ipnum)),"/",(str(int(ipbase))),'=',x)
        lst.append(x)
        ipnum = int(ipnum) // int(ipbase)
    for i in range(0,byteCal(len(lst))): #0 = start, btreCal = end
        lst.append("0")
    lst = reversed(lst)
    count = 0
    for i in lst:
        print(str(int(i)),end = "")
        count +=1
        if count % 4 == 0:
            print(" ",end="")
        
bintodec()
##print(byteCal(1))




    
