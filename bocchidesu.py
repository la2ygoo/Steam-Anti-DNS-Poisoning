# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bocchidesu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import threading
import socket
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon


class Ui_Bocchidesu(object):
    def setupUi(self, Bocchidesu):
        Bocchidesu.setWindowIcon(QIcon("ico/main.ico"))
        Bocchidesu.setFixedSize(Bocchidesu.width(), Bocchidesu.height())
        Bocchidesu.setObjectName("Bocchidesu")
        Bocchidesu.setWindowModality(QtCore.Qt.WindowModal)
        Bocchidesu.setEnabled(True)
        Bocchidesu.setFixedSize(300, 280)
        Bocchidesu.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(Bocchidesu)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(120, 20, 71, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(220, 20, 71, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 50, 71, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(120, 50, 71, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(220, 50, 71, 16))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(120, 80, 71, 16))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_9.setGeometry(QtCore.QRect(220, 80, 71, 16))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_10.setGeometry(QtCore.QRect(20, 110, 71, 16))
        self.checkBox_10.setObjectName("checkBox_10")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 210, 101, 41))
        self.pushButton.setObjectName("pushButton")
        Bocchidesu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Bocchidesu)
        self.statusbar.setObjectName("statusbar")
        Bocchidesu.setStatusBar(self.statusbar)

        self.retranslateUi(Bocchidesu)
        QtCore.QMetaObject.connectSlotsByName(Bocchidesu)

    def retranslateUi(self, Bocchidesu):
        _translate = QtCore.QCoreApplication.translate
        Bocchidesu.setWindowTitle(_translate("Bocchidesu", "控制面板（bushi）"))
        self.checkBox.setText(_translate("Bocchidesu", "onedrive"))
        self.checkBox_2.setText(_translate("Bocchidesu", "exhentai"))
        self.checkBox_3.setText(_translate("Bocchidesu", "pixiv"))
        self.checkBox_4.setText(_translate("Bocchidesu", "discord"))
        self.checkBox_5.setText(_translate("Bocchidesu", "github"))
        self.checkBox_6.setText(_translate("Bocchidesu", "steam"))
        self.checkBox_7.setText(_translate("Bocchidesu", "duckduckgo"))
        self.checkBox_8.setText(_translate("Bocchidesu", "nyaa"))
        self.checkBox_9.setText(_translate("Bocchidesu", "v2ex"))
        self.checkBox_10.setText(_translate("Bocchidesu", "gravatar"))
        self.pushButton.setText(_translate("Bocchidesu", "开启/关闭"))
        self.pushButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        if check_port(80) or check_port(443):
            os.system("taskkill /f /im nginxtray.exe")
            os.system("taskkill /f /im nginx.exe")
            os.system("hosts.exe")
            QMessageBox.information(self, "提示", "80或443端口被占用，请检查一下，如果刚才运行了nginx，则已经关闭(会误杀其他nginx!)", QMessageBox.Yes)
        else:
            if self.checkBox.isChecked():
                with open('hosts/ms.txt', "r") as f1:  # 原txt存放路径
                    Readeddata = f1.readlines()  ##将打开文件的内容读到内存中，with 在执行完命令后，会关闭文件
                    f2 = open("C:/windows/system32/drivers/etc/hosts", "a+")  # 新txt存放路径
                    for hosts in Readeddata:
                        f2.write(hosts)  # 将原记事本的文件写入到另外一个记事本
                    f2.close()  # 执行完毕，关闭文件
            if self.checkBox_2.isChecked():
                with open('hosts/exhentai.txt', "r") as f1:  # 原txt存放路径
                    Readeddata = f1.readlines()  ##将打开文件的内容读到内存中，with 在执行完命令后，会关闭文件
                    f2 = open("C:/windows/system32/drivers/etc/hosts", "a+")  # 新txt存放路径
                    for hosts in Readeddata:
                        f2.write(hosts)  # 将原记事本的文件写入到另外一个记事本
                    f2.close()  # 执行完毕，关闭文件
            if self.checkBox_3.isChecked():
                with open('hosts/pixiv.txt', "r") as f1:  # 原txt存放路径
                    Readeddata = f1.readlines()  ##将打开文件的内容读到内存中，with 在执行完命令后，会关闭文件
                    f2 = open("C:/windows/system32/drivers/etc/hosts", "a+")  # 新txt存放路径
                    for hosts in Readeddata:
                        f2.write(hosts)  # 将原记事本的文件写入到另外一个记事本
                    f2.close()  # 执行完毕，关闭文件
            if self.checkBox_4.isChecked():
                with open('hosts/discord.txt', "r") as f1:  # 原txt存放路径
                    Readeddata = f1.readlines()  ##将打开文件的内容读到内存中，with 在执行完命令后，会关闭文件
                    f2 = open("C:/windows/system32/drivers/etc/hosts", "a+")  # 新txt存放路径
                    for hosts in Readeddata:
                        f2.write(hosts)  # 将原记事本的文件写入到另外一个记事本
                    f2.close()  # 执行完毕，关闭文件
            if self.checkBox_5.isChecked():
                with open('hosts/github.txt', "r") as f1:  # 原txt存放路径
                    Readeddata = f1.readlines()  ##将打开文件的内容读到内存中，with 在执行完命令后，会关闭文件
                    f2 = open("C:/windows/system32/drivers/etc/hosts", "a+")  # 新txt存放路径
                    for hosts in Readeddata:
                        f2.write(hosts)  # 将原记事本的文件写入到另外一个记事本
                    f2.close()  # 执行完毕，关闭文件
            if self.checkBox_6.isChecked():
                with open('hosts/steam.txt', "r") as f1:  # 原txt存放路径
                    Readeddata = f1.readlines()  ##将打开文件的内容读到内存中，with 在执行完命令后，会关闭文件
                    f2 = open("C:/windows/system32/drivers/etc/hosts", "a+")  # 新txt存放路径
                    for hosts in Readeddata:
                        f2.write(hosts)  # 将原记事本的文件写入到另外一个记事本
                    f2.close()  # 执行完毕，关闭文件
            if self.checkBox_7.isChecked():
                with open('hosts/duckduckgo.txt', "r") as f1:  # 原txt存放路径
                    Readeddata = f1.readlines()  ##将打开文件的内容读到内存中，with 在执行完命令后，会关闭文件
                    f2 = open("C:/windows/system32/drivers/etc/hosts", "a+")  # 新txt存放路径
                    for hosts in Readeddata:
                        f2.write(hosts)  # 将原记事本的文件写入到另外一个记事本
                    f2.close()  # 执行完毕，关闭文件
            if self.checkBox_8.isChecked():
                with open('hosts/nyaa.txt', "r") as f1:  # 原txt存放路径
                    Readeddata = f1.readlines()  ##将打开文件的内容读到内存中，with 在执行完命令后，会关闭文件
                    f2 = open("C:/windows/system32/drivers/etc/hosts", "a+")  # 新txt存放路径
                    for hosts in Readeddata:
                        f2.write(hosts)  # 将原记事本的文件写入到另外一个记事本
                    f2.close()  # 执行完毕，关闭文件
            if self.checkBox_9.isChecked():
                with open('hosts/v2ex.txt', "r") as f1:  # 原txt存放路径
                    Readeddata = f1.readlines()  ##将打开文件的内容读到内存中，with 在执行完命令后，会关闭文件
                    f2 = open("C:/windows/system32/drivers/etc/hosts", "a+")  # 新txt存放路径
                    for hosts in Readeddata:
                        f2.write(hosts)  # 将原记事本的文件写入到另外一个记事本
                    f2.close()  # 执行完毕，关闭文件
            if self.checkBox_10.isChecked():
                with open('hosts/gravarta.txt', "r") as f1:  # 原txt存放路径
                    Readeddata = f1.readlines()  ##将打开文件的内容读到内存中，with 在执行完命令后，会关闭文件
                    f2 = open("C:/windows/system32/drivers/etc/hosts", "a+")  # 新txt存放路径
                    for hosts in Readeddata:
                        f2.write(hosts)  # 将原记事本的文件写入到另外一个记事本
                    f2.close()  # 执行完毕，关闭文件
            t = threading.Thread(target=run_nginx)  # 创建线程
            t.start()  # 启动线程
            QMessageBox.information(None, "提示", "开启成功", QMessageBox.Ok)


def run_nginx():
    os.popen("nginxtray.exe")  # 启动nginx


def check_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', port))
        s.close()
        return 0
    except Exception as e:
        return 1
