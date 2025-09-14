
import time

i = 0
frames = [u"\U00057344",u"\U00057345",u"\U00057346", u"\U00057347"]
while True:
    print(f".... {frames[i]} ....", end='\r')
    i+=1
    i = i % 4
    time.sleep(.5)
