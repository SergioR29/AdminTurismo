# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manejarCiudades.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_manejarCiudades(object):
    def setupUi(self, manejarCiudades):
        if not manejarCiudades.objectName():
            manejarCiudades.setObjectName(u"manejarCiudades")
        manejarCiudades.setWindowModality(Qt.WindowModality.WindowModal)
        manejarCiudades.resize(849, 718)
        manejarCiudades.setMaximumSize(QSize(849, 718))
        manejarCiudades.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.frame = QFrame(manejarCiudades)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-2, 0, 851, 721))
        self.frame.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 19, 611, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayoutWidget = QWidget(self.frame)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 110, 271, 31))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.ciudadLabel = QLabel(self.formLayoutWidget)
        self.ciudadLabel.setObjectName(u"ciudadLabel")
        font1 = QFont()
        font1.setPointSize(10)
        self.ciudadLabel.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.ciudadLabel)

        self.ciudadComboBox = QComboBox(self.formLayoutWidget)
        self.ciudadComboBox.setObjectName(u"ciudadComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ciudadComboBox.sizePolicy().hasHeightForWidth())
        self.ciudadComboBox.setSizePolicy(sizePolicy)
        self.ciudadComboBox.setFont(font1)
        self.ciudadComboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom: 2px solid rgb(0, 170, 255);\n"
"border-left:none;\n"
"border-right:none;\n"
"border-top:none;\n"
"background-color: rgb(45, 45, 45);\n"
"padding-left:5px;\n"
"padding-right:5px;")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.ciudadComboBox)

        self.agregarCiudad = QPushButton(self.frame)
        self.agregarCiudad.setObjectName(u"agregarCiudad")
        self.agregarCiudad.setGeometry(QRect(710, 100, 101, 36))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.agregarCiudad.setFont(font2)
        self.agregarCiudad.setStyleSheet(u"background-color: rgb(170, 0, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:5px;")
        icon = QIcon()
        icon.addFile(u"../recursos/iconos/ic_agregar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.agregarCiudad.setIcon(icon)
        self.frame_ciudad = QFrame(self.frame)
        self.frame_ciudad.setObjectName(u"frame_ciudad")
        self.frame_ciudad.setGeometry(QRect(40, 160, 791, 531))
        self.frame_ciudad.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:5px;")
        self.frame_ciudad.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ciudad.setFrameShadow(QFrame.Shadow.Raised)
        self.editarCiudad = QPushButton(self.frame_ciudad)
        self.editarCiudad.setObjectName(u"editarCiudad")
        self.editarCiudad.setGeometry(QRect(580, 20, 97, 31))
        font3 = QFont()
        font3.setBold(True)
        self.editarCiudad.setFont(font3)
        self.editarCiudad.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 170, 255);\n"
"border-radius:5px;")
        icon1 = QIcon()
        icon1.addFile(u"../recursos/iconos/ic_editar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editarCiudad.setIcon(icon1)
        self.eliminarCiudad = QPushButton(self.frame_ciudad)
        self.eliminarCiudad.setObjectName(u"eliminarCiudad")
        self.eliminarCiudad.setGeometry(QRect(690, 20, 97, 31))
        self.eliminarCiudad.setFont(font3)
        self.eliminarCiudad.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 170, 255);\n"
"border-radius:5px;")
        icon2 = QIcon()
        icon2.addFile(u"../recursos/iconos/ic_eliminar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.eliminarCiudad.setIcon(icon2)
        self.img_ciudad = QLabel(self.frame_ciudad)
        self.img_ciudad.setObjectName(u"img_ciudad")
        self.img_ciudad.setGeometry(QRect(10, 20, 241, 181))
        self.img_ciudad.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border: 5px solid qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"border-radius:0px;")
        self.frame_3 = QFrame(self.frame_ciudad)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 300, 731, 211))
        self.frame_3.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(0, 170, 255);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.desc_ciudad = QPlainTextEdit(self.frame_3)
        self.desc_ciudad.setObjectName(u"desc_ciudad")
        self.desc_ciudad.setGeometry(QRect(10, 10, 711, 191))
        self.desc_ciudad.setFont(font1)
        self.desc_ciudad.setStyleSheet(u"background-color: rgb(54, 54, 54);color:white;border-radius:0px;")
        self.desc_ciudad.setReadOnly(True)
        self.nombreCiudad = QLineEdit(self.frame_ciudad)
        self.nombreCiudad.setObjectName(u"nombreCiudad")
        self.nombreCiudad.setGeometry(QRect(10, 210, 241, 31))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        self.nombreCiudad.setFont(font4)
        self.nombreCiudad.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"color: rgb(255, 255, 255);\n"
"border:0px")
        self.nombreCiudad.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nombreCiudad.setReadOnly(True)
        self.label_2 = QLabel(self.frame_ciudad)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 259, 711, 41))
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"color: white;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.guardarCambios = QPushButton(self.frame_ciudad)
        self.guardarCambios.setObjectName(u"guardarCambios")
        self.guardarCambios.setGeometry(QRect(640, 220, 141, 31))
        self.guardarCambios.setFont(font3)
        self.guardarCambios.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 170, 255);\n"
"border-radius:5px;")
        icon3 = QIcon()
        icon3.addFile(u"../recursos/iconos/ic_guardar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.guardarCambios.setIcon(icon3)
        self.seleccionarImagen = QPushButton(self.frame_ciudad)
        self.seleccionarImagen.setObjectName(u"seleccionarImagen")
        self.seleccionarImagen.setGeometry(QRect(270, 90, 171, 41))
        self.seleccionarImagen.setFont(font3)
        self.seleccionarImagen.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 170, 255);\n"
"border-radius:5px;")
        icon4 = QIcon()
        icon4.addFile(u"../recursos/iconos/ic_imagen.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.seleccionarImagen.setIcon(icon4)
        self.seleccionarImagen.setIconSize(QSize(28, 26))
        self.aviso = QLabel(self.frame)
        self.aviso.setObjectName(u"aviso")
        self.aviso.setGeometry(QRect(320, 120, 211, 21))
        self.aviso.setFont(font3)
        self.aviso.setStyleSheet(u"color: rgb(255, 255, 0);")

        self.retranslateUi(manejarCiudades)

        QMetaObject.connectSlotsByName(manejarCiudades)
    # setupUi

    def retranslateUi(self, manejarCiudades):
        manejarCiudades.setWindowTitle(QCoreApplication.translate("manejarCiudades", u"Ciudades", None))
        self.label.setText(QCoreApplication.translate("manejarCiudades", u"ADMINISTRACI\u00d3N DE CIUDADES", None))
        self.ciudadLabel.setText(QCoreApplication.translate("manejarCiudades", u"Ciudad", None))
        self.agregarCiudad.setText(QCoreApplication.translate("manejarCiudades", u"  A\u00f1adir", None))
        self.editarCiudad.setText(QCoreApplication.translate("manejarCiudades", u" Editar", None))
        self.eliminarCiudad.setText(QCoreApplication.translate("manejarCiudades", u" Eliminar", None))
        self.img_ciudad.setText("")
        self.desc_ciudad.setPlainText("")
        self.nombreCiudad.setText(QCoreApplication.translate("manejarCiudades", u"Nombre de la ciudad seleccionada", None))
        self.label_2.setText(QCoreApplication.translate("manejarCiudades", u"DESCRIPCI\u00d3N", None))
        self.guardarCambios.setText(QCoreApplication.translate("manejarCiudades", u"  Guardar cambios", None))
        self.seleccionarImagen.setText(QCoreApplication.translate("manejarCiudades", u" Seleccionar imagen...", None))
        self.aviso.setText(QCoreApplication.translate("manejarCiudades", u"SELECCIONE UNA CIUDAD PRIMERO", None))
    # retranslateUi

