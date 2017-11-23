# Timer

Sets a timer which will close an application on your computer after a certain time.

By default, it will close Chrome after 1 hour.

# Usage
1. Download to your computer
2. Open your .bash_profile
3. Insert the following line:

```bash
function timer() {
    python path/to/timer.py
}
```

Now start a new terminal window and type `timer`

```bash
~/Documents:$ timer
How many minutes shall I wait? (Default: 60) | 45
Which app do you want to close at the end? (Default: Chrome) |
Ok, closing Chrome in 45 minutes!
...
```

# Caveats
Only works on MacOS