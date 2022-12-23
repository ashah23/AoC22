import math

def op0(old):
    return modulo(old * 3)

def op1(old):
    return modulo(old + 7)

def op2(old):
    return modulo(old + 5)

def op3(old):
    return modulo(old + 8)

def op4(old):
    return modulo(old + 4)

def op5(old):
    return modulo(old * 2)

def op6(old):
    return modulo(old + 6)

def op7(old):
    return modulo(old * old)

def modulo(num):
    return num % 9699690

m0 = [78, 53, 89, 51, 52, 59, 58, 85]
c0 = 0

m1 = [64]
c1 = 0

m2 = [71, 93, 65, 82]
c2 = 0

m3 = [67, 73, 95, 75, 56, 74]
c3 = 0

m4 = [85, 91, 90]
c4 = 0

m5 = [67, 96, 69, 55, 70, 83, 62]
c5 = 0

m6 = [53, 86, 98, 70, 64]
c6 = 0

m7 = [88, 64]
c7 = 0

for round in range(10000):
    if round % 500 == 0:
        print(str(round))
    ## go thru each monkey
    ## count += size of their list
    ## iterate thru list and perform op

    ## Monkey 0
    c0 += len(m0)
    while len(m0) > 0:
        old = m0[0]
        m0.remove(old)
        new = math.floor(op0(old))
        if new % 5 == 0:
            m2.append(new)
        else:
            m7.append(new)
    
    ## Monkey 1
    c1 += len(m1)
    while len(m1) > 0:
        old = m1[0]
        m1.remove(old)
        new = math.floor(op1(old))
        if new % 2 == 0:
            m3.append(new)
        else:
            m6.append(new)

    ## Monkey 2
    c2 += len(m2)
    while len(m2) > 0:
        old = m2[0]
        m2.remove(old)
        new = math.floor(op2(old))
        if new % 13 == 0:
            m5.append(new)
        else:
            m4.append(new)   
            
    ## Monkey 3
    c3 += len(m3)
    while len(m3) > 0:
        old = m3[0]
        m3.remove(old)
        new = math.floor(op3(old))
        if new % 19 == 0:
            m6.append(new)
        else:
            m0.append(new)

    ## Monkey 4
    c4 += len(m4)
    while len(m4) > 0:
        old = m4[0]
        m4.remove(old)
        new = math.floor(op4(old))
        if new % 11 == 0:
            m3.append(new)
        else:
            m1.append(new)

    ## Monkey 5
    c5 += len(m5)
    while len(m5) > 0:
        old = m5[0]
        m5.remove(old)
        new = math.floor(op5(old))
        if new % 3 == 0:
            m4.append(new)
        else:
            m1.append(new)

    ## Monkey 6
    c6 += len(m6)
    while len(m6) > 0:
        old = m6[0]
        m6.remove(old)
        new = math.floor(op6(old))
        if new % 7 == 0:
            m7.append(new)
        else:
            m0.append(new)

    ## Monkey 7
    c7 += len(m7)
    while len(m7) > 0:
        old = m7[0]
        m7.remove(old)
        new = math.floor(op7(old))
        if new % 17 == 0:
            m2.append(new)
        else:
            m5.append(new)

print("Monkey0: " + str(c0))
print("Monkey1: " + str(c1))
print("Monkey2: " + str(c2))
print("Monkey3: " + str(c3))
print("Monkey4: " + str(c4))
print("Monkey5: " + str(c5))
print("Monkey6: " + str(c6))
print("Monkey7: " + str(c7))