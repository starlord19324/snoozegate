# -*- coding: utf-8 -*-
import random

####
# Copyright
# Anton Kharchenko
# National Aviation University
# 2019-2020 (c)

####
#
# This matrix contains conventional signals for control of the UAV model
# UAV model will be released soon
# in plans: add octal and hexadecimal libs for variation of signals.
# Explanation of signals meaning:
# '001' - pitch
# '010' - heel
# '100' - yaw
# command - 8 bit, value - 16 bit

signal_lib = ['001',
              '010',
              '100']

# pitch_truth = ['001',
#                '101']
#
# heel_truth = ['010',
#               '011']
#
# yaw_truth = ['100',
#              '110']
#
# error_truth = ['000',
#                '111']

####
#
# input_check function performs verification of input data
# e.g. signal is in library, value (angle of rotation) is in correct range
# will be removed or modified when GUI will be ready - for this stage is useful for testing
#

def input_check():
    # signal = input('Enter the signal here: ')
    # value = int(input('Determine the value from 0 to 90 here: '))
    signal = '001'
    value = int('154')
    if signal in signal_lib and value in range(0, 181):
        # print(signal,value)
        return signal, value
    else:
        print('Incorrect instruction')

####
#
# encoder function encodes obtained value into binary system and adds
# excessive digits to prevent signal noising
# will be also modified for octal and hexadecimal signal systems soon
#

def encoder(signal,value):
    sig = '00000%s' %(signal)
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
    elif value in range(64, 128):
        val = '0%s' %(val)
    elif value in range(128, 181):
        val = '%s' %(val)
    val = '00000000%s' %(val)
    # print(sig, val)
    return sig, val



####
#
# zeroes_environment function simulates noisy environment to make signal distorted
# converts random '0' to '1' and returns distorted signal
# can be used in pair with ones_environment function to increase the distortion level
# will be improved and modified for octal and hexadecimal systems
#

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

    return result_m, result_v


####
#
# ones_environment function simulates noisy environment to make signal distorted
# converts random '1' to '0' and returns distorted signal
# can be used in pair with zeroes_environment function to increase the distortion level
# will be improved and modified for octal and hexadecimal systems
#

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

    return result_m, result_v


pitch_truth = ['001',
               '101']

heel_truth = ['010',
              '011']

yaw_truth = ['100',
             '110']

error_truth = ['000',
               '111']


####
#
# decoder function decodes distorted signals
# removes redundant digits
# performs error correction in correspondence with truth tables
# returns command and value after correction
#

def decoder_lv1(signal, value):
    d_signal = signal[5:]
    d_value = int(value[8:], 2)
    # d_value = '228'
    if d_signal in error_truth:
        d_signal = 'Incorrect instruction: '
    elif d_signal in pitch_truth:
        d_signal = 'Pitch: '
    elif d_signal in heel_truth:
        d_signal = 'Heel: '
    elif d_signal in yaw_truth:
        d_signal = 'Yaw: '
    if d_value in range(0, 181):
        d_value = '%s degrees' %(d_value)
    else:
        d_value = ('Angle (%s degrees) is out of range' %(d_value))
    print(d_signal, d_value)



####
#
# main function - runs called functions together in defined sequence
#

def main():
    signal, value = input_check()
    out_sig, out_val = encoder(signal, value)
    # zeroes_environment(out_sig, out_val)
    c_sig, c_val = ones_environment(out_sig, out_val)
    decoder_lv1(c_sig, c_val)


####
#
# call of main function
#

if __name__ == main():
    main()