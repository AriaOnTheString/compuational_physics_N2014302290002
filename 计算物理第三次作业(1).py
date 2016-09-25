a="#   # ##### #   #  ###   ###  #   # ##  #"
b="#   # #      # #    #     #   #   # ##  #"
c="##### #####   #     #     #   #   # # # #"
d="#   # #       #     #   # #   #   # #  ##"
e="#   # #####   #    ###  ###    ###  #   #"
import time
import os
op=0
while op<120:
    i = os.system('cls')
    time.sleep(0.02)
    a, b,c,d,e=" "+a, " "+b, " "+c," "+d," "+e
    print (a)
    print (b)
    print (c)
    print (d)
    print (e)
    op=op+1