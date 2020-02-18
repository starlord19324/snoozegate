from PySide import QtCore, QtGui
import sys
from ui import Ui_MainWindow
import random
from collections import Counter

####
# Copyright
# Anton Kharchenko
# National Aviation University
# 2019-2020 (c)

# Create application
app = QtGui.QApplication(sys.argv)

# Create form and init UI
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# Hook logic

signal_lib = ['001',
              '010',
              '100']

def input_check(action, angle, acceleration):
    # action = input('Enter the action here: ')
    # angle = int(input('Determine the angle from 0 to 90 here: '))
    # # acceleration = int(input('Determine the value from 0 to 90 here: '))
    # action = '001'
    # angle = int('154')
    # acceleration = int('51')
    if action in signal_lib and angle in range(0, 91) and acceleration in range(1, 256):
        # print(signal,value)
        ui.plainTextEdit_3.setPlainText(str(action) + '\n' + str(angle) + '\n' + str(acceleration) + '\n')
        return action, angle, acceleration
    else:
        ui.plainTextEdit_3.appendPlainText('Incorrect instruction')

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
    ui.plainTextEdit_3.appendPlainText(str(act) + '\n' + str(ang) +'\n' + str(acc) + '\n')
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
            ui.plainTextEdit_3.appendPlainText(str(result_m) + '\n')

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
            ui.plainTextEdit_3.appendPlainText(str(result_v) + '\n')
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
            ui.plainTextEdit_3.appendPlainText(str(result_a) + '\n')
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
            ui.plainTextEdit_3.appendPlainText(str(result_m) + '\n')
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
            ui.plainTextEdit_3.appendPlainText(str(result_v) + '\n')
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
            ui.plainTextEdit_3.appendPlainText(str(result_a) + '\n')
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

def decoder(signal, value, acceleration):
    d_signal = signal[5:]
    d_value = int(value[8:], 2)
    # d_value = '228'
    d_acceleration = int(acceleration[8:], 2)
    if d_signal in error_truth:
        d_signal = 'Некоректна команда: '
    elif d_signal in pitch_truth:
        d_signal = 'Тангаж: '
    elif d_signal in heel_truth:
        d_signal = 'Крен: '
    elif d_signal in yaw_truth:
        d_signal = 'Рискання: '

    if d_value in range(0, 181):
        d_value = '%s градусів' %(d_value)
    else:
        d_value = ('Кут (%s градусів) поза межами' %(d_value))

    if d_acceleration in range(1, 256):
        d_acceleration = '%s mps/second' % (d_acceleration)
    else:
        d_acceleration = ('Рівень прискорення (%s mps/second) поза межами' % (d_acceleration))

    # print(d_signal, d_value, d_acceleration)
    ui.plainTextEdit_3.appendPlainText(str(d_signal) + '\n' + str(d_value) + '\n' + str(d_acceleration) + '\n')
    return d_signal, d_value, d_acceleration

def statistics(action, angle, acceleration, trials):
    k = 0
    M_act = []
    M_ang = []
    M_acc = []
    while (k < trials):
        act, ang, acc = input_check(action, angle, acceleration)
        ui.plainTextEdit_3.appendPlainText(str(action) + '\n' + str(angle) + '\n' + str(acceleration) + '\n')
        out_act, out_ang, out_acc = encoder(act, ang, acc)
        ui.plainTextEdit_3.appendPlainText(str(out_act) + '\n' + str(out_ang) + '\n' + str(out_acc) + '\n')
        env_act, env_ang, env_acc = ones_environment(out_act, out_ang, out_acc)
        ui.plainTextEdit_3.appendPlainText(str(env_act) + '\n' + str(env_ang) + '\n' + str(env_acc) + '\n')
        in_act, in_ang, in_acc = decoder(env_act, env_ang, env_acc)
        ui.plainTextEdit_3.appendPlainText(str(in_act) + '\n' + str(in_ang) + '\n' + str(in_acc) + '\n')
        M_act.append(in_act)
        M_ang.append(in_ang)
        M_acc.append(in_acc)
        k = k + 1

    Mact = Counter(M_act)
    ui.plainTextEdit_3.appendPlainText(str(M_act) + '\n')
    Mang = Counter(M_ang)
    ui.plainTextEdit_3.appendPlainText(str(M_ang) + '\n')
    Macc = Counter(M_acc)
    ui.plainTextEdit_3.appendPlainText(str(M_acc) + '\n')

    act_set = set(M_act)
    ang_set = set(M_ang)
    acc_set = set(M_acc)

    most_common_act = None
    qty_most_common = 0
    for item1 in act_set:
        qty = M_act.count(item1)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common_act = item1
    # print(most_common_act)
    ui.plainTextEdit_3.appendPlainText(str(most_common_act) + '\n')

    most_common_ang = None
    qty_most_common = 0
    for item2 in ang_set:
        qty = M_ang.count(item2)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common_ang = item2
    # print(most_common_ang)
    ui.plainTextEdit_3.appendPlainText(str(most_common_ang) + '\n')

    most_common_acc = None
    qty_most_common = 0
    for item3 in acc_set:
        qty = M_acc.count(item3)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common_acc = item3
    # print(most_common_acc)
    ui.plainTextEdit_3.appendPlainText(str(most_common_acc) + '\n')

    Mact = str(Mact)
    Mang = str(Mang)
    Macc = str(Macc)

    # print(Mact)
    # print(Mang)
    # print(Macc)


    Ract = ''.join(most_common_act) + ''.join(most_common_ang) + ', ' + ''.join(most_common_acc)
    # print(Ract)

    return Ract, Mact, Mang, Macc

def main():
    text1 = ui.lineEdit_3.text()
    signal = str(text1)
    action, angle, acceleration = signal.rstrip().split(':')
    if action == 'Рискання' or action == 'рискання' or action == 'РИСКАННЯ':
        action = '100'
    elif action == 'Крен' or action == 'крен' or action == 'КРЕН':
        action = '010'
    elif action == 'Тангаж' or action == 'тангаж' or action == 'ТАНГАЖ':
        action = '001'
    angle = int(angle)
    acceleration = int(acceleration)
    text2 = ui.lineEdit_4.text()
    trials = int(text2)
    Q, K, V, M = statistics(action, angle, acceleration, trials)
    K = K[9:-2]
    V = V[9:-2]
    M = M[9:-2]
    ui.plainTextEdit.setPlainText(K + '\n' + V + '\n' + M)
    ui.plainTextEdit_2.setPlainText(Q)


ui.pushButton_4.clicked.connect( main )
# Run main loop
sys.exit(app.exec_())
