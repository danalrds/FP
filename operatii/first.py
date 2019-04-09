'''
  Goia Daniela Informatica Engleza grupa 913
'''
def printmenu():
    print("1.Enter operation")
    print("2.Enter conversion")
    print("3.Show formats")
    print("0.Exit")
def printmenu2():
    print("1.Enter addition")
    print("2.Enter subtraction")
    print("3.Enter multiplication")
    print("4.Enter division")
    print("5.Rapid conversion between bases 2,4,8,16 with sourcebase<destbase")
    print("6.Rapid conversion between bases 2,4,8,16 with sourcebase>destbase")
    print("7.Succesive divisions and multiplications sourcebase<destbase ")
    print("8.Succesive divisions and multiplications sourcebase>destbase ")
    print("9.Show formats")
    print("0.Exit")
def help():
    print("The needed formats for operations are:")
    print("a+b(base)")
    print("a-b(base)")
    print("a*b(base)")
    print("a/b(base)")
    print("\n")
    print("The needed format for conversions are:")
    print("a(source base)>destination base\n")
def creare(numar,base,sign):
    vector=[]    
    for i in range(0,len(numar)):
        if numar[i] in "ABCDEF":
            if numar[i]=="A":
                vector.append(10)                
            elif numar[i]=="B":
                vector.append(11)             
            elif numar[i]=="C":
                vector.append(12)             
            elif numar[i]=="D":
                vector.append(13)             
            elif numar[i]=="E":
                vector.append(14)             
            elif numar[i]=="F":
                vector.append(15) 
            if vector[i]>=base:
                raise ValueError("One of the numbers is not in the given base")            
        else:
            w=int(numar[i])
            vector.append(w) 
            if vector[i]>=base:
                raise ValueError("One of the numbers is not in the given base")
    if sign=="/" or sign=="conv":
        return vector
    else:
        vect=vector
        vector=[]
        for i in range(len(vect)-1,-1,-1):
            vector.append(vect[i])  
        return vector
def afisare(nr1,base,sign):
    string=""
    i=len(nr1)-1     
    if sign=="-" :      
        while nr1[i]==0:
            nr1.pop(i)  
            i=len(nr1)-1           
    if sign=="/":        
        while nr1[0]==0:
            nr1.pop(0)
            
    if sign=="/" or sign=="//":
        lenn=0
        limit=len(nr1)
        inc=1
    else:
        lenn=len(nr1)-1
        limit=-1
        inc=-1
    for i in range(lenn,limit,inc):
        if nr1[i]<=9:
            string=string+str(nr1[i]) 
        else:
            if nr1[i]==10:
                st="A"
            elif nr1[i]==11:
                st="B"
            elif nr1[i]==12:
                st="C"
            elif nr1[i]==13:
                st="D"
            elif nr1[i]==14:
                st="E"
            else:
                st="F"
            string=string+st
    string=string+"("+str(base)+")"
    if sign=="/" or sign=="//":
        return string
    else:
        print(string) 
              

def to10(nr,base):
    number=0
    p=1
    while nr>0:
        number=number+(nr % 10)*p
        p=p*base
        nr=nr//10
    return number

def compute(op):
    sign=""
    if "+" in op:
        sign="+"
    elif "-"in op:
        sign="-"
    elif "*" in op:
        sign="*"
    elif "/" in op:
        sign="/"
    else:
        raise ValueError("This is not a valid opeartion ")
    if sign !="":
        nr1=[]
        nr2=[]
        a=op[:op.find(sign)]
        b=op[op.find(sign)+1:op.find("(")]
        base=op[op.find("(")+1:op.find(")")]
        base=int(base)               
        nr1=creare(a,base,sign)
        nr2=creare(b,base,sign)       
        if sign=="+":
            aduna(nr1,nr2,base)
        elif sign=="-":
            scade(nr1,nr2,base)  
        elif sign=="*":
            inmulteste(nr1,nr2,base)              
        elif sign=="/":            
            imparte(nr1,nr2,base)
            
     

def aduna(nr1,nr2,base):
    minte=0
    if len(nr1)>len(nr2):
        max=len(nr1) 
        for i in range(0,max-len(nr2)):
            nr2.append(0)
    elif len(nr2)>len(nr1):       
        max=len(nr2)
        for i in range(max-len(nr1)):
            nr1.append(0)
    else:
        max=len(nr1)
    for p in range(0,max):         
        nr1[p]=nr1[p]+nr2[p]+minte
        minte=0
        aux=0
        if nr1[p]>=base:
            aux=nr1[p]
            nr1[p]=nr1[p] % base
            minte=aux// base             
    if minte>0:
        nr1.append(minte)  
    afisare(nr1,base,"+")      
def scade(nr1,nr2,base):
    minte=0
    if len(nr1)>len(nr2):
        max=len(nr1) 
        for i in range(0,max-len(nr2)):
            nr2.append(0)
    elif len(nr2)>len(nr1):       
        max=len(nr2)
        for i in range(max-len(nr1)):
            nr1.append(0)
    else:
        max=len(nr1)
    for p in range(0,max):
        if nr1[p]<nr2[p]+minte:
            nr1[p]=nr1[p]+base-nr2[p]-minte
            minte=1
        else:
            nr1[p]=nr1[p]-nr2[p]-minte
            minte=0     
    afisare(nr1,base,"-")
    
def inmulteste(nr1,nr2,base):
    minte=0
    digit=nr2[0]
    for p in range(0,len(nr1)):         
        nr1[p]=nr1[p]*digit+minte
        minte=0
        aux=0
        if nr1[p]>=base:
            aux=nr1[p]
            nr1[p]=nr1[p] % base
            minte=aux// base             
    if minte>0:
        nr1.append(minte)  
    afisare(nr1,base,"*")  
    
def imparte(nr1,nr2,base):    
    cat=nr1[0]    
    digit=nr2[0]
    nr2=[]
    i=0
    while i<=len(nr1):        
        #cat=to10(cat,base)
        nr2.append(cat//digit)      
        cat=cat%digit
       
        i+=1
        
        if i==len(nr1):
            i=len(nr1)+5
        else:
            cat=cat*base+nr1[i]    
    string=afisare(nr2,base,"/")
    print("quotient " +string)
    nr1=[]
    nr1.append(cat)
    st=''
    st=afisare(nr1,base,"//")
    print("remainder "+st)    
                      
    '''                               CONVERSII               '''

def putere(x):
    i=0
    while x % 2==0:
        x=x // 2
        i=i+1
    return i
def baza2(nr):
    x=[]    
    while nr / 2!=0:
        x.append(nr % 2)
        nr=nr // 2
    xx=[]
    xx=x
    x=[]    
    for i in range(len(xx)-1,-1,-1):
        x.append(xx[i])
    
    return x
def bazat2(v):
    nr=0
    p=1
    for i in range(len(v)-1,-1,-1):
        nr=nr+p*v[i]
        p=p*2    
    return nr
def transforma_in2(vect,a):
    p=putere(a)
    new=[]
    for i in range(0,len(vect)):
        nr=vect[i]
        v=[]
        v=baza2(vect[i])
        if len(v)<p:
            for j in range(0,p-len(v)):
                new.append(0)
            for j in range(0,len(v)):
                new.append(v[j])
        else:
            for j in range(0,len(v)):
                new.append(v[j])
   
    return new
def transforma_din2(vect,a):
    p=putere(a)    
    while len(vect)%p!=0:
        vect.insert(0,0)
    fin=len(vect)
    new=[]
    for i in range(0,fin,p):
        v=[]
        for j in range(i,i+p):
            v.append(vect[j])
        cif=bazat2(v)
        new.append(cif)
    
    return new 

    '''        Calculation in destination base when source<dest  '''
def convert_from10(x,base):
    y=[]
    p=1
    while x!=0:
        y.append(x % base)
        x= x // base     
    return y
def mic_mare(vect,source,dest):
    s=0;
    p=1
    for i in range(len(vect)-1,-1,-1):
        s=s+vect[i]*p
        p=p*source
    y=convert_from10(s,dest)    
    afisare(y,dest,"")

def mare_mic(vect,source,dest):       
    digit=dest
    new=[]
    nr2=[]
    while True:
        nr2=[]
        cat=vect[0] 
        i=0
        while i<=len(vect):        
            #cat=to10(cat,base)
            nr2.append(cat//digit)      
            cat=cat%digit
       
            i+=1
        
            if i==len(vect):
                i=len(vect)+5
            else:
                cat=cat*source+vect[i]        
        if nr2[0]==0 :
            nr2.pop(0)            
        
        vect=[]
        vect=nr2
        new.append(cat)
        if len(nr2)==0:
            break
    afisare(new,dest,"")    
    
def compute_conv(op):   
    a=op[:op.find("(")]
    source=op[op.find("(")+1:op.find(")")]
    dest=op[op.find(">")+1:]
    source=int(source)
    dest=int(dest)    
    nr1=creare(a,source,"conv") 
    if source in [2,4,8,16] and dest in [2,4,8,16]:
        if source<dest:
            vector=nr1
            if source!=2:
                vector=transforma_in2(nr1, source)
            vect=transforma_din2(vector, dest)
            while vect[0]==0:
                vect.pop(0)
            string=afisare(vect, dest, "//")
            print(string)
        else:
            vector=transforma_in2(nr1, source)
            vect=transforma_din2(vector, dest)
            while vect[0]==0:
                vect.pop(0)
            string=afisare(vect, dest, "//")        
            print(string)    
    elif source<dest:
        mic_mare(nr1,source,dest)
    else:
        mare_mic(nr1,source,dest)
def start():
    while True:
        try:
            printmenu()
            x=input()
            if x=="1":
                op=input("Write operation:\n")
                compute(op)
            elif x=="2":
                op=input("Write conversion: \n")
                compute_conv(op)
            elif x=="3":
                help()
            elif x=="0":
                break
            else:
                print("Invalid command!") 
        except ValueError as e:
            print("Message error: ",e)
def start2():
    while True:
        try:
            printmenu2()
            x=input()
            if x=="1":
                op=input("Write addition:\n")
                compute(op)
            elif x=="2":
                op=input("Write subtraction:\n")
                compute(op)
            elif x=="3":
                op=input("Write multiplication:\n")
                compute(op)
            elif x=="4":
                op=input("Write division:\n")
                compute(op)
            elif x=="5" or x=="6" or x=="7" or x=="8":
                op=input("Write conversion: \n")
                compute_conv(op)
            elif x=="9":
                help()
            elif x=="0":
                break
            else:
                print("Invalid command!") 
        except ValueError as e:
            print("Message error: ",e)
start()