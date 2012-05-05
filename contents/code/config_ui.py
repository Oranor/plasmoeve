# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_ui.ui'
#
# Created: Wed Oct  5 07:18:30 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(381, 243)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 54))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblUserID = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblUserID.setObjectName(_fromUtf8("lblUserID"))
        self.horizontalLayout.addWidget(self.lblUserID)
        self.txtUserID = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.txtUserID.setObjectName(_fromUtf8("txtUserID"))
        self.horizontalLayout.addWidget(self.txtUserID)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblUserID_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblUserID_2.setObjectName(_fromUtf8("lblUserID_2"))
        self.horizontalLayout_2.addWidget(self.lblUserID_2)
        self.txtAPIKey = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.txtAPIKey.setObjectName(_fromUtf8("txtAPIKey"))
        self.horizontalLayout_2.addWidget(self.txtAPIKey)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lstChars = QtGui.QListWidget(Dialog)
        self.lstChars.setGeometry(QtCore.QRect(10, 100, 361, 61))
        self.lstChars.setObjectName(_fromUtf8("lstChars"))
        self.cmdRetrieveChars = QtGui.QPushButton(Dialog)
        self.cmdRetrieveChars.setGeometry(QtCore.QRect(10, 70, 361, 23))
        self.cmdRetrieveChars.setObjectName(_fromUtf8("cmdRetrieveChars"))
        self.txtStatus = QtGui.QLabel(Dialog)
        self.txtStatus.setGeometry(QtCore.QRect(10, 160, 361, 16))
        self.txtStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.txtStatus.setObjectName(_fromUtf8("txtStatus"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 180, 351, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lblUserID.setText(QtGui.QApplication.translate("Dialog", "KeyID:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblUserID_2.setToolTip(QtGui.QApplication.translate("Dialog", "Verification Code", None, QtGui.QApplication.UnicodeUTF8))
        self.lblUserID_2.setText(QtGui.QApplication.translate("Dialog", "VCode:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdRetrieveChars.setText(QtGui.QApplication.translate("Dialog", "Retrieve Characters", None, QtGui.QApplication.UnicodeUTF8))
        self.txtStatus.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "<html><b>Donate some ISK to \"Auto Awesome\" to support this Plasmoid!", None, QtGui.QApplication.UnicodeUTF8))

