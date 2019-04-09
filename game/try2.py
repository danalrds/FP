# A minimal SQLite shell for experiments

import sqlite3
def printmenu():
    print("1.Add client")
    print("2.Show ")
def showclient():
    con = sqlite3.connect("fisier.db")
    c = con.cursor()
    for row in c.execute("SELECT id,name  FROM clients "):
        print(row)    
    con.commit()
    c.execute("DELETE  FROM clients ")
    for row in c.execute("SELECT id,name  FROM clients "):
        print(row)
    con.commit()
    c.close()
    con.close()
def addclient(id,name):
    con = sqlite3.connect("fisier.db")
    c = con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS clients(id TEXT, name TEXT)")
    c.execute("INSERT INTO clients(id,name) VALUES(id,name)")
    con.commit()
    c.close()
    con.close()
def start():
    while True:
        printmenu()
        x=input()
        if x=="1":
            id=input("id: ")
            name=input("name")
            addclient(id,name)
        elif x=="2":
            showclient()
start()
'''
import sqlite3

class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return "%f;%f" % (self.x, self.y)

con = sqlite3.connect(":memory:")
cur = con.cursor()

p = Point(4.0, -3.2)
cur.execute("select ?", (p,))
print(cur.fetchone())
'''