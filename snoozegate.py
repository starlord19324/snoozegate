# -*- coding: utf-8 -*-
import random
from collections import Counter

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
    # action = input('Enter the action here: ')
    # angle = int(input('Determine the angle from 0 to 90 here: '))
    # acceleration = int(input('Determine the value from 0 to 90 here: '))
    action = '001'
    angle = int('154')
    acceleration = int('51')
    if action in signal_lib and angle in range(0, 181) and acceleration in range(1, 256):
        # print(signal,value)
        return action, angle, acceleration
    else:
        print('Incorrect instruction')

####
#
# encoder function encodes obtained value into binary system and adds
# excessive digits to prevent signal noising
# will be also modified for octal and hexadecimal signal systems soon
#

def encoder(action, angle, acceleration):
    act = '00000%s' %(action)

    ang = bin(angle)
    ang = ang[2:]

    if angle in range(0, 2):
        ang = '0000000%s' % (ang)
    elif angle in range(2, 4):
        ang = '000000%s' % (ang)
    elif angle in range(4, 8):
        ang = '00000%s' % (ang)
    elif angle in range(8, 16):
        ang = '0000%s' % (ang)
    elif angle in range(16, 32):
        ang = '000%s' % (ang)
    elif angle in range(32, 64):
        ang = '00%s' % (ang)
    elif angle in range(64, 128):
        ang = '0%s' % (ang)
    elif angle in range(128, 181):
        ang = '%s' % (ang)
    ang = '00000000%s' %(ang)


    acc = bin(acceleration)
    acc = acc[2:]

    if acceleration in range(0, 2):
        acc = '0000000%s' % (acc)
    elif acceleration in range(2, 4):
        acc = '000000%s' % (acc)
    elif acceleration in range(4, 8):
        acc = '00000%s' % (acc)
    elif acceleration in range(8, 16):
        acc = '0000%s' % (acc)
    elif acceleration in range(16, 32):
        acc = '000%s' % (acc)
    elif acceleration in range(32, 64):
        acc = '00%s' % (acc)
    elif acceleration in range(64, 128):
        acc = '0%s' % (acc)
    elif acceleration in range(128, 181):
        acc = '%s' % (acc)
    acc = '00000000%s' %(acc)

    # print(act, ang, acc)
    return act, ang, acc



####
#
# zeroes_environment function simulates noisy environment to make signal distorted
# converts random '0' to '1' and returns distorted signal
# can be used in pair with ones_environment function to increase the distortion level
# will be improved and modified for octal and hexadecimal systems
#

def zeroes_environment(signal, value, acceleration):

    s = list(signal)
    v = list(value)
    a = list(acceleration)

    matrix_s = []
    matrix_v = []
    matrix_a = []

    for index, item in enumerate(s, 1):
        mask1 = [index,item]
        matrix_s.append(mask1)

    for index, item in enumerate(v, 1):
        mask2 = [index,item]
        matrix_v.append(mask2)

    for index, item in enumerate(a, 1):
        mask3 = [index,item]
        matrix_a.append(mask3)

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
            # print(result_m)
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
            # print(result_v)
        else:
            pass

    A = '1'
    N = 0
    while (N < (len(matrix_a)-1)):
        z3 = random.randint(0, len(matrix_a) - 1)
        k3 = matrix_s[z3][1]
        if (k3 == '0'):
            N = len(matrix_a)
            mask_a = []
            mask_a.append(z3)
            mask_a.append(A)
            if (z3 == 0):
                matrix_s[z3].clear()
                matrix_s[z3].extend(mask_a)
            elif (z3 > 0):
                matrix_a[z3 - 1].clear()
                matrix_a[z3 - 1].extend(mask_a)
            L = 0
            result_ma = []
            while L < len(matrix_a):
                result_ma.append(matrix_a[L][1])
                L = L + 1
            result_a = ''.join(result_ma)
            # print(result_a)
        else:
            pass

    return result_m, result_v, result_a


####
#
# ones_environment function simulates noisy environment to make signal distorted
# converts random '1' to '0' and returns distorted signal
# can be used in pair with zeroes_environment function to increase the distortion level
# will be improved and modified for octal and hexadecimal systems
#

def ones_environment(signal, value, acceleration):

    s = list(signal)
    v = list(value)
    a = list(acceleration)

    matrix_s = []
    matrix_v = []
    matrix_a = []

    for index, item in enumerate(s, 1):
        mask1 = [index,item]
        matrix_s.append(mask1)

    for index, item in enumerate(v, 1):
        mask2 = [index,item]
        matrix_v.append(mask2)

    for index, item in enumerate(a, 1):
        mask3 = [index,item]
        matrix_a.append(mask3)

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
            # print(result_m)
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
            # print(result_v)
        else:
            pass

    A = '0'
    N = 0
    while (N < (len(matrix_a)-1)):
        z3 = random.randint(0, len(matrix_a) - 1)
        k3 = matrix_a[z3][1]
        if (k3 == '1'):
            N = len(matrix_a)
            mask_a = []
            mask_a.append(z3)
            mask_a.append(A)
            if (z3 == 0):
                matrix_s[z3].clear()
                matrix_s[z3].extend(mask_a)
            elif (z3 > 0):
                matrix_a[z3 - 1].clear()
                matrix_a[z3 - 1].extend(mask_a)
            L = 0
            result_ma = []
            while L < len(matrix_a):
                result_ma.append(matrix_a[L][1])
                L = L + 1
            result_a = ''.join(result_ma)
            # print(result_a)
        else:
            pass

    return result_m, result_v, result_a


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

def decoder(signal, value, acceleration):
    d_signal = signal[5:]
    d_value = int(value[8:], 2)
    # d_value = '228'
    d_acceleration = int(acceleration[8:], 2)
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

    if d_acceleration in range(1, 256):
        d_acceleration = '%s mps/second' % (d_acceleration)
    else:
        d_acceleration = ('Acceleration rate (%s m/s^2) is out of range' % (d_acceleration))

    # print(d_signal, d_value, d_acceleration)
    return d_signal, d_value, d_acceleration

 ####
 #
 # statistics function for last resort errors correction
 #

def statistics(trials):
    k = 0
    M_act = []
    M_ang = []
    M_acc = []
    while (k < trials):
        act, ang, acc = input_check()
        out_act, out_ang, out_acc = encoder(act, ang, acc)
        env_act, env_ang, env_acc = ones_environment(out_act, out_ang, out_acc)
        # in_act, in_ang, in_acc = decoder(env_act, env_ang, env_acc)
        M_act.append(env_act)
        M_ang.append(env_ang)
        M_acc.append(env_acc)
        k = k + 1
    Mact = Counter(M_act)
    Mang = Counter(M_ang)
    Macc = Counter(M_acc)

    print(Mact)
    print(Mang)
    print(Macc)
    #
    # Ract = ''.join(Mact)
    # print(Ract)

####
#
# main function - runs called functions together in defined sequence
#

def main():
    K = 10000
    statistics(K)
    # action, angle, acceleration = input_check()
    # out_act, out_ang, out_acc = encoder(action, angle, acceleration)
    # zeroes_environment(out_sig, out_val)
    # c_act, c_ang, c_acc = ones_environment(out_act, out_ang, out_acc)
    # decoder(c_act, c_ang, c_acc)


####
#
# call of main function
#

if __name__ == main():
    main()