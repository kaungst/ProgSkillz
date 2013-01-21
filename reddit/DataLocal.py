"""
takes in string from stdin with keys for datetime
correctly outputs datetime
useful for translating different time standards

keys: "%l": Milliseconds (000 to 999) "%s": Seconds (00 to 59)
      "%m": Minutes (00 to 59) "%h": Hours (in 1 to 12 format) 
      "%H": Hours (in 0 to 23 format) "%c": AM / PM (regardless of hour-format) 
      "%d": Day (1 up to 31) "%M": Month (1 to 12) "%y": Year (four-digit format)
"""
from datetime import datetime

info = list(raw_input("What kind of time do you want?\n"))
now = datetime.now()
h12 = now.hour%12
dLight = 'PM' if now.hour >= 12 else 'AM'

stuff = {'l':now.microsecond, 's':now.second, 'm':now.minute,
         'h':h12, 'H':now.hour, 'c':dLight,
         'd':now.day, 'M':now.month, 'y':now.year}

for c in range(len(info)):
    if info[c] == '%':
        info[c] = ''
        info[c+1] = str(stuff[info[c+1]])

print ''.join(info)
        
