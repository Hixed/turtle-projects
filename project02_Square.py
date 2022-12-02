# importing turtle module 
from turtle import * 
bgcolor("black")
#colors
colors_list = ["blue", "red", "white" , "yellow"]
speed(0)
for i in range(1000):
    #set colors
    pencolor(colors_list[i%4]) 
    forward(i * 4)
    #(360 / 4) - 1
    right(89)
done() 
