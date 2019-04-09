def Initlist(list):
    ''' function that initializez the list with flights
      returns the initialized list'''
    list=[]
    list.append(('0B3002',45,'Cluj-Napoca','London'))
    list.append(('0C2',40,'Ankara','London'))
    list.append(('0B347802',48,'London','Ryad'))
    list.append(('05689D',56,'Taipei','London'))
    list.append(('0754J',36,'Cluj-Napoca','Beijing'))
    list.append(('0B32',100,'Cluj-Napoca','Maldive'))
    list.append(('0CCC02',78,'Cluj-Napoca','Singapore'))
    list.append(('0B39999',523,'Cluj-Napoca','Canberra'))
    list.append(('0B3ST',78,'Sydney','London'))
    list.append(('0T02',47,'Cluj-Napoca','Ulan Bator'))
    return list

def printmenu():
    '''function that prints the menu '''
    print("1.Add a flight")
    print("2.Delete a flight")
    print("3.Show all flights with a given departure city sorted  by their destination city")
    print("4.Increase the duration of a flight")
    print("5.List")
    print("6.Exit")
    
'''function that adds a flight
input:list, code, time,dep,dest
if code,dep,dest have the length >=3 and time>=20 the flight will be added
otherwise a message error will be sent'''

def add(list,code,time,dep,dest):
    if len(code)<3 or len(dep)<3 or len(dest)<3 or time<20:
        raise ValueError("Code,departure,detination must have len>=3 and time must be >=20")
    else:
        list.append((code,time,dep,dest))
        
''' function that prints the list of flights'''

def listall(list):
    for l in list:
        print("Code",l[0],"Time:",l[1],l[2],l[3])

''' function that finds the position of a certain flight code in the list
input: list and code
otput: the position or -1 if the code doesn't exist'''

def find(list,code):
    for i in range(0,len(list)):
        if list[i][0]==code:
            return i
    return -1

''' function that removes a flight with a given code
input:list code
if the code is in the list the flight will be deleted'''
def remove(list,code):
    poz=find(list,code)
    if poz!=-1:
        list.pop(poz)
    else:
        raise ValueError("Inexistent code!")
    
''' function that sorts all the flights by the destination city
input:unsorted list
output:sorted list'''

def sort(rezults):
    ok=True
    while ok==True:
        ok=False
        for i in range(0,len(rezults)-1):
            if rezults[i][3]>rezults[i+1][3]:
                aux=rezults[i]
                rezults[i]=rezults[i+1]
                rezults[i+1]=aux
                ok=True
    return rezults

''' function that shows all the flights with the dep city given sorted increasingly by dest city
input:list,dep
if there are flughts with the given departure city they will be sorted and printed '''

def show_dep(list,dep):
    rezults=[(t[0],t[1],t[2],t[3]) for t in list if t[2]==dep]
    if len(rezults)>0:
        rezults=sort(rezults)
        listall(rezults)
    else:
        print("There are no flights with this departure city!")
        
'''function that finds the first position of a given departure city in the list
input:list and dep
output: the position or -1 if there is no such elemnet'''

def find_dep(list,dep):
    for i in range(0,len(list)):
        if list[i][2]==dep:
            return i
    return -1

''' function that increases the time for all flights with the given dep city
if time is in [10,60] and there are flights with the dep city that was given their time will be modified'''

def increase(list,dep,time):
    poz=find_dep(list,dep)    
    if time>=10 and time <=60:
        if poz!=-1:
            for i in range(0,len(list)):
                if list[i][2]==dep:
                    object=list[i]                
                    code=object[0]
                    timp=object[1]
                    dest=object[3]
                    timp=timp+time
                    list[i]=(code,timp,dep,dest)                
                
        else:
            print("There are no flights with this departure city!")
    else:
        raise ValueError("Time must be in [10,60]!")
def test_Initlist():
    list=[]
    list=Initlist(list)
    assert list==[('0B3002',45,'Cluj-Napoca','London'),('0C2',40,'Ankara','London'),('0B347802',48,'London','Ryad'),('05689D',56,'Taipei','London'),
                  ('0754J',36,'Cluj-Napoca','Beijing'),('0B32',100,'Cluj-Napoca','Maldive'),('0CCC02',78,'Cluj-Napoca','Singapore'),('0B39999',523,'Cluj-Napoca','Canberra'),
                  ('0B3ST',78,'Sydney','London'),('0T02',47,'Cluj-Napoca','Ulan Bator')]
    
def test_add():
    list=[]
    list.append(('0B3002',45,'Cluj-Napoca','London'))
    list.append(('0C2',40,'Ankara','London'))
    add(list,'0B347802',48,'London','Ryad')
    assert list==[('0B3002',45,'Cluj-Napoca','London'),('0C2',40,'Ankara','London'),('0B347802',48,'London','Ryad')]

def test_remove():
    list=[]
    list.append(('0B3002',45,'Cluj-Napoca','London'))
    list.append(('0C2',40,'Ankara','London'))
    remove(list,'0C2')
    assert list==[('0B3002',45,'Cluj-Napoca','London')]
def test_sort():
    list=[]
    list.append(('0B3002',45,'Cluj-Napoca','London'))
    list.append(('0C2',40,'Ankara','Beijing'))
    list=sort(list)
    assert list==[('0C2',40,'Ankara','Beijing'),('0B3002',45,'Cluj-Napoca','London')]
def test_increase():
    list=[]
    list.append(('0B3002',45,'Cluj-Napoca','London'))
    list.append(('0C2',40,'Ankara','Beijing'))
    increase(list,'Cluj-Napoca',50)
    assert list==[('0B3002',95,'Cluj-Napoca','London'),('0C2',40,'Ankara','Beijing')]
    
def testall():
    test_Initlist()
    test_add()
    test_remove()
    test_sort()
    test_increase()
def start():
    list=[]
    list=Initlist(list)
    while True:
        try:
            printmenu()
            x=input("Enter command:")
            if x=='1':
                code=input("Give the code of the flight: ")
                time=int(input("Give the duration of the flight: "))
                dep=input("Give the departure city: ")
                dest=input("Give the destination city: ")
                add(list,code,time,dep,dest)
            elif x=='2':
                code=input("Give the code of the flight: ")
                remove(list,code)
            elif x=='3':
                dep=input("Give the departure city: ")
                show_dep(list,dep)
            elif x=='4':
                dep=input("Give the departure city: ")
                time=int(input("Give the number of minutes to increase: "))
                increase(list,dep,time)
            elif x=='5':
                listall(list)
            elif x=='6':
                break
            else:
                print("Invalid command!")
        except ValueError as e:
            print("Message error:",e)
testall()
start()
