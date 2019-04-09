import unittest
def evensum(list):
    s=0
    c=0
    l=[]
    if type(list)!=type(l):
        raise TypeError("must be a list")
    for nr in list:
        if nr %2==0:
            s+=nr
            c+=1
    if c==0:
        raise ValueError("No even numbers!")
    return s

def test():
    list=[0,1,2,4]    
    s=0
    s=evensum(list)
    print(s)
    assert s==6
    try:
        list=[1,3,5]
        s=evensum(list)
        assert s==5
    except:
        AssertionError
        print("no even numbers!")
    try:
        list=4
        s=evensum(list)
        assert s==5
    except:
        AssertionError
        print("must be a list!")
test()

def function(n):
    d = 2
    while (d < n - 1) and n % d > 0:
        d += 1
    return d >= n - 1
def test_function():
    ok=function(0)
    print(ok)  
test_function()
