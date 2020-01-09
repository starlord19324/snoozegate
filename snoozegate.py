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
# 00001111 - dry-down
# 00001000 - dry-up
# 00000100 - dry-left
# 00000010 - dry-right
# 11110100 - left+down
# 10000100 - left+up
# 11110010 - right+down
# 10000010 - right+up
#
## Values:
# Only positive integer values in degrees
# from 0 to 180
# would be converted into 8-bit binary


signal_lib = ['0000', '1000', '0100', '0010',
       '1100', '1010', '0011', '0101']


def input_check(signal,value):
    if signal in signal_lib:
        print(signal)
        # return signal
    else:
        print('Incorrect instruction')
    if value in range(0,181):
        print(value)
        # return value
    else:
        print('Incorrect value')


# def encoder(signal,value):
    # sig = '00%s00' %(signal)
    # val =
    # print(sig,value)



def main():
    signal = input('Enter the signal here: ')
    value = int(input('Determine the value from 0 to 180 in 4 digits (e.g. 0162) here: '))
    input_check(signal,value)
    encoder(signal,value)


if __name__ == main():
    main()