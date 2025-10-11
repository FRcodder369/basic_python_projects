import time
import datetime
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('alarm.mp3')

def set_alarm():
    alarm_time = input('enter the alarm time you want to wake up (HH:MM:SS): ')
    now = datetime.datetime.now().strftime('%H:%M:%S')

    while now != alarm_time:
        print(now)
        time.sleep(1)
        now = datetime.datetime.now().strftime('%H:%M:%S')

    print('WAKE UP')


order = 'set'
while order != 'exit':

    if order == 'set':
        pygame.mixer.music.stop()
        set_alarm()
        pygame.mixer.music.play(-1)

    elif order == 'snooze':
        print('Snoozing... 😴')
        pygame.mixer.music.pause()
        time.sleep(10)
        pygame.mixer.music.unpause()


    else:
        print('Have a nice day!')
        break

    order = input('Do you want to set the alarm again, snooze or exit? (set/ snooze/ exit): ').lower()




