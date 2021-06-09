# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1030, 810)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.content_view = QtWidgets.QListWidget(self.splitter)
        self.content_view.setObjectName("content_view")
        self.Vehicle_view = QtWidgets.QListWidget(self.splitter)
        self.Vehicle_view.setObjectName("Vehicle_view")
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.TimeSelect = QtWidgets.QComboBox(Dialog)
        self.TimeSelect.setObjectName("TimeSelect")
        self.horizontalLayout.addWidget(self.TimeSelect)
        self.simulation = QtWidgets.QPushButton(Dialog)
        self.simulation.setObjectName("simulation")
        self.horizontalLayout.addWidget(self.simulation)

        self.timer = QtCore.QTimer(Dialog)
        self.timer.start()


        self.label1 = QtWidgets.QLabel(Dialog)
        self.horizontalLayout.addWidget(self.label1)


        spacerItem = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.content_analys = QtWidgets.QPushButton(Dialog)
        # self.content_analys.setObjectName("")
        self.horizontalLayout.addWidget(self.content_analys)

        # spacerItem1 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout.addItem(spacerItem1)

        self.movies = QtWidgets.QPushButton(Dialog)
        self.horizontalLayout.addWidget(self.movies)

        self.latency = QtWidgets.QPushButton(Dialog)
        self.latency.setObjectName("latency")
        self.horizontalLayout.addWidget(self.latency)

        self.chart = QtWidgets.QPushButton(Dialog)
        self.horizontalLayout.addWidget(self.chart)

        # spacerItem2 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout.addItem(spacerItem2)



        self.verticalLayout.addLayout(self.horizontalLayout)
        self.chartview = QChartView()
        self.chartview.setObjectName("ChartView")
        self.chartview.setStyleSheet("background-color:lightblue")
        # self.chartview.chart().setStyleSheet("background-color:red")
        self.verticalLayout.addWidget(self.chartview)
        # self.chartview.setStyleSheet('QChartview{background-color:#000000}')

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.simulation.setStyleSheet("QPushButton{color:black}"
                                     "QPushButton:hover{color:blue}"
                                     "QPushButton{background-color:lightblue}"
                                     "QPushButton{border:10px}"
                                     "QPushButton{border-radius:10px}"
                                     "QPushButton{padding:5px 10px}")
        self.series = QLineSeries()
        self.x_Aix = QValueAxis()
        self.y_Aix = QValueAxis()

        self.latency.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:15px;}QPushButton:hover{background:red;}QPushButton{padding:5px 10px}''')
        self.content_analys.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:15px;}QPushButton:hover{background:yellow;}QPushButton{padding:5px 10px}''')
        self.movies.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:15px;}QPushButton:hover{background:green;}QPushButton{padding:5px 10px}''')
        self.chart.setStyleSheet(
            '''QPushButton{background:#87CEFA;border-radius:15px;}QPushButton:hover{background:lightblue;}QPushButton{padding:5px 10px}''')
        # self.setWindowOpacity(0.9)  # 设置窗口透明度
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "车载内容缓存策略仿真系统"))
        self.label.setText(_translate("Dialog", "设置时间"))
        self.simulation.setText(_translate("Dialog", "开始仿真"))
        self.latency.setText(_translate("Dialog", "延迟分析"))
        self.content_analys.setText(_translate("Dialog","内容分析"))
        self.movies.setText(_translate("Dialog","查看文件"))
        self.chart.setText(_translate("Dialog","算法分析"))