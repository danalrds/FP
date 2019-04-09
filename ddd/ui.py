from tests import *
from functions import *
def start(expenseslist,undolist):               #main function that reads the command and solves the problem    
    while True:
        try:
            cmd = input("Enter command: ")   
            cmd = readCommand(cmd)        
            command = cmd[0]
            params = cmd[1]
            '''Tratez cazurile add, remove, replace si list '''
            if command == 'add':            
                add_command(expenseslist, params,undolist)
            elif command == 'remove':
                remove_command(expenseslist, params,undolist)
            elif command == 'replace':
                replace_command(expenseslist, params,undolist)
            elif command == 'list':
                list_command(expenseslist, params)
            elif command == 'sum':
                sum_command(expenseslist, params)
            elif command == 'max':
                max_command(expenseslist, params)
            elif command == 'sort':
                sort_command(expenseslist, params)
            elif command == 'filter':
                filter_command(expenseslist, params,undolist)
            elif command == 'undo':                                   
                expenseslist=undo_command(undolist,expenseslist)
            elif command == 'help':
                help_command()
            elif command == 'exit':
                break    
            else:
                print("Invalid command!")
        except ValueError as e:
            print("Message error:",e)

def start2(expenseslist,undolist):                #main second function that reads the command and solves the problem
    expenseslist = []
    undolist=[]
    testInit(expenseslist)
    while True:
        try:
            printmenu()
            x=input()
            cmd=[]
            if x=='1':
                cm=input("Give the number of the apartment: ")
                cm2=input("Give the tipe of expense: ")
                cm3=input("Give the amount: ")
                cmd='add '+cm+' '+cm2+' '+cm3            
                cmd = readCommand(cmd)             
                params = cmd[1]
                add_command(expenseslist, params,undolist)
            elif x=='2':
                cm=input("Give the apartment: ")
                cmd='remove '+cm
                cmd = readCommand(cmd)             
                params = cmd[1]
                remove_command(expenseslist, params,undolist)
            elif x=='3':
                start=int(input("Give the start position: "))
                fin=int(input("Give the final position: "))
                remove_expense_fromto(expenseslist,start,fin,undolist)                
            elif x=='4':
                tipes=input("Give the type/types of expense you want to remove : ")
                cmd='remove '+tipes
                cmd = readCommand(cmd)             
                params = cmd[1]
                remove_command(expenseslist, params,undolist)
            elif x=='5':
                nr=input("Give the number of apartment: ")
                tip=input("Give the type of expense: ")
                amount=input("Give the new amount: ")
                cmd='replace '+nr+' '+tip+' with '+amount
                cmd = readCommand(cmd)             
                params = cmd[1]
                replace_command(expenseslist, params,undolist)
            elif x=='6':
                listall(expenseslist)
            elif x=='7':
                nr=int(input("Give the number of apartment: "))
                listbyapartment(expenseslist,nr)                
            elif x=='8':
                sign=input("Give the sign: ")
                value=int(input("Give the value: "))
                listbyexpenses(expenseslist,sign,value)
            elif x=='9':
                tip=input("Give the type of expense: ")
                cmd='sum '+tip
                cmd = readCommand(cmd)             
                params = cmd[1]
                sum_command(expenseslist, params)
            elif x=='10':
                nr=input("Give the number of apartment: ")
                cmd='max '+nr
                cmd = readCommand(cmd)             
                params = cmd[1]
                max_command(expenseslist, params)
            elif x=='11':
                cmd='sort apartment'            
                cmd = readCommand(cmd)             
                params = cmd[1]
                sort_command(expenseslist, params)
            elif x=='12':            
                cmd='sort type'
                cmd = readCommand(cmd)             
                params = cmd[1]
                sort_command(expenseslist, params)
            elif x=='13':
                tip=input("Give the type of expense: ")
                remove_type(expenseslist,tip)
            elif x=='14':
                value=int(input("Give the value: "))
                remove(expenseslist,value)                
            elif x=='15':
                expenseslist=undo_command(undolist,expenseslist)
            else:
                break
        except ValueError as e:
            print("Message error:",e)
            
def choose():    
    expenseslist = []
    undolist=[]
    testInit(expenseslist)
    print("1.For command-based interface enter 1")
    print("2.For menu-based interface enter 2")
    val=int(input())
    if val==1:
        start(expenseslist,undolist)
    elif val==2:
        start2(expenseslist,undolist)
    else:
        print("Invalid choice")
def testall():    
    testaddexpense()
    testfindById()
    testfindbyid()
    testchecktype()
    testremove_expenses()
    testremove_expenses_type()
    testremove_expense_fromto()
    testreplace_command()
    testmaximum()
    testsort()
    testfilter_command()
    testundo_command()
testall()
choose()

