def convert24(str1):
#     check last two elemnts of time
# is Am and first two elementsare 12
       if  str1[-2]=='AM' and str1[2]=='12':
            return "00"+str1[2:-2]

        # remove am
       elif str1[-2]=='AM':
           return str1[-2]

       elif str1[-2:]=='PM' and str1[:2]=='12':
           return str1[:-2]
       else:
           return str(int(str1[:2])+12)+str1[2:8]


print(convert24("08:05:45 PM"))