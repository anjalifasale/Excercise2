import time

def countdown(t):
    while t:
        mins,sec=divmod(t,60)
        timer='{:02d}:{:02d}'.format(mins,sec)
        print(timer,end='\r')
        time.sleep(1)
        t-=1

    print("fire in hole")

t=input("enter time in sec")
countdown(int(t))
