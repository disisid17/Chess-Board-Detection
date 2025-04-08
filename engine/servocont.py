import time
from ..engine.pigtest import angler
from ..engine.uites import coord_Move as cords
from ..engine.uites import plana as plan
from ..chessgame.stock import b2cord
import math
agrip = False

def pivot(ang):
    angler(min(max(2*ang+90,0),180),0)
def open():
    agrip = True
    angler(70,3)#gripper
    # Turn servo 40 degrees from center
def close():
    agrip = False
    angler(5,3)#gripper
    # Turn servo 40 degrees from center
def armgle():
    if agrip:
        close()
    else:
        open()
def bmap(y,x):
    x=(x+4)
    y=(y-4)*14/8 
    a=math.atan2(y,x)
    l=x/math.cos(a)
    return(l,math.degrees(a))
    #return(x,y)
def resPos():
    cords(3,2)
    pivot(0)
    time.sleep(1)
def mov(move,z=0):
    g = b2cord(move)
    print(g)
    c=g[2]
    #resPos()
    d,t=plan(c[1],c[0]-3.5)
    print(d,t)
    cords(d,z)
    pivot(t)
resPos()
time.sleep(1)
close()
time.sleep(1)
armgle()
time.sleep(1)
armgle()
time.sleep(1)
mov("g7e5")
time.sleep(1)
open()
time.sleep(1)
mov("g7e5",-3)
time.sleep(1)
close()
time.sleep(1)
resPos()
time.sleep(1)
mov("b7e5")
time.sleep(1)
time.sleep(1)
mov("b7e5",-3)
time.sleep(1)
open()
#cords(d,0)
time.sleep(1)
resPos()
time.sleep(1)
