from time import sleep
import subprocess
from datetime import datetime, timedelta

# Get time
time_input = input('How many minutes shall I wait? (Default: 60) | ')
time_input = '60' if time_input == '' else time_input
mins = int(time_input) * 60
end_time = datetime.now() + timedelta(minutes = int(time_input))

# Get just the hour:minutes
end_time = str(end_time.time())[0:5]

# Get app
app = input('Which app do you want to close at the end? (Default: Chrome) | ')
app = 'Chrome' if app == '' else app

# Wait x mins
print(f'Ok, closing {app} at {end_time}!')
print('...')
sleep(mins)

# Close selected app
subprocess.call(['osascript', '-e', f'tell application "{app}" to quit'])