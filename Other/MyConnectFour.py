from tkinter import *
from random import randint
import time
import sys

class Point():
    def __init__(self,x,y):
        self._x=x 
        self._y=y
    def getX(self):
        return int(self._x)
    def getY(self):
        return int(self._y)
    
class Board():
    def __init__(self):
        self._board=[[-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1]]
    def validare(self,point):
        if point.getX()>=0 and point.getX()<=5 and point.getY()>=0 and point.getY()<=6:
            return True
        return False       
    def valid(self,point):
        if point.getX()>=0 and point.getX()<=5 and point.getY()>=0 and point.getY()<=6:
            if self._board[point.getX()][point.getY()]==-1:
                return True
        return False            
    def makeMove(self,point,user):
        if user=="player":
            u=4                      
        else:
            u=0
          
        if point.getX()>=0 and point.getX()<=5 and point.getY()>=0 and point.getY()<=6:
            if self._board[point.getX()][point.getY()]==-1:
                self._board[point.getX()][point.getY()]=u
            else:
                raise Exception("Square already taken!")
        else:
            raise Exception("Move outside the board!")    
   
    def possibleWin(self,user):
        b=self._board          
        if user=="player":
            suma=11           
        else:
            suma=-1            
        for k in range(0,6):
            for i in range(0,4):
                s=0
                for j in range(i,i+4):
                    s+=b[k][j]
                if s==suma: 
                    for j in range(i,i+4):
                        if b[k][j]==-1:
                            p=self.findpoint(j)
                            if p.getX()==k:
                                return p 
        for col in range(0,7):
            for i in range(0,3):
                s=0
                for j in range(i,i+4):
                    s+=b[j][col]
                if s ==suma:
                    if self.valid(Point(i,col)):
                        next=Point(i,col)
                        return next
        ok=self.este_prima(3,0,suma)
        if ok!=None:            
            return ok
        ok1=self.este_prima(4,0,suma)
        if ok1!=None:            
            return ok1
        ok2=self.este_prima(5,0,suma)
        if ok2!=None:            
            return ok2
        ok3=self.este_prima(5,1,suma)
        if ok3!=None:            
            return ok3
        ok4=self.este_prima(5,2,suma)
        if ok4!=None:            
            return ok4    
        ok5=self.este_prima(5,3,suma)
        if ok5!=None:            
            return ok5   
        
         
        ok=self.este_adoua(2,0,suma)
        if ok!=None:            
            return ok  
        ok=self.este_adoua(1,0,suma)
        if ok!=None:            
            return ok  
        ok=self.este_adoua(0,0,suma)
        if ok!=None:            
            return ok 
        ok=self.este_adoua(0,1,suma)
        if ok!=None:            
            return ok  
        ok=self.este_adoua(0,2,suma)
        if ok!=None:            
            return ok   
        ok=self.este_adoua(0,3,suma)
        if ok!=None:            
            return ok    
        return None
    def calcsuma(self,vect,i):
        b=self._board
        ss=0
        for j in range(i,i+4):
            ss+=b[vect[j][0]][vect[j][1]] 
        return ss
    def este_prima(self,linie,coloana,suma):
        b=self._board
        list=[]                    
        while True:            
            if self.validare(Point(linie,coloana))==True:
                el=(linie,coloana)
                list.append(el)
            else:
                break
            linie=linie-1
            coloana+=1
        n=len(list)                      
        for i in range(0,n-3):
            s=0
            s=self.calcsuma(list, i)                                                    
            if s==suma: 
                                                            
                for j in range(i,i+4):
                    linia=list[j][0]
                    coloana=list[j][1]  
                    if b[linia][coloana] ==-1:                                              
                        pointgasit=self.findpoint(coloana)                        
                        if pointgasit.getX()==linia:
                            return Point(linia,coloana)
                        #if pointgasit==Point(linia,coloana):
                            
                        #    return Point(list[j][0],list[j][1])            
                
        return None
    def este_adoua(self,lin,col,suma):
        b=self._board
        list=[] 
        linie=lin 
        coloana=col           
        while True:            
            if self.validare(Point(linie,coloana))==True:
                el=(linie,coloana)
                list.append(el)
            else:
                break
            linie+=1
            coloana+=1
        n=len(list)
        
        for i in range(0,n-3):
            s=0
            s=self.calcsuma(list, i)
            if s==suma:
                for j in range(i,i+4):
                    linia=list[j][0]
                    coloana=list[j][1]
                    if b[linia][coloana] ==-1:
                        pointfound=self.findpoint(coloana)                        
                        if pointfound.getX()==linia:
                            return Point(linia,coloana) 
              
        return None
    def avMoves(self):
        b=self._board
        moves=[]
        for y in range(0,7):
            for i in range(5,-1,-1):
                if b[i][y]==-1:
                    moves.append(Point(i,y))
                    break   
        #print(len(moves))                          
        return moves
    def isDraw(self):
        if self.avMoves()==[]:
            return True
        return False
    def findpoint(self,col):
        b=self._board
        for i in range(5,-1,-1):
            if b[i][col]==-1:
                return Point(i,col)
        return None      
    def encode(self,nr):
        if nr==-1:
            return '_'
        if nr==0:
            return '@'
        if nr==4:
            return '*'
    def __str__(self):
        result=""
        for line in self._board:
            result+=self.encode(line[0])+"|"+self.encode(line[1])+"|"+self.encode(line[2])+"|"+self.encode(line[3])+"|"+self.encode(line[4])+"|"+self.encode(line[5])+"|"+self.encode(line[6])+"\n"
        return result
            
    def isGameWon(self,lp,cp,la,ca):
        b=self._board
        for k in range(0,6):
            for i in range(0,4):
                s=0
                for j in range(i,i+4):
                    s+=b[k][j]
                if s in [0,16]:
                    return True
        for col in range(0,7):
            for i in range(0,3):
                s=0
                for j in range(i,i+4):
                    s+=b[j][col]
                if s in [0,16]:
                    return True        
                
        ok=self.este_prima2(lp,cp,16,"no")
        if ok==True:
            return True        
        ok=self.este_prima2(la, ca,0,"no")
        if ok==True:
            return True  
        ok=self.este_adoua2(lp,cp,16,"no")
        if ok==True:
            return True        
        ok=self.este_adoua2(la, ca,0,"no")
        if ok==True:
            return True              
        return False
    def este_prima2(self,linie,coloana,suma,ms):
        b=self._board
        list=[]       
        s=linie+coloana
        if s>=5:
            linie=5
        else:
            linie=s
        coloana=s-linie        
        while True:            
            if self.validare(Point(linie,coloana))==True:
                el=(linie,coloana)
                list.append(el)
            else:
                break
            linie=linie-1
            coloana+=1
        n=len(list)
        
        for i in range(0,n-3):
            s=0
            for j in range(i,i+4):
                s+=b[list[j][0]][list[j][1]]
            if s==suma:
                if ms=="yes":
                    for j in range(i,i+4):
                        if b[list[j][0]][list[j][1]] ==-1:
                            linia=list[j][0]
                            coloana=list[j][1]
                            if self.findpoint(coloana)==Point(linia,coloana):
                                return Point(list[j][0],list[j][1]) 
                    return None 
                else:
                    return True      
                
        return None
    def este_adoua2(self,lin,col,suma,ms):
        b=self._board
        list=[]       
        if lin<col:
            linie=0
            coloana=col-lin
        else:
            linie=lin-col
            coloana=0      
        while True:            
            if self.validare(Point(linie,coloana))==True:
                el=(linie,coloana)
                list.append(el)
            else:
                break
            linie+=1
            coloana+=1
        n=len(list)
        
        for i in range(0,n-3):
            s=0
            for j in range(i,i+4):
                s+=b[list[j][0]][list[j][1]]
            if s==suma:
                if ms=="yes":
                    for j in range(i,i+4):
                        if b[list[j][0]][list[j][1]] ==-1:
                            linia=list[j][0]
                            coloana=list[j][1]
                            if self.findpoint(coloana)==Point(linia,coloana):
                                return Point(list[j][0],list[j][1]) 
                    return None 
                else:
                    return True 
                
        return None
    
    
class Game():
    def __init__(self,board):
        self.__board=board
    def makeMoveAI(self,lp,cp,la,ca):
        next=self.__board.possibleWin("ai")
        if next!=None:            
            self.__board.makeMove(next,"ai")            
            return next           
        else:
            contra=self.__board.possibleWin("player")
            if contra!=None:
                self.__board.makeMove(contra,"ai")   
                return contra             
            else:
                availableMoves=self.__board.avMoves()
                randMove=randint(0,len(availableMoves)-1)
                self.__board.makeMove(availableMoves[randMove],"ai")   
                return availableMoves[randMove]             
    def makeMovePlayer(self,point):
        self.__board.makeMove(point,"player")        
    def getBoard(self):
        return self.__board 

class UserInterface():
    def __init__(self,game,parent):
        crtPlayer=4
        self.lp=0
        self.la=0
        self.cp=0
        self.ca=0
        self.__game=game
        self.labels = [] #lista cu cele 42 pozitii
        self.turn_counter = 0 #numarul de miscari pe tabla
        self.win_status = 0 #daca s-a castigat jocul
        
        self.empty_image = PhotoImage(file = "assets/empty.gif") #All slots begin with an "empty" image
        
        self.blue_image = PhotoImage(file = "assets/blue.gif") #Blue slots
        self.red_image = PhotoImage(file = "assets/red.gif") #Red slots
        
        #define piece dimensions
        self.height = 100
        self.width = 100
        
        for i in range(42):
            self.labels.append(Label(parent,
                                     image = self.empty_image,
                                     bg = "white", #background is white, can be changed
                                     width = self.width,
                                     height = self.height, #restricted to 96 so the images have no gaps
                                     ))
        
    
        #Places slots in grid
        piece_index = 0 #every piece has a unique identifier
        for c in range(7): #pieces are numbered from left to right
            for r in range(6,0,-1): #pieces are numbered bottom to top (hence the -1)
                self.labels[piece_index].grid(row = r,
                                              column = c,
                                              padx = 0,
                                              pady = 0,
                                              sticky = S) #places pieces in grid
         
                self.labels[piece_index].bind("<Button-1>", lambda event, coords = (r,c): self.column_click(event, coords)) #coordinates of each piece are passed to column_click
                piece_index += 1
        #self.__start()
         
    def column_click(self, event, coords):
        print("Turn", self.turn_counter + 1, "request to column", coords[1])
        if self.__game.getBoard().isGameWon(self.lp,self.cp,self.la,self.ca)==False and self.__game.getBoard().isDraw()==False:          
            point=self.__game.getBoard().findpoint(coords[1])
            try:
                self.__game.makeMovePlayer(point)  
                self.lp=point.getX()
                self.cp=point.getY()
                print(self.lp,self.cp)
                crtPlayer=0
                self.turn_counter+=1
                self.redraw(self.cp, self.lp, 4)
                if self.__game.getBoard().isGameWon(self.lp,self.cp,self.la,self.ca)==True:                       
                    blue_win.display_win_message()
            except Exception as exc:
                print(exc)
            if self.__game.getBoard().isGameWon(self.lp,self.cp,self.la,self.ca)==False:
                point=self.__game.makeMoveAI(self.lp,self.cp,self.la,self.ca)
                self.la=point.getX()
                self.ca=point.getY()
                print(self.la,self.ca)
                crtPlayer=4
                self.turn_counter+=1
                self.redraw(self.ca, self.la,0)
                if self.__game.getBoard().isGameWon(self.lp,self.cp,self.la,self.ca)==True:                       
                    red_win.display_win_message()
            if self.__game.getBoard().isDraw()==True:
                tie_win.display_win_message()
        else:            
            print("Game has already been won!")
    def redraw(self, c_ord, r_ord, piece_state): 

        self.c_ord = c_ord
        r_ord=5-r_ord
        self.r_ord = r_ord
        print(r_ord,c_ord)
        self.piece_state = piece_state

        piece_index = r_ord + 6 * c_ord #recalculate unique piece identifier from 0 to 42 by row and column

        if self.piece_state == 4:
            self.labels[piece_index].configure(image = self.blue_image)
            for i in range(42):
                root.configure(cursor="@assets/cursor_red.cur")
        elif self.piece_state == 0:
            self.labels[piece_index].configure(image = self.red_image)
            for i in range(42):
                root.configure(cursor="@assets/cursor_blue.cur")        
        
      
    def __start(self):        
        crtPlayer=4
        lp=0
        la=0
        cp=0
        ca=0
        while self.__game.getBoard().isGameWon(lp,cp,la,ca)==False and self.__game.getBoard().isDraw()==False:            
            if crtPlayer==4:
                print(self.__game.getBoard()) 
                y=int(input("Y coord: "))
                point=self.__game.getBoard().findpoint(y)
                try:
                    self.__game.makeMovePlayer(point)  
                    lp=point.getX()
                    cp=point.getY()                                    
                    crtPlayer=0
                except Exception as exc:
                    print(exc)
            else:
                point=self.__game.makeMoveAI(lp,cp,la,ca)
                la=point.getX()
                ca=point.getY() 
                crtPlayer=4
        print(self.__game.getBoard())
        if self.__game.getBoard().isGameWon(lp,cp,la,ca)==True:
            if crtPlayer==4:
                print("Computer has won.")
            elif crtPlayer==0:
                print("Human has won.")
        else:
            if self.__game.getBoard().isDraw()==True:
                print("It is a draw.")
class Win_message:
    def __init__(self, root, team):
        
        self.root = root
        self.team = team
        self.frame_status = 0
        self.total_frame_num = 21 #length of GIF anim in frames
        self.frame_delay = 30 #in ms
        #grid contraction variables
        self.grid_total_frame_num = 9 #controls duration of contraction
        self.grid_multiplier = 3 #controls speed of contraction
        #button slide variables
        self.current_height = -0.1 #also the starting height
        self.final_height = 0.32 #actual stopping height will be greater and a multiple of increment_height
        self.increment_height = 0.02 #as a proportion of the window space
        #cursor animation variables
        self.cursor_state = 0
        self.cursor_total_states = 17 #multiples of 8 + 1 for the full loop
        self.cursor_delay = 100

        #refresh button, does the same as "play again"
        self.refresh_image = PhotoImage(file = "assets/refresh.gif")
        self.refresh_button = Label(image = self.refresh_image, bg = "#FFFFFF")
        self.refresh_button.place(relx = 0, rely = 0)
        self.refresh_button.bind("<Button-1>", lambda event: self.again())      

    #load animation frames. This is an individual method because it does not need to be called on 'Play Again', whereas everything else in __init__() needs to be reset.
    def load_frames(self):
        #print("Load frames")
        self.frames = []    
        #loads each frame to the list self.frames
        for i in range(self.total_frame_num):
            
            self.frames.append(PhotoImage(file = self.team, format = "gif -index " + str(i)))
            

    #create the two buttons just once
    def place_buttons(self):
        #print("Place buttons")
        game.win_status = 1 #game has been won, prevents slots from being clicked
        self.button_again = Button(text = "Play Again",
                                   command = self.again,
                                   height = 4,
                                   width = 20)
        self.button_again.place(relx = 0.25, rely = self.current_height)

        self.button_quit = Button(text = "Quit",
                                  command = self.quit_game,
                                  height = 4,
                                  width = 20)
        self.button_quit.place(relx = 0.55, rely = self.current_height)
        
        self.animate_buttons() #begin animation of buttons

    #animate the two buttons
    def animate_buttons(self):
        #print("Animate buttons")
        #drop the play again / quit buttons down
        if self.current_height < self.final_height:
            self.button_again.place(rely = self.current_height)
            self.button_quit.place(rely = self.current_height)
            self.current_height += self.increment_height
            
            self.root.after(self.frame_delay, self.animate_buttons)

    #animate the main win banner            
    def win_animation(self):
        #print("Win animation")
        self.winlabel = Label(background = "white", image = self.frames[self.frame_status])#creates label from first frame
        self.winlabel.place(relx = 0.5, rely = 1, anchor = S)
        
        for i in range(42):
            ui.labels[i].lift() #pulls banner below the pieces
        
        if self.frame_status < self.total_frame_num:
            self.frame_status += 1 #cycles to next frame
            
        self.winlabel.configure(image = self.frames[self.frame_status - 1]) #refreshes frame
        #print("Displaying frame", self.frame_status)

        if self.frame_status < self.grid_total_frame_num:            
            for i in range(42):
                ui.labels[i].configure(height = 100 - self.frame_status * self.grid_multiplier) #contracts grid at the same time as animated banner
        
        if self.frame_status < self.total_frame_num:
            self.root.after(self.frame_delay, self.win_animation) #keeps updating the image every 20ms
        else:
            self.place_buttons() #triggers button fall AFTER animation is complete to avoid a bug

  
    #initiates animations. Allows them to be split into their own methods.
    def display_win_message(self):
        #print("Display the massage")
        self.win_animation()
        
    def again(self):
        root.configure(cursor = "@assets/cursor_blue.cur")
        #restart board and memory
        for i in range(0,42):
            ui.labels[i].grid_forget()
              
        GameBoard.__init__()
        ui.__init__(game,root)
        blue_win.__init__(root, "blue")
        red_win.__init__(root, "red")        
                
    def quit_game(self): #Contains both methods because one does not work in the IDE
        root.destroy()
        sys.exit()         



root = Tk()
root.resizable(width=FALSE, height=FALSE)
root.geometry("728x624")
root.configure(bg="white", cursor="@assets/cursor_blue.cur")
root.title("Connect Four")
blue_win = Win_message(root, 'assets/bluewin.gif')
red_win = Win_message(root, 'assets/redwin.gif')
tie_win = Win_message(root, 'assets/tiewin.gif')
blue_win.load_frames()
red_win.load_frames()
tie_win.load_frames()

GameBoard=Board()
game=Game(GameBoard)
ui=UserInterface(game,root)

