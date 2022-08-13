# python program to find time diffrence between two times
# Approch:input=h1=16 m1=20,h2=16,m2=20
# 1.convert both times into minuites
# 2.find diffrence in miutes
# 3.if diffrence are same both are same time
# 4.else convert diffrence in hour minute format and print

def diffrence(h1,m1,h2,m2):
    # 1.convert h1,m2 into minutes
    t1=h1*60+m2
    # 2.convert h2,m2 into minutes
    t2=h2*60+m2

    if t1==t2:
        print("both time are same")
        return
    else:
        diff=t2-t1
        # calculating hours from diffrence
        h=int(diff/60)%24
        # calculating minutes from diffrence
        m=diff % 60
        print(h,":",m)

diffrence(7,20,9,45)
