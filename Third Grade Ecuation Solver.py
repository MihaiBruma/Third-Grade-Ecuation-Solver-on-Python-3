def SQRT2Function(value) :
    return (value)**(1/2)
def SQRT3Function(value) :
    return (value)**(1/3)
def PowerFunction(value):
    return value*value
def Power3Function(value):
    return value*value*value
def ThirdGradeEcuationSolver(a,b,c,d) :
    print(">>> Your Third Grade Ecuation is : ", a, "x ^ 3", "+", b, "x ^ 2", "+", c,"x","+",d," = 0")
    if a == 0 :
        print(">>> This is not Third Grade Function, because a = 0,"
              " so 0*x^3 + bx^2 + cx + d = 0 => bx^2 + cx + d = 0, this is Second Grade Ecuation")
        if b == 0:
            print(">>> This is not Second Grade Function, because b = 0,"
                  " so 0*x^2 + cx + d = 0 => cx + d = 0, which is First Grade Ecuation")
            print(">>> Your First Grade Ecuation is : ", a, "x", "+", b, "= 0")
            if c == 0:
                print(">>> This is not First Grade Function, because c = 0,"
                      " so 0*x + d = 0 => d = 0, which is not true !")
                exit()
            elif c != 0 :
                while d != 0:
                    if d > 0 and (c > 0 or c < 0):
                        print(">>> Your solution is : ")
                        x = -d / c
                        print(">>>Float value x = ", x)
                        x = int(-d / c)
                        print(">>>Integer value x = ", x)
                        break
                        exit()
                    elif d == 0 and (c > 0 or c < 0):
                        print(">>> Your solution is : ")
                        x = 0
                        print(">>> x = ", x)
                        break
                        exit()
                    elif d < 0 and (c > 0 or c < 0):
                        print(">>> Your solution is : ")
                        x = d / c
                        print(">>>Float value x = ", x)
                        x = int(d / c)
                        print(">>>Integer value x = ", x)
                        break
                        exit()
                    else:
                        print(">>> An Error Occured !")
                        break
                        exit()
        elif b != 0:
            print(">>> Your Second Grade Ecuation is : ", b, "x ^ 2", "+", c, "x", "+", d, " = 0")
            delta = PowerFunction(c) - (4 * b * d)
            print(">>> delta = ", delta)
            if delta > 0:
                if c > 0:
                    print(">>> Your Ecuation has two solutions : x1 & x2")
                    x1 = ((-c) - SQRT2Function(delta)) / (2 * b)
                    x2 = ((-c) + SQRT2Function(delta)) / (2 * b)
                    print(">>>Float value x1 = ", x1)
                    print(">>>Float value x2 = ", x2)
                    x1 = int(((-c) - SQRT2Function(delta)) / (2 * b))
                    x2 = int(((-c) + SQRT2Function(delta)) / (2 * b))
                    print(">>>Integer value x1 = ", x1)
                    print(">>>Integer value x2 = ", x2)
                    exit()
                elif c < 0:
                    print(">>> Your Ecuation has two solutions : x1 & x2")
                    x1 = (c - SQRT2Function(delta)) / (2 * b)
                    x2 = (c + SQRT2Function(delta)) / (2 * b)
                    print(">>>Float value x1 = ", x1)
                    print(">>>Float Value x2 = ", x2)
                    x1 = int((c - SQRT2Function(delta)) / (2 * b))
                    x2 = int((c + SQRT2Function(delta)) / (2 * b))
                    print(">>>Integer value x1 = ", x1)
                    print(">>>Integer value x2 = ", x2)
                    exit()
                else:
                    exit()
            elif delta == 0:
                if c > 0:
                    print(">>> Your Ecuation has only one solution : x")
                    x = (-c) / (2 * b)
                    print(">>>Float value x = ", x)
                    x = int((-c) / (2 * b))
                    print(">>>Integer value x = ", x)
                    exit()
                elif b < 0:
                    print(">>> Your Ecuation has only one solution : x")
                    x = c / (2 * b)
                    print(">>>Float value x = ", x)
                    x = int(c / (2 * b))
                    print(">>>Integer value x = ", x)
                    exit()
                else:
                    exit()
            elif delta < 0:
                print("Ecuation has no solutions, because delta < 0")
                exit()

    elif a != 0 and b != 0 and c != 0 :
        print(">>> Your Third Grade Ecuation is : ", a, "x ^ 3", "+", b, "x ^ 2", "+", c, "x", "+", d, " = 0")
        print(">>> We have next substituion : x = (y-b)/(3*a) ")
        #x = (y-b)/(3*a)
        p = (c/a) - (PowerFunction(b)/(3*PowerFunction(a)))
        q = ((2*Power3Function(b))/(27*Power3Function(a))) - ((b*c)/(3*PowerFunction(a))) + d/a
        print(">>> p = ", p)
        print(">>> q = ", q)
        print(">>> After substitution your Third Grade Ecuation is : ","y^3","+",p,"y","+",q)
        P = SQRT3Function((-q/a)+SQRT2Function(PowerFunction(p/3)+PowerFunction(q/2)))
        Q = SQRT3Function((-q/a)-SQRT2Function(PowerFunction(p/3)+PowerFunction(q/2)))
        print(">>> P = ", p)
        print(">>> Q = ", Q)
        delta0 = Power3Function(p/3) + PowerFunction(q/2)
        indexValue1 = (P+Q) / 2
        indexValue2 = ((P-Q) / 2)*SQRT2Function(3)
        print(">>> delta0 = ", delta0)
        if delta0 < 0 :
            print(">>> Third Grade Ecuation has 3 Real Solutions :")
            y1 = P + Q
            y2 = complex((-indexValue1) + indexValue2)
            y3 = complex((-indexValue1) - indexValue2)
            print(">>> y1 = ", y1)
            print(">>> y2 = ", y2.real)
            print(">>> y3 = ", y3.real)
            exit()
        elif delta0 == 0 :
            print(">>> Third Grade Ecuation has 3 Real Solutions, at least two of them are equal by value :")
            y1 = P + Q
            y2 = complex((-indexValue1) + indexValue2)
            y3 = complex((-indexValue1) - indexValue2)
            print(">>> y1 = ", y1)
            print(">>> y2 = ", y2.real)
            print(">>> y3 = ", y3.real)
            exit()
        elif delta0 > 0 :
            print(">>> Third Grade Ecuation has 3 Solutions,one of them is Real and two Complex :")
            y1 = P + Q
            y2 = complex((-indexValue1) + indexValue2)
            y3 = complex((-indexValue1) - indexValue2)
            print(">>> y1 = ", y1.real)
            print(">>> y2 = ", y2)
            print(">>> y3 = ", y3)
            exit()
        else :
            print(">>> An error occured !")
            exit()

a = int(input(">>> Introduce a = "))
b = int(input(">>> Introduce b = "))
c = int(input(">>> Introduce c = "))
d = int(input(">>> Introduce d = "))
ThirdGradeEcuationSolver(a,b,c,d)