from time import sleep
import subprocess

# Get time
time_input = input('How many minutes shall I wait? (Default: 60) | ')
time_input = '60' if time_input == '' else time_input
mins = int(time_input) * 60

# Get app
app = input('Which app do you want to close at the end? (Default: Chrome) | ')
app = 'Chrome' if app == '' else app

# Wait x mins
print(f'Ok, closing {app} in {time_input} minutes!')
print('...')
sleep(mins)

# Close selected app
subprocess.call(['osascript', '-e', f'tell application "{app}" to quit'])