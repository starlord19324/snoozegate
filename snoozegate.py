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


# import pylab
# import numpy
import re
import random



signal_lib = ['10001111',
            '10001101',
            '10001011',
            '10001001',
            '11111011',
            '11001011',
            '11111001',
            '11001001']


def input_check():
    # signal = input('Enter the signal here: ')
    # value = int(input('Determine the value from 0 to 90 here: '))
    signal = '10001001'
    value = int('31')
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
    # print(sig, val)
    return sig, val




def zeroes_environment(signal, value):

    s = list(signal)
    v = list(value)

    matrix_s = []
    matrix_v = []

    for index, item in enumerate(s, 1):
        mask1 = [index,item]
        matrix_s.append(mask1)


    for index, item in enumerate(v, 1):
        mask2 = [index,item]
        matrix_v.append(mask2)

    A = '1'
    N = 0
    while (N < (len(matrix_s)-1)):
        z1 = random.randint(0, len(matrix_s) - 1)
        k1 = matrix_s[z1][1]
        if (k1 == '0'):
            N = len(matrix_s)
            mask_m = []
            mask_m.append(z1)
            mask_m.append(A)
            if (z1 == 0):
                matrix_s[z1].clear()
                matrix_s[z1].extend(mask_m)
            elif (z1 > 0):
                matrix_s[z1 - 1].clear()
                matrix_s[z1 - 1].extend(mask_m)
            L = 0
            result_mm = []
            while L < len(matrix_s):
                result_mm.append(matrix_s[L][1])
                L = L + 1
            result_m = ''.join(result_mm)
            print(result_m)
        else:
            pass


    A = '1'
    N = 0
    while (N < (len(matrix_v)-1)):
        z2 = random.randint(0, len(matrix_v) - 1)
        k2 = matrix_v[z2][1]
        if (k2 == '0'):
            N = len(matrix_v)
            mask_v = []
            mask_v.append(z2)
            mask_v.append(A)
            if (z2 == 0):
                matrix_v[z2].clear()
                matrix_v[z2].extend(mask_v)
            elif (z2 > 0):
                matrix_v[z2 - 1].clear()
                matrix_v[z2 - 1].extend(mask_v)
            L = 0
            result_mv = []
            while L < len(matrix_v):
                result_mv.append(matrix_v[L][1])
                L = L + 1
            result_v = ''.join(result_mv)
            print(result_v)
        else:
            pass


def ones_environment(signal, value):

    s = list(signal)
    v = list(value)

    matrix_s = []
    matrix_v = []

    for index, item in enumerate(s, 1):
        mask1 = [index,item]
        matrix_s.append(mask1)


    for index, item in enumerate(v, 1):
        mask2 = [index,item]
        matrix_v.append(mask2)

    A = '0'
    N = 0
    while (N < (len(matrix_s)-1)):
        z1 = random.randint(0, len(matrix_s) - 1)
        k1 = matrix_s[z1][1]
        if (k1 == '1'):
            N = len(matrix_s)
            mask_m = []
            mask_m.append(z1)
            mask_m.append(A)
            if (z1 == 0):
                matrix_s[z1].clear()
                matrix_s[z1].extend(mask_m)
            elif (z1 > 0):
                matrix_s[z1 - 1].clear()
                matrix_s[z1 - 1].extend(mask_m)
            L = 0
            result_mm = []
            while L < len(matrix_s):
                result_mm.append(matrix_s[L][1])
                L = L + 1
            result_m = ''.join(result_mm)
            print(result_m)
        else:
            pass


    A = '0'
    N = 0
    while (N < (len(matrix_v)-1)):
        z2 = random.randint(0, len(matrix_v) - 1)
        k2 = matrix_v[z2][1]
        if (k2 == '1'):
            N = len(matrix_v)
            mask_v = []
            mask_v.append(z2)
            mask_v.append(A)
            if (z2 == 0):
                matrix_v[z2].clear()
                matrix_v[z2].extend(mask_v)
            elif (z2 > 0):
                matrix_v[z2 - 1].clear()
                matrix_v[z2 - 1].extend(mask_v)
            L = 0
            result_mv = []
            while L < len(matrix_v):
                result_mv.append(matrix_v[L][1])
                L = L + 1
            result_v = ''.join(result_mv)
            print(result_v)
        else:
            pass



def main():
    signal, value = input_check()
    out_sig, out_val = encoder(signal, value)
    zeroes_environment(out_sig, out_val)
    ones_environment(out_sig, out_val)


if __name__ == main():
    main()