# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Inicio(object):
    def setupUi(self, Inicio):
        if not Inicio.objectName():
            Inicio.setObjectName(u"Inicio")
        Inicio.setWindowModality(Qt.WindowModality.WindowModal)
        Inicio.resize(808, 503)
        Inicio.setMaximumSize(QSize(808, 503))
        icon = QIcon()
        icon.addFile(u"../recursos/iconos/icono_admin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Inicio.setWindowIcon(icon)
        Inicio.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(Inicio)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -5, 811, 511))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 786, 61))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bienvenida = QLabel(self.verticalLayoutWidget)
        self.bienvenida.setObjectName(u"bienvenida")
        font = QFont()
        font.setFamilies([u"Script MT"])
        font.setPointSize(20)
        font.setBold(True)
        self.bienvenida.setFont(font)
        self.bienvenida.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(255, 255, 0);\n"
"padding-left: 5px;\n"
"padding-right: 5px")
        self.bienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.bienvenida)

        self.verticalLayoutWidget_3 = QWidget(self.frame)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(20, 450, 771, 41))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.instrucciones = QLabel(self.verticalLayoutWidget_3)
        self.instrucciones.setObjectName(u"instrucciones")
        self.instrucciones.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.instrucciones.setFont(font1)
        self.instrucciones.setStyleSheet(u"border: 2px solid rgb(0, 170, 255);\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);")
        self.instrucciones.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.instrucciones)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(19, 100, 771, 331))
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius: 15px")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.img_sitios = QLabel(self.frame_2)
        self.img_sitios.setObjectName(u"img_sitios")
        self.img_sitios.setGeometry(QRect(50, 28, 200, 221))
        self.img_sitios.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.img_sitios.setPixmap(QPixmap(u"../recursos/img/sitios.png"))
        self.manejarSitios = QPushButton(self.frame_2)
        self.manejarSitios.setObjectName(u"manejarSitios")
        self.manejarSitios.setGeometry(QRect(50, 270, 200, 41))
        self.manejarSitios.setFont(font1)
        self.manejarSitios.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 127);\n"
"border: 3px solid rgb(0, 0, 0);")
        self.img_ciudades = QLabel(self.frame_2)
        self.img_ciudades.setObjectName(u"img_ciudades")
        self.img_ciudades.setGeometry(QRect(505, 28, 221, 221))
        self.img_ciudades.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.img_ciudades.setPixmap(QPixmap(u"../recursos/img/ciudades.png"))
        self.manejarCiudades = QPushButton(self.frame_2)
        self.manejarCiudades.setObjectName(u"manejarCiudades")
        self.manejarCiudades.setGeometry(QRect(505, 270, 221, 41))
        self.manejarCiudades.setFont(font1)
        self.manejarCiudades.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 127);\n"
"border: 3px solid rgb(0, 0, 0);")
        Inicio.setCentralWidget(self.centralwidget)

        self.retranslateUi(Inicio)

        QMetaObject.connectSlotsByName(Inicio)
    # setupUi

    def retranslateUi(self, Inicio):
        Inicio.setWindowTitle(QCoreApplication.translate("Inicio", u"Inicio", None))
        self.bienvenida.setText(QCoreApplication.translate("Inicio", u"Bienvenido a la interfaz de administraci\u00f3n de sitios tur\u00edsticos y ciudades", None))
        self.instrucciones.setText(QCoreApplication.translate("Inicio", u"Para empezar, seleccione si desea manejar la informaci\u00f3n de los sitios tur\u00edsticos o de las ciudades", None))
        self.img_sitios.setText("")
        self.manejarSitios.setText(QCoreApplication.translate("Inicio", u"Manejar sitios", None))
        self.img_ciudades.setText("")
        self.manejarCiudades.setText(QCoreApplication.translate("Inicio", u"Manejar ciudades", None))
    # retranslateUi

