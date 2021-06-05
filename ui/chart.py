# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chart.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
mode = ['egreedy','三种策略奖励对比']
from src import MAB


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(383, 67)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 10, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(120, 10, 111, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(mode)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 81, 18))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.start_mab)

        # self.comboBox.setObjectName("模式")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "算法分析"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.label.setText(_translate("Dialog", "选择模式"))


    def start_mab(self):
        text = self.comboBox.currentText()
        MAB.select_mab_kind(text)