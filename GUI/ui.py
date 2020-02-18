# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Noivern\PycharmProjects\snoozegate\GUI\snoozegate.ui'
#
# Created: Tue Feb 18 03:15:19 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 542)
        MainWindow.setStyleSheet("QPushButton {\n"
"    background-color: rgb(219, 223, 255);\n"
"    color: rgb(110, 111, 128);\n"
"    width: 250px;\n"
"    height: 120px;\n"
"    font: Yu Gothic UI Semilight;\n"
"    font-size: 20px;\n"
"    font-height: bold;\n"
"    text-align: center;\n"
"    border: none;        \n"
"    border-color: (67, 74, 133);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(143, 154,255);\n"
"    border-color: (67, 74, 133);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(67, 74, 133);\n"
"    color: rgb(219, 223, 255);\n"
"    border-color: (219, 223, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"    width: 250px;\n"
"    height: 120px;\n"
"    font: Yu Gothic UI Semilight;\n"
"    font-size: 20px;\n"
"    font-height: bold;\n"
"    text-align: center;\n"
"    border: none;        \n"
"    border-color: (67, 74, 133);\n"
"}\n"
"\n"
"QCheckBox {\n"
"    background-color: rgb(219, 223, 255);\n"
"    color: rgb(110, 111, 128);\n"
"    width: 75px;\n"
"    height: 50px;\n"
"    font: Yu Gothic UI Semilight;\n"
"    font-size: 20px;\n"
"    font-height: bold;\n"
"    text-align: center;\n"
"    border: none;        \n"
"}\n"
"\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: rgb(143, 154,255);\n"
"    border-color: (67, 74, 133);\n"
"}\n"
"\n"
"QCheckBox:pressed {\n"
"    background-color: rgb(67, 74, 133);\n"
"    color: rgb(219, 223, 255);\n"
"    border-color: (219, 223, 255);\n"
"}")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 20, 91, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 20, 321, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 120, 191, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 300, 101, 21))
        self.label.setObjectName("label")
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 390, 111, 21))
        self.label_6.setObjectName("label_6")
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 420, 431, 101))
        self.plainTextEdit.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(40, 330, 431, 51))
        self.plainTextEdit_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 60, 281, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 60, 141, 31))
        self.label_5.setObjectName("label_5")
        self.plainTextEdit_3 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(40, 210, 431, 81))
        self.plainTextEdit_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 180, 101, 21))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Команда:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "СТАРТ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Результат:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Статистика:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Розмір пакету:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Прогрес:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

