## DIANA BONILLA
##ESTRELLA CON PUNTAS N

import turtle
import os
win = turtle.Screen()
win.bgcolor("lightblue")
t = turtle.Pen()
t.reset()
n = int(input("Ingrese un numero: "))

if n % 2 == 0:
    a = 360/n 
    b = 360 - a
    t.right(45)
##    for x in range(0,n): ##sirve solo con 8 12 16 etc
##        t.forward(100)
##        t.left(180-(360/n))
    for i in range(n):
        t.forward(100)
        t.right(a)
        for i in range(3):
            t.color(0,0,1)
            t.begin_fill()
            t.forward(100)
            t.right(120)
            t.end_fill()
        for i in range(4):
            t.color(1,0,1)
            t.begin_fill()
            t.forward(100)
            t.right(90)
            t.end_fill()
else:
    an = 180/n
    an2= 180-an

    t.reset()
    for x in range(n):
        t.color(1,1,0)
        t.begin_fill()
        t.forward(300)
        t.left(an2)
        t.end_fill()
turtle.getscreen()._root.mainloop()
