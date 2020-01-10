# snoozegate
Repo for my bachelor diploma project

useful links: 
https://python-scripts.com/animations-with-matplotlib
https://docs.python.org/3/library/random.html

Just code
GUI
Drone actions modulation


Signals library
Encoder and decoder
Few levels of noised environments
Modulation of drone actions


Inputting the signal
Encoding the signal
Stressing the signal (noised environment)
Decoding the signal
Sending the signal to the drone


# Signals library:

# Actions:
Only binary values
in 4 binary bits
00001111 - dry-down
00001000 - dry-up
00000100 - dry-left
00000010 - dry-right
11110100 - left+down
10000100 - left+up
11110010 - right+down
10000010 - right+up

## Values:
Only positive integer values in degrees
from 0 to 180
would be converted into 8-bit binary