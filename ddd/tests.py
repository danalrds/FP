from functions import *
def testaddexpense():
    expenseslist=[]
    testInit(expenseslist)
    addexpense(expenseslist,(25,'gas',100))
    assert expenseslist==[(1, 'gas', 100), (2, 'water', 80), (2, 'heating', 200), (2, 'electricity', 170), (5, 'gas', 225), (6, 'water', 400), (7, 'electricity', 855), (8, 'heating', 90), (9, 'water', 432), (10, 'gas', 184),(25,'gas',100)]

def testfindById():
    expenseslist=[]
    addexpense(expenseslist,(25,'gas',100))
    addexpense(expenseslist,(40,'water',200))
    addexpense(expenseslist,(35,'heating',450))
    pos=findById(expenseslist,40,'water')
    assert pos==1
    pos=findById(expenseslist,35,'heating')
    assert pos==2

def testfindbyid():
    expenseslist=[]
    addexpense(expenseslist,(25,'gas',100))
    addexpense(expenseslist,(40,'water',200))
    addexpense(expenseslist,(35,'heating',450))
    pos=findbyid(expenseslist,40)
    assert pos==1
    pos=findbyid(expenseslist,35)
    assert pos==2

def testchecktype():
    expenseslist=[]
    addexpense(expenseslist,(25,'gas',100))
    addexpense(expenseslist,(40,'water',200))
    addexpense(expenseslist,(35,'heating',450))
    pos=checktype(expenseslist,'gas')
    assert pos==0
    pos=checktype(expenseslist,'heating')
    assert pos==2

def testremove_expenses():
    expenseslist=[]
    undolist=[]
    addexpense(expenseslist,(25,'gas',100))
    addexpense(expenseslist,(40,'water',200))
    addexpense(expenseslist,(35,'heating',450))
    assert remove__expenses(expenseslist,40,undolist)
    assert expenseslist==[(25,'gas',100),(35,'heating',450)]

def testremove_expenses_type():
    expenseslist=[]    
    addexpense(expenseslist,(25,'gas',100))
    addexpense(expenseslist,(40,'water',200))
    addexpense(expenseslist,(35,'gas',450))
    assert remove__expenses_type(expenseslist,'gas')
    assert expenseslist==[(40,'water',200)]

def testremove_expense_fromto():
    expenseslist=[]
    undolist=[]
    addexpense(expenseslist,(25,'gas',100))
    addexpense(expenseslist,(26,'gas',369))
    addexpense(expenseslist,(27,'water',100))
    addexpense(expenseslist,(40,'water',200))
    addexpense(expenseslist,(35,'gas',450))
    remove_expense_fromto(expenseslist,25,30,undolist)
    assert expenseslist==[(25,'gas',100),(40,'water',200),(35,'gas',450)]

def testreplace_command():
    expenseslist=[]
    undolist=[]
    addexpense(expenseslist,(25,'gas',100))
    addexpense(expenseslist,(40,'water',200))
    addexpense(expenseslist,(35,'gas',450))
    replace_command(expenseslist,['','35','gas','with','900'],undolist)
    assert expenseslist==[(25,'gas',100),(40,'water',200),(35,'gas',900)]

def testmaximum():    
    expenseslist=[]
    testInit(expenseslist)
    max=maximum(expenseslist)
    assert max==10

def testsort():    
    expenseslist=[]
    s=[]
    addexpense(expenseslist,(25,'gas',100))
    addexpense(expenseslist,(40,'water',200))
    addexpense(expenseslist,(35,'gas',450))
    addexpense(expenseslist,(10,'gas',4560))
    addexpense(expenseslist,(25,'water',5000))
    s=sort_apartments(expenseslist)
    s=sort(s)   
    assert s==[(40, 200), (35, 450), (10, 4560), (25, 5100)]

def testfilter_command():
    expenseslist=[]
    undolist=[]
    addexpense(expenseslist,(25,'gas',100))
    addexpense(expenseslist,(40,'water',200))
    addexpense(expenseslist,(35,'heating',450))
    addexpense(expenseslist,(45,'gas',187))
    filter_command(expenseslist,['','gas'],undolist)
    assert expenseslist==[(25,'gas',100),(45,'gas',187)]

def testundo_command():
    expenseslist=[]
    testInit(expenseslist)
    remove__expenses_type(expenseslist,'gas')
    assert expenseslist==[(2, 'water', 80), (2, 'heating', 200), (2, 'electricity', 170), (6, 'water', 400), (7, 'electricity', 855), (8, 'heating', 90), (9, 'water', 432)]
    
