# Write a python program which reminds you of drinking water every hour or two. 
# Your program can either beep or send desktop notifications for a specific operating system

from plyer import notification
import time
from os import system

# Use while loop to create notifications indefinetly
while(True):
    #notification
    notification.notify(
        title = "Reminder to take a break",
        message = '''Drink water, take a walk''',
        timeout = 60
    )
    system(f'say Drink water, take a walk')
    # System pause the execution of this programm for 60 minutes
    time.sleep(60*60)