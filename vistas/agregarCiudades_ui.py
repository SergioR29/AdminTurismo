# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agregarCiudades.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_agregarCiudades(object):
    def setupUi(self, agregarCiudades):
        if not agregarCiudades.objectName():
            agregarCiudades.setObjectName(u"agregarCiudades")
        agregarCiudades.setWindowModality(Qt.WindowModality.WindowModal)
        agregarCiudades.resize(836, 648)
        agregarCiudades.setMaximumSize(QSize(836, 648))
        agregarCiudades.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);")
        self.label = QLabel(agregarCiudades)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 811, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.seleccionarImagen = QPushButton(agregarCiudades)
        self.seleccionarImagen.setObjectName(u"seleccionarImagen")
        self.seleccionarImagen.setGeometry(QRect(330, 270, 181, 41))
        font1 = QFont()
        font1.setBold(True)
        self.seleccionarImagen.setFont(font1)
        self.seleccionarImagen.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 170, 255);")
        icon = QIcon()
        icon.addFile(u"../recursos/iconos/ic_imagen.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.seleccionarImagen.setIcon(icon)
        self.seleccionarImagen.setIconSize(QSize(28, 28))
        self.img_ciudad = QLabel(agregarCiudades)
        self.img_ciudad.setObjectName(u"img_ciudad")
        self.img_ciudad.setGeometry(QRect(300, 80, 241, 181))
        self.img_ciudad.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border: 5px solid qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.formLayoutWidget = QWidget(agregarCiudades)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(220, 350, 391, 27))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.nombreLabel = QLabel(self.formLayoutWidget)
        self.nombreLabel.setObjectName(u"nombreLabel")
        font2 = QFont()
        font2.setPointSize(10)
        self.nombreLabel.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nombreLabel)

        self.nombreLineEdit = QLineEdit(self.formLayoutWidget)
        self.nombreLineEdit.setObjectName(u"nombreLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nombreLineEdit.sizePolicy().hasHeightForWidth())
        self.nombreLineEdit.setSizePolicy(sizePolicy)
        self.nombreLineEdit.setFont(font2)
        self.nombreLineEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(44, 44, 44);\n"
"border-bottom: 2px solid rgb(0, 170, 255);\n"
"border-left:none;\n"
"border-right:none;\n"
"border-top:none;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.nombreLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nombreLineEdit)

        self.desc_ciudad = QPlainTextEdit(agregarCiudades)
        self.desc_ciudad.setObjectName(u"desc_ciudad")
        self.desc_ciudad.setGeometry(QRect(80, 450, 681, 121))
        font3 = QFont()
        font3.setPointSize(9)
        self.desc_ciudad.setFont(font3)
        self.desc_ciudad.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(53, 53, 53);\n"
"border:2px solid rgb(0, 85, 255);\n"
"border-radius: 5px")
        self.guardarCiudad = QPushButton(agregarCiudades)
        self.guardarCiudad.setObjectName(u"guardarCiudad")
        self.guardarCiudad.setGeometry(QRect(460, 600, 91, 31))
        self.guardarCiudad.setFont(font1)
        self.guardarCiudad.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 170, 255);")
        icon1 = QIcon()
        icon1.addFile(u"../recursos/iconos/ic_guardar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.guardarCiudad.setIcon(icon1)
        self.cerrar = QPushButton(agregarCiudades)
        self.cerrar.setObjectName(u"cerrar")
        self.cerrar.setGeometry(QRect(300, 600, 91, 31))
        self.cerrar.setFont(font1)
        self.cerrar.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 170, 255);")
        icon2 = QIcon()
        icon2.addFile(u"../recursos/iconos/cerrar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cerrar.setIcon(icon2)
        self.cerrar.setIconSize(QSize(20, 20))
        self.label_2 = QLabel(agregarCiudades)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 410, 681, 31))
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: white;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(agregarCiudades)
        self.cerrar.clicked.connect(agregarCiudades.close)

        QMetaObject.connectSlotsByName(agregarCiudades)
    # setupUi

    def retranslateUi(self, agregarCiudades):
        agregarCiudades.setWindowTitle(QCoreApplication.translate("agregarCiudades", u"A\u00f1adir Ciudades", None))
        self.label.setText(QCoreApplication.translate("agregarCiudades", u"FORMULARIO DE CIUDADES", None))
        self.seleccionarImagen.setText(QCoreApplication.translate("agregarCiudades", u" Seleccionar imagen...", None))
        self.img_ciudad.setText("")
        self.nombreLabel.setText(QCoreApplication.translate("agregarCiudades", u"Nombre", None))
        self.guardarCiudad.setText(QCoreApplication.translate("agregarCiudades", u"  Guardar", None))
        self.cerrar.setText(QCoreApplication.translate("agregarCiudades", u" Cerrar", None))
        self.label_2.setText(QCoreApplication.translate("agregarCiudades", u"DESCRIPCI\u00d3N", None))
    # retranslateUi

