# Just code
# GUI
# Drone actions modulation


# Signals library
# Encoder and decoder
# Few levels of noised environments
# Modulation of drone actions


# Inputting the signal
# Encoding the signal
# Stressing the signal (noised environment)
# Decoding the signal
# Sending the signal to the drone


### Signals library:
#
## Actions:
# Only binary values
# in 4 binary bits
# 10001111 - dry-down
# 10001100 - dry-up
# 10001010 - dry-left
# 10001001 - dry-right
# 11111010 - left+down
# 11001010 - left+up
# 11111001 - right+down
# 11001001 - right+up
#
## Values:
# Only positive integer values in degrees
# from 0 to 180
# would be converted into 8-bit binary


import random


signal_lib = ['10001111',
            '10001100',
            '10001010',
            '10001001',
            '11111010',
            '11001010',
            '11111001',
            '11001001']


def input_check():
    # signal = input('Enter the signal here: ')
    value = int(input('Determine the value from 0 to 90 here: '))
    signal = '10001111'
    # value = int('31')
    if signal in signal_lib and value in range(0, 91):
        # print(signal,value)
        return signal, value
    else:
        print('Incorrect instruction')


def encoder(signal,value):
    sig = '00000000%s' %(signal)
    val = bin(value)
    val = val[2:]
    if value in range(0,2):
        val = '0000000%s' %(val)
    elif value in range(2, 4):
        val = '000000%s' %(val)
    elif value in range(4, 8):
        val = '00000%s' %(val)
    elif value in range(8, 16):
        val = '0000%s' %(val)
    elif value in range(16, 32):
        val = '000%s' %(val)
    elif value in range(32, 64):
        val = '00%s' %(val)
    elif value in range(64, 91):
        val = '0%s' %(val)
    val = '00000000%s' %(val)
    print(sig, val)


def environment(signal,value):
    p1 = 0.17
    p2 = 0.24



def main():
    sig, val = input_check()
    encoder(sig, val)


if __name__ == main():
    main()