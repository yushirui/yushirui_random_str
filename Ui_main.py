# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\yu_python\yu_工具开发_2018\yu_suijiStr2\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 225)
        MainWindow.setMinimumSize(QtCore.QSize(400, 225))
        MainWindow.setMaximumSize(QtCore.QSize(400, 225))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 402, 221))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cb_shuzi = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.cb_shuzi.setMinimumSize(QtCore.QSize(0, 0))
        self.cb_shuzi.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cb_shuzi.setObjectName("cb_shuzi")
        self.gridLayout_2.addWidget(self.cb_shuzi, 1, 5, 1, 1)
        self.cb_zhongwen = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.cb_zhongwen.setMinimumSize(QtCore.QSize(0, 0))
        self.cb_zhongwen.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cb_zhongwen.setChecked(True)
        self.cb_zhongwen.setObjectName("cb_zhongwen")
        self.gridLayout_2.addWidget(self.cb_zhongwen, 1, 1, 1, 1)
        self.cb_yingwen = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.cb_yingwen.setMinimumSize(QtCore.QSize(0, 0))
        self.cb_yingwen.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cb_yingwen.setObjectName("cb_yingwen")
        self.gridLayout_2.addWidget(self.cb_yingwen, 1, 3, 1, 1)
        self.cb_yingbiao = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.cb_yingbiao.setMinimumSize(QtCore.QSize(0, 0))
        self.cb_yingbiao.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cb_yingbiao.setObjectName("cb_yingbiao")
        self.gridLayout_2.addWidget(self.cb_yingbiao, 1, 4, 1, 1)
        self.cb_zhongbiao = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.cb_zhongbiao.setMinimumSize(QtCore.QSize(0, 0))
        self.cb_zhongbiao.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cb_zhongbiao.setObjectName("cb_zhongbiao")
        self.gridLayout_2.addWidget(self.cb_zhongbiao, 1, 2, 1, 1)
        self.pb_wanneng = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pb_wanneng.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_wanneng.setMaximumSize(QtCore.QSize(51, 16777215))
        self.pb_wanneng.setObjectName("pb_wanneng")
        self.gridLayout_2.addWidget(self.pb_wanneng, 2, 0, 1, 1)
        self.pb_tongyong = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pb_tongyong.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_tongyong.setMaximumSize(QtCore.QSize(51, 16777215))
        self.pb_tongyong.setObjectName("pb_tongyong")
        self.gridLayout_2.addWidget(self.pb_tongyong, 2, 1, 1, 1)
        self.pb_tesu = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pb_tesu.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_tesu.setMaximumSize(QtCore.QSize(51, 16777215))
        self.pb_tesu.setObjectName("pb_tesu")
        self.gridLayout_2.addWidget(self.pb_tesu, 2, 2, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.spinBox.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.spinBox.setMaximum(10000)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 1, 0, 1, 1)
        self.cb_zhiding = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.cb_zhiding.setMinimumSize(QtCore.QSize(0, 0))
        self.cb_zhiding.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cb_zhiding.setChecked(True)
        self.cb_zhiding.setObjectName("cb_zhiding")
        self.gridLayout_2.addWidget(self.cb_zhiding, 1, 6, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 7)
        self.pb_10 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pb_10.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_10.setMaximumSize(QtCore.QSize(51, 16777215))
        self.pb_10.setObjectName("pb_10")
        self.gridLayout_2.addWidget(self.pb_10, 2, 3, 1, 1)
        self.pb_20 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pb_20.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_20.setMaximumSize(QtCore.QSize(51, 16777215))
        self.pb_20.setObjectName("pb_20")
        self.gridLayout_2.addWidget(self.pb_20, 2, 4, 1, 1)
        self.pb_50 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pb_50.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_50.setMaximumSize(QtCore.QSize(51, 16777215))
        self.pb_50.setObjectName("pb_50")
        self.gridLayout_2.addWidget(self.pb_50, 2, 5, 1, 1)
        self.pb_100 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pb_100.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_100.setMaximumSize(QtCore.QSize(51, 16777215))
        self.pb_100.setObjectName("pb_100")
        self.gridLayout_2.addWidget(self.pb_100, 2, 6, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cb_shuzi.setText(_translate("MainWindow", "数字"))
        self.cb_zhongwen.setText(_translate("MainWindow", "中文"))
        self.cb_yingwen.setText(_translate("MainWindow", "英文"))
        self.cb_yingbiao.setText(_translate("MainWindow", "英标"))
        self.cb_zhongbiao.setText(_translate("MainWindow", "中标"))
        self.pb_wanneng.setText(_translate("MainWindow", "万能"))
        self.pb_tongyong.setText(_translate("MainWindow", "通用"))
        self.pb_tesu.setText(_translate("MainWindow", "特殊"))
        self.cb_zhiding.setText(_translate("MainWindow", "置顶"))
        self.pb_10.setText(_translate("MainWindow", "10"))
        self.pb_20.setText(_translate("MainWindow", "20"))
        self.pb_50.setText(_translate("MainWindow", "50"))
        self.pb_100.setText(_translate("MainWindow", "100"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

