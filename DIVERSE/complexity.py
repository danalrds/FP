'''
Created on Dec 6, 2016

@author: Arthur
'''
from datetime import datetime
from texttable import Texttable

'''
    1. Here we have two implementation for the Fibonacci sequence
'''
def fibonacciIterative(n):
    '''
    Iterative implementation for computing n-th term of the Fibonacci sequence
    '''
    if n == 0:
        return 0
    x = 0
    y = 1
    for i in range(1, n):
        z = x + y
        x = y
        y = z
    return y


def fibonacciRecursive(n):
    '''
    Recursive implementation for computing n-th term of the Fibonacci sequence
    '''
    if n < 2:
        return n
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)

'''
    2. We test them to see they work correctly
'''
def testFibonacci():
    fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for i in range(0, len(fib)):
        assert fibonacciIterative(i) == fib[i], (i, fibonacciIterative(i))
        assert fibonacciRecursive(i) == fib[i]
                                 
testFibonacci() 

'''
    3. Let's see how quick each implementation is
'''

def toMiliseconds(start, end):
    '''
    Function to convert a timedelta into miliseconds
    input:
        start, end - timedelta objects
    output:
        Number of miliseconds
    '''
    diff = end - start
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return int(millis)

def speedTestFibonacci(term):
        t1 = datetime.now()
        fibonacciIterative(term)
        t2 = datetime.now()
        fibonacciRecursive(term)
        t3 = datetime.now()
        return (toMiliseconds(t1 , t2), toMiliseconds(t2, t3))

'''
    NB!
    To run the function below, you must have installed the texttable component from:
    https://github.com/foutaise/texttable
'''
def buildResultTable():
    table = Texttable()
    table.add_row(['Term', 'Iterative', 'Recursive'])
    for term in [10, 20, 30, 32, 34, 36]:
        row = speedTestFibonacci(term)
        table.add_row([term, row[0], row[1]])
    return table     
       
if __name__ == "__main__":       
    print(buildResultTable().draw())
        
'''
    In case you cannot run the example, this is what it is supposed to look like:
    
    +------+-----------+-----------+
    | Term | Iterative | Recursive |
    +------+-----------+-----------+
    | 10   | 0         | 0         |
    +------+-----------+-----------+
    | 20   | 0         | 3         |
    +------+-----------+-----------+
    | 30   | 0         | 357       |
    +------+-----------+-----------+
    | 32   | 0         | 937       |
    +------+-----------+-----------+
    | 34   | 0         | 2440      |
    +------+-----------+-----------+
    | 36   | 0         | 6437      |
    +------+-----------+-----------+
    
    NB!
    0 miliseconds is not really 0, it's just too short to measure accurately
'''
