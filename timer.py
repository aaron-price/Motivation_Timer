#! /usr/local/bin/python3
from time import sleep
import subprocess

# Get time
time_input = input('How many minutes shall I wait? (Default: 60) | ')
if time_input == '':
    time_input = '60'

# Convert string to int in minutes
mins = int(time_input) * 60

# Get app
app = input('Which app do you want to close at the end? (Default: Chrome) | ')
if app == '':
    app = 'Chrome'

# Wait x mins
print(f'Ok, closing {app} in {time_input} minutes!')
print('...')
sleep(mins)

# Close selected app
subprocess.call(['osascript', '-e', 'tell application "' + app + '" to quit'])