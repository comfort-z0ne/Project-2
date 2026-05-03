# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLCDNumber, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)
from pathlib import Path

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(948, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.channelWidget = QStackedWidget(self.centralwidget)
        self.channelWidget.setObjectName(u"channelWidget")
        self.channelWidget.setGeometry(QRect(280, 0, 671, 481))
        self.off = QWidget()
        self.off.setObjectName(u"off")
        self.offLabel = QLabel(self.off)
        self.offLabel.setObjectName(u"offLabel")
        self.offLabel.setGeometry(QRect(230, 220, 201, 16))
        self.offLabel.setAlignment(Qt.AlignCenter)
        self.channelWidget.addWidget(self.off)
        self.channel1 = QWidget()
        self.channel1.setObjectName(u"channel1")
        self.picture1 = QLabel(self.channel1)
        self.picture1.setObjectName(u"picture1")
        self.picture1.setGeometry(QRect(-430, -220, 1201, 771))
        self.channelWidget.addWidget(self.channel1)
        self.channel2 = QWidget()
        self.channel2.setObjectName(u"channel2")
        self.picture2 = QLabel(self.channel2)
        self.picture2.setObjectName(u"picture2")
        self.picture2.setGeometry(QRect(-520, -350, 1231, 921))
        self.channelWidget.addWidget(self.channel2)
        self.channel3 = QWidget()
        self.channel3.setObjectName(u"channel3")
        self.picture3 = QLabel(self.channel3)
        self.picture3.setObjectName(u"picture3")
        self.picture3.setGeometry(QRect(-490, 0, 1341, 681))
        self.channelWidget.addWidget(self.channel3)
        self.channel4 = QWidget()
        self.channel4.setObjectName(u"channel4")
        self.picture4 = QLabel(self.channel4)
        self.picture4.setObjectName(u"picture4")
        self.picture4.setGeometry(QRect(-400, -180, 1061, 691))
        self.channelWidget.addWidget(self.channel4)
        self.channel5 = QWidget()
        self.channel5.setObjectName(u"channel5")
        self.picture5 = QLabel(self.channel5)
        self.picture5.setObjectName(u"picture5")
        self.picture5.setGeometry(QRect(-510, -30, 1181, 891))
        self.channelWidget.addWidget(self.channel5)
        self.inputLine = QLineEdit(self.centralwidget)
        self.inputLine.setObjectName(u"inputLine")
        self.inputLine.setGeometry(QRect(80, 30, 121, 20))
        self.inputLine.setInputMethodHints(Qt.ImhNone)
        self.inputLine.setReadOnly(True)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 60, 239, 141))
        self.keypadLayout = QGridLayout(self.gridLayoutWidget)
        self.keypadLayout.setObjectName(u"keypadLayout")
        self.keypadLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_six = QPushButton(self.gridLayoutWidget)
        self.pushButton_six.setObjectName(u"pushButton_six")

        self.keypadLayout.addWidget(self.pushButton_six, 1, 2, 1, 1)

        self.pushButton_five = QPushButton(self.gridLayoutWidget)
        self.pushButton_five.setObjectName(u"pushButton_five")

        self.keypadLayout.addWidget(self.pushButton_five, 1, 1, 1, 1)

        self.pushButton_two = QPushButton(self.gridLayoutWidget)
        self.pushButton_two.setObjectName(u"pushButton_two")

        self.keypadLayout.addWidget(self.pushButton_two, 2, 1, 1, 1)

        self.pushButton_four = QPushButton(self.gridLayoutWidget)
        self.pushButton_four.setObjectName(u"pushButton_four")

        self.keypadLayout.addWidget(self.pushButton_four, 1, 0, 1, 1)

        self.pushButton_nine = QPushButton(self.gridLayoutWidget)
        self.pushButton_nine.setObjectName(u"pushButton_nine")

        self.keypadLayout.addWidget(self.pushButton_nine, 0, 2, 1, 1)

        self.pushButton_seven = QPushButton(self.gridLayoutWidget)
        self.pushButton_seven.setObjectName(u"pushButton_seven")

        self.keypadLayout.addWidget(self.pushButton_seven, 0, 0, 1, 1)

        self.pushButton_eight = QPushButton(self.gridLayoutWidget)
        self.pushButton_eight.setObjectName(u"pushButton_eight")

        self.keypadLayout.addWidget(self.pushButton_eight, 0, 1, 1, 1)

        self.pushButton_one = QPushButton(self.gridLayoutWidget)
        self.pushButton_one.setObjectName(u"pushButton_one")

        self.keypadLayout.addWidget(self.pushButton_one, 2, 0, 1, 1)

        self.pushButton_three = QPushButton(self.gridLayoutWidget)
        self.pushButton_three.setObjectName(u"pushButton_three")

        self.keypadLayout.addWidget(self.pushButton_three, 2, 2, 1, 1)

        self.pushButton_zero = QPushButton(self.gridLayoutWidget)
        self.pushButton_zero.setObjectName(u"pushButton_zero")

        self.keypadLayout.addWidget(self.pushButton_zero, 3, 0, 1, 1)

        self.pushButton_confirm = QPushButton(self.gridLayoutWidget)
        self.pushButton_confirm.setObjectName(u"pushButton_confirm")

        self.keypadLayout.addWidget(self.pushButton_confirm, 3, 2, 1, 1)

        self.pushButton_backspace = QPushButton(self.gridLayoutWidget)
        self.pushButton_backspace.setObjectName(u"pushButton_backspace")

        self.keypadLayout.addWidget(self.pushButton_backspace, 3, 1, 1, 1)

        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(210, 20, 64, 23))
        self.pushButton_power = QPushButton(self.centralwidget)
        self.pushButton_power.setObjectName(u"pushButton_power")
        self.pushButton_power.setGeometry(QRect(10, 10, 61, 41))
        self.label_error = QLabel(self.centralwidget)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setGeometry(QRect(70, 10, 141, 20))
        self.label_error.setAlignment(Qt.AlignCenter)
        self.pushButton_volUp = QPushButton(self.centralwidget)
        self.pushButton_volUp.setObjectName(u"pushButton_volUp")
        self.pushButton_volUp.setGeometry(QRect(10, 210, 61, 41))
        self.pushButton_volDown = QPushButton(self.centralwidget)
        self.pushButton_volDown.setObjectName(u"pushButton_volDown")
        self.pushButton_volDown.setGeometry(QRect(10, 280, 61, 41))
        self.label_volume = QLabel(self.centralwidget)
        self.label_volume.setObjectName(u"label_volume")
        self.label_volume.setGeometry(QRect(20, 260, 46, 13))
        self.label_volume.setAlignment(Qt.AlignCenter)
        self.pushButton_chUp = QPushButton(self.centralwidget)
        self.pushButton_chUp.setObjectName(u"pushButton_chUp")
        self.pushButton_chUp.setGeometry(QRect(210, 210, 61, 41))
        self.pushButton_chDown = QPushButton(self.centralwidget)
        self.pushButton_chDown.setObjectName(u"pushButton_chDown")
        self.pushButton_chDown.setGeometry(QRect(210, 280, 61, 41))
        self.label_channel = QLabel(self.centralwidget)
        self.label_channel.setObjectName(u"label_channel")
        self.label_channel.setGeometry(QRect(220, 260, 46, 13))
        self.label_channel.setAlignment(Qt.AlignCenter)
        self.pushButton_mute = QPushButton(self.centralwidget)
        self.pushButton_mute.setObjectName(u"pushButton_mute")
        self.pushButton_mute.setGeometry(QRect(110, 210, 61, 41))
        self.volumeBar = QProgressBar(self.centralwidget)
        self.volumeBar.setObjectName(u"volumeBar")
        self.volumeBar.setGeometry(QRect(10, 450, 261, 23))
        self.volumeBar.setMaximum(10)
        self.volumeBar.setValue(1)
        self.volumeBar.setTextVisible(True)
        self.label_muted = QLabel(self.centralwidget)
        self.label_muted.setObjectName(u"label_muted")
        self.label_muted.setGeometry(QRect(110, 430, 46, 13))
        self.label_muted.setAlignment(Qt.AlignCenter)
        self.pushButton_guide = QPushButton(self.centralwidget)
        self.pushButton_guide.setObjectName(u"pushButton_guide")
        self.pushButton_guide.setGeometry(QRect(110, 280, 61, 41))
        self.guideWidget = QStackedWidget(self.centralwidget)
        self.guideWidget.setObjectName(u"guideWidget")
        self.guideWidget.setGeometry(QRect(9, 339, 261, 91))
        self.hidden = QWidget()
        self.hidden.setObjectName(u"hidden")
        self.guideWidget.addWidget(self.hidden)
        self.visible = QWidget()
        self.visible.setObjectName(u"visible")
        self.listWidget = QListWidget(self.visible)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 0, 261, 91))
        self.guideWidget.addWidget(self.visible)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.channelWidget.setCurrentIndex(0)
        self.guideWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Example TV Controller", None))
        self.offLabel.setText(QCoreApplication.translate("MainWindow", u"The TV is now off.", None))
        self.picture1.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p><img src=\"{Path(__file__).parent.joinpath('assets/brick.webp')}\"/></p></body></html>", None))
        self.picture2.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p><img src=\"{Path(__file__).parent.joinpath('assets/bob.webp')}\"/></p></body></html>", None))
        self.picture3.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p><img src=\"{Path(__file__).parent.joinpath('assets/bad.png')}\"/></p></body></html>", None))
        self.picture4.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p><img src=\"{Path(__file__).parent.joinpath('assets/gaba.webp')}\"/></p></body></html>", None))
        self.picture5.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p><img src=\"{Path(__file__).parent.joinpath('assets/lady.jpg')}\"/></p></body></html>", None))
        self.inputLine.setInputMask("")
        self.inputLine.setText("")
        self.pushButton_six.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_five.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_two.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_four.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_nine.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_seven.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_eight.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_one.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_three.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_zero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_confirm.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.pushButton_backspace.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_power.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_error.setText("")
        self.pushButton_volUp.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_volDown.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_volume.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.pushButton_chUp.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_chDown.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_channel.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.pushButton_mute.setText(QCoreApplication.translate("MainWindow", u"Mute", None))
        self.volumeBar.setFormat(QCoreApplication.translate("MainWindow", u"%v", None))
        self.label_muted.setText("")
        self.pushButton_guide.setText(QCoreApplication.translate("MainWindow", u"Guide", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"1 - Brick and Mortar", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"2 - Spunchburb Pant", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"3 - Walta Whit Methe", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"4 - 20 Years in the Can", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"5 - Your Mom Loved this Show", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

