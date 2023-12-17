from turtle import *

bgcolor('black')
speed(0)

colores = ['blue', 'cyan', 'lightgreen', 'yellow', 'red', 'violet']

for i in range(150):
    pencolor(colores[i % 6])
    circle(190 - i / 2, 90)
    left(90)
    circle(190 - i / 3, 90)
    left(60)

done()
