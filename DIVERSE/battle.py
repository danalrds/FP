from texttable import Texttable


def show():
        
    table = Texttable()
    table.add_row([' ','A', 'B', 'C','D','E','F'])
    for i in range(1,7):        
        table.add_row(board[i])
    return table     

    
board=[[0,0,0,0,0,0,0,],
       [0,0,0,0,0,0,0,],
       [1,0,0,0,0,0,0,],
       [2,0,0,0,0,0,0,],
       [3,0,0,0,0,0,0,],
       [4,0,0,0,0,0,0,],
       [5,0,0,0,0,0,0,],
       ]
print(show().draw())

def delete(x,board):    
    comanda=x.strip()
    com=comanda.split(" ")
    coord=com[1]
    litere=[' ','A','B','C','D','E','F']
    i=1
    for c in com[1]:
        if i %2==1:
            coloana=litere.index(c)
        else:
            linie=int(c)
            board[linie][coloana]='0'
        i+=1
    
    return board


def ship(x,board):    
    comanda=x.strip()
    com=comanda.split(" ")
    coord=com[1]
    litere=[' ','A','B','C','D','E','F']
    i=1
    for c in com[1]:
        if i %2==1:
            coloana=litere.index(c)
        else:
            linie=int(c)
            board[linie][coloana]='*'
        i+=1
    print(show().draw())
    return board
contor=0
while True:
    try:
        x=input("Give coordinates")
        contor=contor+1
        if contor==1:
            first=x
        if contor==2:
            second=x
        print(contor)
        if contor==3:
            board=delete(first,board)
            contor=2
            first=second
            board=ship(x,board)
            second=x
        else:
            board=ship(x,board)
        print(first,second)
    except Exception as exc:
        print(str(exc))
