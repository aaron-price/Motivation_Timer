from time import sleep
import subprocess
from datetime import datetime, timedelta
import webbrowser

# Return user input, or a default value.
def inp_default(string, default):
	inp = input(string + f' ({default}) | ')
	return default if inp == '' else inp

# Variables
t_on = int(inp_default('How many minutes on?', '25'))
t_off = int(inp_default('How many minutes off?', '5'))
app = inp_default('Pick an app to close', 'Chrome')
url = inp_default('Which url do you want to open?', 'https://google.com')

def wait(t, action):
	end_time = datetime.now() + timedelta(minutes = t)
	end_time = str(end_time.time())[0:5]
	print(f'{action} {app} at {end_time}.')
	sleep(t * 60)

def run_pom():
	wait(t_on, 'Closing')
	subprocess.call(['osascript', '-e', f'tell application "{app}" to quit'])
	wait(t_off, 'Opening')
	webbrowser.open(url, new=2)
	run_pom()

run_pom()