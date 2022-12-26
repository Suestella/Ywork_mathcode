import math

#显示主页面
def show_Y():
    print('\n' + " " * 10 + "*****主页面*****" + " " * 10)
    print(" " * 10 + "*****请选择*****" + " " * 10)
    print(" " * 10 + "*****1.Rotundity*****" + " " * 10)
    print(" " * 10 + "*****2.Rectangle*****" + " " * 10)
    print(" " * 10 + "*****3.Triangle*****" + " " * 10)
    print(" " * 10 + "*****4.Sphere*****" + " " * 10)
    print(" " * 10 + "*****5.Cylinder*****" + " " * 10)
    print(" " * 10 + "*****6.Cone*****" + " " * 10)
    print('*' * 50)
# 圆面积
def Rotundity_area(a):
    return math.pi*a*a
# 圆周长
def Rotunduty_circumference(a):
    return 2*math.pi*a
# 矩形面积
def Rectangle_area(a,b):
    return a*b
# 矩形周长
def Rectangle_circumference(a,b):
    return (a+b)*2
# 三角形面积（海伦公式）
def Triangle_area(a,b,c):
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))
# 三角形周长
def Triangle_circumference(a,b,c):
    return a+b+c
# 球体表面积
def Sphere_area(a):
    return 4*math.pi*a*a
# 球体体积
def Sphere_volume(a):
    return (4/3)*math.pi*a*a*a
# 圆柱表面积
def Cylinder_area(a,h):
    return Rotundity_area(a)*2+Rotunduty_circumference(a)*h
# 圆柱体积
def Cylinder_volume(a,h):
    return Rotundity_area(a)*h
# 圆锥表面积
def Cone_area(a,h):
    l = math.sqrt(a*a + h*h)
    return Rotundity_area(a)+math.pi*a*l
# 圆锥体积
def Cone_volume(a,h):
    return (1/3)*Rotundity_area(a)*h

def My_calculator(x):
    a = 0
    b = 0
    c = 0
    h = 0
    # l = 0
    if x == 1 :
        a = eval(input("您已选择圆形，请输入半径："))
        print("圆面积为：" + str(Rotundity_area(a)))
        print("圆周长为：" + str(Rotunduty_circumference(a)))
        return
    elif x == 2:
        a = eval(input("您已选择矩形，请输入第一个边长："))
        b = eval(input("您已选择矩形，请输入第二个边长："))
        print("矩形面积为：" + str(Rectangle_area(a,b)))
        print("矩形周长为：" + str(Rectangle_circumference(a,b)))
        return
    elif x == 3:
        a = eval(input("您已选择三角形，请输入第一个边长："))
        b = eval(input("您已选择三角形，请输入第二个边长："))
        c = eval(input("您已选择三角形，请输入第二个边长："))
        print("三角形面积为：" + str(Triangle_area(a,b,c)))
        print("三角形周长为：" + str(Triangle_circumference(a,b,c)))
        return
    elif x == 4:
        a = eval(input("您已选择球体，请输入半径："))
        print("球体表面积为：" + str(Sphere_area(a)))
        print("球体体积为：" + str(Sphere_volume(a)))
        return
    elif x == 5:
        a = eval(input("您已选择圆柱体，请输入底面圆半径："))
        h = eval(input("您已选择圆柱体，请输入高："))
        print("圆柱表面积为：" + str(Cylinder_area(a,h)))
        print("圆柱体积为：" + str(Cylinder_volume(a,h)))
        return
    elif x == 6:
        a = eval(input("您已选择圆锥体，请输入底面圆半径："))
        h = eval(input("您已选择圆锥体，请输入高："))
        # l = eval(input("您已选择圆锥体，请输入母线："))
        print("圆锥表面积为：" + str(Cone_area(a,h)))
        print("圆锥体积为：" + str(Cone_volume(a,h)))
        return
    else:
        print("输入错误，请重试")
        show_Y()
        x = eval(input())
        My_calculator(x)


if __name__ == '__main__':
    while True:
        show_Y()
        x = eval(input())
        if x == 0:
            break
        My_calculator(x)





