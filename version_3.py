
import time

i = 0
frames = [
    u"\U00057344  \U00057344",
    u"\U00057344 \U00057344",
    u"\U00057344\U00057344",
    u"\U00057344 \U00057344",
    u"\U00057344  \U00057344",
]
while True:
    # Cool use of a control character.
    print(f".... {frames[i]} ....", end='\r')
    i+=1
    i = i % 4
    time.sleep(.5)
