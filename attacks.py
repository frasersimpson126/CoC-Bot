import func as f
import time as t

p = '5554' # port

def Position(n):
    if n == 1:
        f.tap(1000,125,p)
    if n == 2:
        f.tap(1150,240,p)
    if n == 3:
        f.tap(1350,380,p)
    if n == 4:
        f.tap(1560,540,p)
    if n == "c":
        f.tap(1245,370,p)

def Slot(n):  # tap on slot n
    xccord = 225-150
    for x in range(0,n):
        xccord += 150
    f.tap(xccord, 925, p)

def droptrophies():
        f.find(p)
        t.sleep(6)
        Slot(7)
        f.tap(1000,500,p)
        t.sleep(0.5)
        f.tap(135,815,p)
        t.sleep(0.5)
        f.tap(1150,700,p)
        t.sleep(0.5)
        f.tap(900,910,p)

def Sdrag():
    f.swipe(p)
    Slot(1)
    for x in range(1,5): #Super drag
        Position(x)
        Position(x)
        
  
    Slot(2) #clanC
    Position("c")
    
    for x in range(0,4): #heros
        Slot(x+3) 
        Position("c")
        
    Slot(3) #Royal champ ability
    Slot(4) #Archer queen ability
    
    Slot(7)
    for x in range(0,11): # batspell
        Position("c")

    Slot(5) #warden ability
    Slot(6) #king

def MEKKA():
    f.swipe(p)
    Slot(1)
    for x in range(1,5): #MEKKA
        for y in range(0,8):
            Position(x)
        
  
    Slot(2) #clanC
    Position("c")
    
    for x in range(0,4): #heros
        Slot(x+3) 
        Position("c")
        
    Slot(3) #Royal champ ability
    Slot(4) #Archer queen ability
    
    Slot(7)
    for x in range(0,11): # batspell
        Position("c")

    Slot(5) #warden ability
    Slot(6) #king

def BB():
    f.swipe2(p)
    Slot(1)
    f.tap(1535,585,p)
    t.sleep(0.5)

    Slot(2)
    for x in range(6):
        f.tap(1535,585,p)
    for x in range(2,8):
        Slot(x)
    
def BB2():
    f.swipe2(p)
    Slot(1)
    f.tap(1535,585,p)
    Slot(9)
    for x in range(8):
        f.tap(1535,585,p)
    for x in range(2,10):
        Slot(x)
    