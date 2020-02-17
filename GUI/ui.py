# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Noivern\PycharmProjects\snoozegate\GUI\snoozegate.ui'
#
# Created: Mon Feb 17 17:35:19 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 833)
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
"QRadioButton {\n"
"    background-color: rgb(219, 223, 255);\n"
"    color: rgb(110, 111, 128);\n"
"    width: 70px;\n"
"    height: 60px;\n"
"    font: Yu Gothic UI Semilight;\n"
"    font-size: 20px;\n"
"    font-height: bold;\n"
"    text-align: center;\n"
"    border: none;        \n"
"}\n"
"\n"
"\n"
"QRadioButton:hover {\n"
"    background-color: rgb(143, 154,255);\n"
"    border-color: (67, 74, 133);\n"
"}\n"
"\n"
"QRadiolButton:pressed {\n"
"    background-color: rgb(67, 74, 133);\n"
"    color: rgb(219, 223, 255);\n"
"    border-color: (219, 223, 255);\n"
"}")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 131, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 100, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 140, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 180, 221, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 180, 113, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 430, 121, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 230, 201, 31))
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 411, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_2 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(250, 230, 121, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_4 = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_5 = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_6 = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.horizontalLayout_2.addWidget(self.radioButton_6)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 540, 101, 21))
        self.label.setObjectName("label")
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 630, 111, 21))
        self.label_6.setObjectName("label_6")
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(80, 490, 351, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 570, 421, 51))
        self.label_7.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 660, 421, 161))
        self.label_8.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 270, 411, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_7 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout.addWidget(self.radioButton_7)
        self.radioButton_8 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout.addWidget(self.radioButton_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Кут (0-90):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Прискорення:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Розмір пакету сигналів:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "СТАРТ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Рівень зашумленості:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("MainWindow", " Крен", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("MainWindow", " Рискання", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("MainWindow", " Тангаж", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_4.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_5.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_6.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Результат:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Статистика:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_7.setText(QtGui.QApplication.translate("MainWindow", " \"Нерозумне\" кодування", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_8.setText(QtGui.QApplication.translate("MainWindow", " \"Розумне кодування\"", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

