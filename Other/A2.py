def printmenu():
    print("0.Read numbers")
    print("1.Strictly increasing numbers")
    print("3.All consecutive number pairs have the greatest common divisor 1")
    print("5.Consist of a single number")
    print("4.Only prime numbers")
    print("7.The difference between the absolute value of consecutive numbers is a prime number.")
    print("8.All elements in [0,10] range")
    print("-1.EXIT")    

def readnumbers(nlist,n):           #subprogram pt citire a celor n numere
   for i in range(1,n+1):
       nr=int(input())
       nlist.append(nr)

def writesequence(nlist,st,dr):           #subprogram care afiseaza secventa[st,dr] din nlist
    if st<=dr:
        for i in range(st,dr+1):
            print(nlist[i])
    else:
        print("There is no sequence! ")

def gcd(a,b):                       #subprogram care calculeaza cel mai mare divizor comun
    r=1
    if a<b:
        aux=a
        a=b
        b=aux
    a=abs(a)
    b=abs(b)
    while r!=0:
        r=a%b
        a=b
        b=r
    return a

def prime(x):                       #functia de numar prim
    if x==1 or x==0:
        return False
    else:
        for d in range(2,int(x**0.5)+1):
            if x%d==0:
                return False
        return True

def prob1(nlist,n):
    l=1
    max=0
    st=0
    sf=0
    stbun=0
    sfbun=0
    for i in range(1,n):
        if nlist[i-1]>=nlist[i]:
            if l>max:
                max=l
                stbun=st
                sfbun=sf
            st=i
            l=0
        else:
            l+=1
            sf=i
    if l>max:
        max=l
        stbun=st
        sfbun=i
    writesequence(nlist,stbun,sfbun)

def prob3(nlist,n):
    l=1
    max=0
    st=0
    sf=0
    stbun=0
    sfbun=0
    for i in range(1,n):
        if gcd(nlist[i-1],nlist[i])!=1:
            if l>max:
                max=l
                stbun=st
                sfbun=sf
            st=i
            l=0
        else:
            l+=1
            sf=i
    if l>max:
        max=l
        stbun=st
        sfbun=i
    writesequence(nlist,stbun,sfbun)

def prob4(nlist,n):
    max=0
    l=0
    st=0
    sf=0
    stbun=0
    sfbun=0
    for i in range(0,n):
        if prime(nlist[i])==True:
            sf=i
            l+=1
        else:            
            if l>max:
                max=l
                stbun=st
                sfbun=sf
            l=0
            st=i+1
    if l>max:
        max=l
        stbun=st
        sfbun=i
    writesequence(nlist,stbun,sfbun)

def prob5(nlist,n):
    l=1
    max=0
    st=0
    sf=0
    stbun=0
    sfbun=0
    for i in range(1,n):
        if nlist[i-1] != nlist[i]:
            if l>max:
                max=l
                stbun=st
                sfbun=sf
            st=i
            l=0
        else:
            l+=1
            sf=i
    if l>max:
        max=l
        stbun=st
        sfbun=i
    writesequence(nlist,stbun,sfbun)


def prob7(nlist,n):
    l=1
    max=0
    st=0
    sf=0
    stbun=0
    sfbun=0
    for i in range(1,n):
        if prime(abs(nlist[i-1]-nlist[i]))==False:
            if l>max:
                max=l
                stbun=st
                sfbun=sf
            st=i
            l=0
        else:
            l+=1
            sf=i
    if l>max:
        max=l
        stbun=st
        sfbun=i
    writesequence(nlist,stbun,sfbun)
    
def prob8(nlist,n):
    max=0
    l=0
    st=0
    for i in range(0,n):
        if (nlist[i]>=0) and nlist[i]<=10:
            sf=i
            l+=1
        else:            
            if l>max:
                max=l
                stbun=st
                sfbun=sf
            l=0
            st=i+1
    if l>max:
        max=l
        stbun=st
        sfbun=i
    writesequence(nlist,stbun,sfbun)


def start():
    nlist=[7, 4, 1, 2, 3, 9, 7, 1, 1, 1, 5, 14, 3, 9, 7]
    n=15
    x=1
    while x!=0:
        print(nlist)
        printmenu()       
        x=input()
        if x=="0":
            nlist=[]
            n=int(input("Give the number n: "))
            readnumbers(nlist,n)
        elif x=="1":
            print("The longest sequence of strictly increasing numbers: ")
            prob1(nlist,n)
        elif x=="3":
            print("The longest sequence of consecutive number pairs which have the greatest common divisor 1: ")
            prob3(nlist,n)
        elif x=="4":
            print("The longest sequence of prime numbers: ")
            prob4(nlist,n)
        elif x=="5":
            print("The longest sequence of one single number: ")
            prob5(nlist,n)
        elif x=="7":
            print("The longest sequence in wich the difference between the absolute value of consecutive numbers is a prime number: ")
            prob7(nlist,n)
        elif x=="8":
            print("The longest sequence of numbers in [0,10]: ")
            prob8(nlist,n)   
        else:
            break
start()
            
