import time
import turtle

face_color = [["#2F200D","#2B1E0D","#2F1F0F","#281C0B","#241808","#261A0A","#2B1E0D","#2A1D0D"],
              ["#2B1E0D","#2B1E0D","#2B1E0D","#332411","#422A12","#3F2A15","#2C1E0E","#281C0B"],
              ["#2B1E0D","#B6896C","#BD8E72","#C69680","#BD8B72","#BD8E74","#AC765A","#342512"],
              ["#AA7D66","#B4846D","#AA7D66","#AD806D","#9C725C","#BB8972","#9C694C","#9C694C"],
              ["#B4846D","#FFFFFF","#523D89","#B57B67","#BB8972","#523D89","#FFFFFF","#AA7D66"],
              ["#9C6346","#B37B62","#B78272","#6A4030","#6A4030","#BE886C","#A26A47","#805334"],
              ["#905E43","#965F40","#41210C","#8A4C3D","#8A4C3D","#45220E","#8F5E3E","#815339"],
              ["#6F452C","#6D432A","#41210C","#421D0A","#45220E","#45220E","#83553B","#7A4E33"]]

def draw_square():
    steve.pendown()
    steve.speed(0)
    steve.forward(87)
    steve.rt(90)
    steve.forward(87)
    steve.rt(90)
    steve.forward(87)
    steve.rt(90)
    steve.forward(87)
    steve.rt(90)
    steve.forward(87)


can_x = 348
can_y = 348

steve = turtle.Turtle()
steve.speed(20)

steve.penup()
steve.goto(-can_x,can_y)
steve.pendown()
steve.goto(can_x,can_y)
steve.goto(can_x,-can_y)
steve.goto(-can_x,-can_y)
steve.goto(-can_x,can_y)
#Init Square DONE

#Next step drawing picels0
steve.penup()
for j in range(8):
    steve.goto(-can_x, can_y)
    for i in range(8):
        #steve.goto(-can_x, can_y)
        steve.begin_fill()
        steve.fillcolor(face_color[j][i])
        draw_square()
        steve.end_fill()
    can_y -= 87
    steve.penup()
time.sleep(5)