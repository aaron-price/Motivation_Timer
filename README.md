# Timer

## Set up
1. Download to your computer
2. Open your .bash_profile
3. Insert the following code anywhere:

```bash
function timer() {
    python path/to/timer.py
}
function pomodorro() {
    python path/to/pomodorro.py
}
```

## Caveats
Only works on MacOS

Requires your `python` cli command to use python 3.6+. Check it by running `python --version`. You might need to upgrade or use python3 in the bash functions.

## Usage
#### Simple Timer

Start a new terminal window and type `timer`

It will close your browser (or any other app) after a specified time.

```bash
~/Documents:$ timer
How many minutes shall I wait? (Default: 60) | 45
Which app do you want to close at the end? (Default: Chrome) |
Ok, closing Chrome at 12:10!
...
```

#### Pomodorro Timer

Start a new terminal window and type `pomodorro`

It will endlessly open and close your browser at the specified intervals until you stop the script with `Ctrl + c`

```bash
~/Documents:$ pomodorro
How many minutes on? (25) | 
How many minutes off? (5) | 
Pick an app to close (Chrome) | 
Which url do you want to open? (https://google.com) |
Closing Chrome at 13:56.

```

