import math
import turtle
bob = turtle.Turtle()
# 输出一个长为length的n边形，所有更抽象
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    print(t)
    turtle.mainloop()

# 它画一个近似圆，边长要足够多才行,这个圆只根r有关，其它的是内部操作,r确定了，就确定了周长，有了总长度，确定一下边长length，得出多少条边n
#def circle(t, r):
#    # 计算周长：
#    circ = 2 * math.pi * r
#    n = 50
#    length = circ / n
#    for i in range(n):
#        t.fd(length)
#        t.lt(360/n)
#    print(t)
#    turtle.mainloop()

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)


circle(bob, 80)

# 这个函数就不能用画圆的思路了，而是
def arc(t, r, angle):
    circumference = angle * r
    n = int(circumference / 3) + 1
    length = circumference / n
    for i in range(n):
        t.fd(length)
        t.lt(angle/n)
    print(t)
    turtle.mainloop()

def circle(t, r):
    arc(t, r, 2*math.pi)


arc(bob, 40, 30)

"""  
def circle(t, r):
    cir = 2 * math.pi * r
    n = int(cir / 3) + 1
    length = cir / n
    polygon(t, length, n)

def arc(t, r, angle):
    cir = 2 * math.pi * r
    n = int(cir / 3) + 1
    length = cir / n
    m = angle/360
    x = m * n

    for i in range(x):
        t.fd(length)
        t.lt(360/x)
    print(t)
    turtle.mainloop()

#arc(bob, 90, 180)
circle(bob)

"""