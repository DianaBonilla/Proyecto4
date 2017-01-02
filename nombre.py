## Diana Bonilla
## Primer nombre
## Uso de la libreria turtle

import turtle
from turtle import *
import os
turtle.setup(1300, 600)
win = turtle.Screen()
win.bgcolor("black")
##title("DIANA")
t = turtle.Pen()
t.reset()
## LETRA D
def letraD():
    t.left(180)
    t.forward(400)
    t.left(180)
    t.color(1,0,1)
    t.begin_fill()
    t.left(90) ## inicio de la D
    t.forward(200) ## lado vertical
    t.right(90)
    t.forward(100) ## lado horizontal
    t.right(45) ## giro
    t.forward(50)
    t.right(45)
    t.forward(130)
    t.left(315) ## giro
    t.forward(50)
    t.left(315)
    t.forward(100)
    t.backward(25)
    t.right(90) ## inicio de la parte interna
    t.end_fill()
    t.forward(170)
    t.right(90)
    
    t.color(1,1,1) ## color en la parte interna
    t.begin_fill()
    t.forward(70)
    t.right(45) ## giro
    t.forward(30)
    t.right(45)
    t.forward(100)
    t.left(315)
    t.forward(30)
    t.right(45)
    t.forward(70)
    t.end_fill()

    t.color(1,0,1)
    t.begin_fill()
    t.left(90) ## salida
    t.forward(27)
    t.end_fill()


## LETRA I
def letraI():
    t.left(90) ## paso a la siguiente
    t.forward(220)
    t.color(0,0,1)
    t.begin_fill()
    t.left(90) ## inicio
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(100)## subida
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100) ## base
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.end_fill()

## LETRA A
def letraA():
    t.forward(50)## paso a la siguiente
    t.color(1,0,1)
    t.begin_fill()
    t.left(90)
    t.forward(80) ## lateral izquierdo corto
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(80) ## lateral derecho corto
    t.left(90)
    t.forward(30)
    t.left(90) 
    t.forward(200) ## lateral derecho largo
    t.left(90)
    t.forward(100) ## base superior
    t.left(90)
    t.forward(200)
    t.end_fill()
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(170)
    t.right(90)
    t.color(1,1,1)
    t.begin_fill()
    t.forward(40) ##parte interna
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(40)
    t.end_fill()
    t.color(1,0,1) ## paso a la siguiente
    t.begin_fill()
    t.left(90)
    t.forward(30) ## lateral izquierdo corto
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(80) ## lateral derecho corto
    t.left(90)
     

## LETRA N
def letraN():
    t.forward(80) ## base
    
    t.color(0,0,1)
    t.begin_fill()
    t.left(90)
    t.forward(170) ## inicio de la N
    t.left(215)
    t.forward(210)
    t.left(55) ## angulo de la N
    t.forward(30)
    t.left(90)
    t.forward(200) ## lateral derecho
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(160) ## lateral interno derecho
    t.right(145) ## angulo de la N superior
    t.forward(200)
    t.left(55)
    t.forward(35)
    t.left(90)
    t.forward(203)
    t.end_fill()
    t.left(90) ## nuevo inicio
    t.forward(30)
    t.left(90)
    t.forward(170) ## inicio de la N
    t.left(215)
    t.forward(210)
    t.left(55) ## angulo de la N
    t.forward(20)
    

    
    
    
    
    
letraD()
letraI()
letraA()
letraN()
letraA()






