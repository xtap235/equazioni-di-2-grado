from math import sqrt

while True:
    a = float(input("insert a: "))
    b = float(input("insert b: "))
    c = float(input("insert c: "))
    delta = (b**2)-4*a*c
    radicedelta = sqrt(delta)
    x1 = (-b + radicedelta) / (2*a)
    x2 = (-b - radicedelta) / (2*a)

    print("delta",delta,sep="=")
    print("x1",x1,sep="=")
    print("x2",x2,sep="=")
