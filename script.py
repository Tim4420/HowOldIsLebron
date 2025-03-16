from datetime import datetime
from time import sleep
birthdate = datetime(1984, 12, 29, 16, 4, 0) 

def gettime():
    time = (datetime.now()) - birthdate
    years = int(time.days) // 365
    days = time.days - years*365
    hours, remainder = divmod(time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"\rTime since {birthdate.strftime('%Y-%m-%d %H:%M:%S')}: "
          f"{years} years, {days} days, {hours:02d}:{minutes:02d}:{seconds:02d}", end='')

while True:        
    gettime()
    sleep(1)