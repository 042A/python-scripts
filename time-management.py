#LEARNT TODAY: DON'T NAME YOUR FILES THE SAME AS THE LIBS...

import time 
import datetime
from datetime import date

# GET NOW TIME UNIXDATE
t = time.time()
print (t)  

# GET NOW TIME DATE
print (time.gmtime()) 
#VARIATION
time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(t))
time.strftime('%Y-%m-%d %H:%M %Z', time.gmtime(t))


# CONVERT UNIX DATE TO DATE
print (time.ctime(int("1284101485")))
print (time.strftime("%D %H:%M", time.localtime(int("1284101485"))))

# CONVERT DATE TO UNIX DATE
d = date(2014, 10, 27)
unixtime = time.mktime(d.timetuple())
print (unixtime)