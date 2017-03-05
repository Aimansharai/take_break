import time
import webbrowser
import random

hours = input ('Enter the number of hours you will be styding:')
total_breaks =  input ('Enter the number of breaks you want to take:')
message = ('Music will be played in your browser every break')
print message
break_count = 0

m_selection= ['https://www.youtube.com/watch?v=v4GIfNf7AYk', 'https://www.youtube.com/watch?v=papuvlVeZg8', 'https://www.youtube.com/watch?v=papuvlVeZg8']
secure_random = random.SystemRandom()
timer = hours/total_breaks

while (break_count < total_breaks ):
    time.sleep(timer*60*60)
    webbrowser.open(secure_random.choice(m_selection))
    break_count = break_count + 1
