# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agregarSitios.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_agregarSitios(object):
    def setupUi(self, agregarSitios):
        if not agregarSitios.objectName():
            agregarSitios.setObjectName(u"agregarSitios")
        agregarSitios.setWindowModality(Qt.WindowModality.WindowModal)
        agregarSitios.resize(836, 689)
        agregarSitios.setMaximumSize(QSize(836, 689))
        icon = QIcon()
        icon.addFile(u"../recursos/img/sitios.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        agregarSitios.setWindowIcon(icon)
        agregarSitios.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);")
        self.label = QLabel(agregarSitios)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 811, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.seleccionarImagen = QPushButton(agregarSitios)
        self.seleccionarImagen.setObjectName(u"seleccionarImagen")
        self.seleccionarImagen.setGeometry(QRect(330, 270, 181, 41))
        font1 = QFont()
        font1.setBold(True)
        self.seleccionarImagen.setFont(font1)
        self.seleccionarImagen.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 170, 255);")
        icon1 = QIcon()
        icon1.addFile(u"../recursos/iconos/ic_imagen.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.seleccionarImagen.setIcon(icon1)
        self.seleccionarImagen.setIconSize(QSize(28, 28))
        self.img_sitio = QLabel(agregarSitios)
        self.img_sitio.setObjectName(u"img_sitio")
        self.img_sitio.setGeometry(QRect(300, 80, 241, 181))
        self.img_sitio.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border: 5px solid qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.desc_sitio = QPlainTextEdit(agregarSitios)
        self.desc_sitio.setObjectName(u"desc_sitio")
        self.desc_sitio.setGeometry(QRect(90, 490, 681, 121))
        font2 = QFont()
        font2.setPointSize(10)
        self.desc_sitio.setFont(font2)
        self.desc_sitio.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(53, 53, 53);\n"
"border:2px solid rgb(0, 85, 255);\n"
"border-radius: 5px")
        self.guardarSitio = QPushButton(agregarSitios)
        self.guardarSitio.setObjectName(u"guardarSitio")
        self.guardarSitio.setGeometry(QRect(500, 640, 101, 36))
        self.guardarSitio.setFont(font1)
        self.guardarSitio.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 170, 255);")
        icon2 = QIcon()
        icon2.addFile(u"../recursos/iconos/ic_guardar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.guardarSitio.setIcon(icon2)
        self.cerrar = QPushButton(agregarSitios)
        self.cerrar.setObjectName(u"cerrar")
        self.cerrar.setGeometry(QRect(260, 640, 101, 36))
        self.cerrar.setFont(font1)
        self.cerrar.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 170, 255);")
        icon3 = QIcon()
        icon3.addFile(u"../recursos/iconos/cerrar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cerrar.setIcon(icon3)
        self.cerrar.setIconSize(QSize(22, 22))
        self.label_2 = QLabel(agregarSitios)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 450, 681, 31))
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: white;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayoutWidget = QWidget(agregarSitios)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(210, 340, 391, 71))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(15)
        self.formLayout_2.setContentsMargins(0, 0, 0, 6)
        self.nombreLabel = QLabel(self.formLayoutWidget)
        self.nombreLabel.setObjectName(u"nombreLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nombreLabel)

        self.nombreLineEdit = QLineEdit(self.formLayoutWidget)
        self.nombreLineEdit.setObjectName(u"nombreLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nombreLineEdit.sizePolicy().hasHeightForWidth())
        self.nombreLineEdit.setSizePolicy(sizePolicy)
        self.nombreLineEdit.setFont(font2)
        self.nombreLineEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom: 2px solid rgb(0, 170, 255);\n"
"border-left:none;\n"
"border-right:none;\n"
"border-top:none;\n"
"background-color: rgb(45, 45, 45);\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.nombreLineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nombreLineEdit)

        self.ciudadLabel = QLabel(self.formLayoutWidget)
        self.ciudadLabel.setObjectName(u"ciudadLabel")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.ciudadLabel)

        self.ciudadComboBox = QComboBox(self.formLayoutWidget)
        self.ciudadComboBox.setObjectName(u"ciudadComboBox")
        sizePolicy.setHeightForWidth(self.ciudadComboBox.sizePolicy().hasHeightForWidth())
        self.ciudadComboBox.setSizePolicy(sizePolicy)
        self.ciudadComboBox.setFont(font2)
        self.ciudadComboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom: 2px solid rgb(0, 170, 255);\n"
"border-left:none;\n"
"border-right:none;\n"
"border-top:none;\n"
"background-color: rgb(45, 45, 45);\n"
"padding-left:5px;\n"
"padding-right:5px;")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.ciudadComboBox)


        self.retranslateUi(agregarSitios)
        self.cerrar.clicked.connect(agregarSitios.close)

        QMetaObject.connectSlotsByName(agregarSitios)
    # setupUi

    def retranslateUi(self, agregarSitios):
        agregarSitios.setWindowTitle(QCoreApplication.translate("agregarSitios", u"Sitios", None))
        self.label.setText(QCoreApplication.translate("agregarSitios", u"FORMULARIO DE SITIOS", None))
        self.seleccionarImagen.setText(QCoreApplication.translate("agregarSitios", u" Seleccionar imagen...", None))
        self.img_sitio.setText("")
        self.guardarSitio.setText(QCoreApplication.translate("agregarSitios", u"  Guardar", None))
        self.cerrar.setText(QCoreApplication.translate("agregarSitios", u" Cerrar", None))
        self.label_2.setText(QCoreApplication.translate("agregarSitios", u"DESCRIPCI\u00d3N", None))
        self.nombreLabel.setText(QCoreApplication.translate("agregarSitios", u"Nombre", None))
        self.ciudadLabel.setText(QCoreApplication.translate("agregarSitios", u"Ciudad", None))
    # retranslateUi

