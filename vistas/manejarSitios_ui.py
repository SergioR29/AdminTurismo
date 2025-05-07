# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manejarSitios.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_manejarSitios(object):
    def setupUi(self, manejarSitios):
        if not manejarSitios.objectName():
            manejarSitios.setObjectName(u"manejarSitios")
        manejarSitios.setWindowModality(Qt.WindowModality.WindowModal)
        manejarSitios.resize(849, 718)
        manejarSitios.setMaximumSize(QSize(849, 718))
        icon = QIcon()
        icon.addFile(u"../../V_Escritorio/recursos/iconos/ic_Sitios.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        manejarSitios.setWindowIcon(icon)
        manejarSitios.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.frame = QFrame(manejarSitios)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 861, 721))
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
        self.formLayoutWidget.setGeometry(QRect(30, 90, 271, 71))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(13)
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

        self.sitioLabel = QLabel(self.formLayoutWidget)
        self.sitioLabel.setObjectName(u"sitioLabel")
        self.sitioLabel.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.sitioLabel)

        self.sitioComboBox = QComboBox(self.formLayoutWidget)
        self.sitioComboBox.setObjectName(u"sitioComboBox")
        sizePolicy.setHeightForWidth(self.sitioComboBox.sizePolicy().hasHeightForWidth())
        self.sitioComboBox.setSizePolicy(sizePolicy)
        self.sitioComboBox.setFont(font1)
        self.sitioComboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom: 2px solid rgb(170, 0, 255);\n"
"border-left:none;\n"
"border-right:none;\n"
"border-top:none;\n"
"background-color: rgb(45, 45, 45);\n"
"padding-left:5px;\n"
"padding-right:5px;")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sitioComboBox)

        self.agregarSitio = QPushButton(self.frame)
        self.agregarSitio.setObjectName(u"agregarSitio")
        self.agregarSitio.setGeometry(QRect(710, 100, 101, 36))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.agregarSitio.setFont(font2)
        self.agregarSitio.setStyleSheet(u"background-color: rgb(170, 0, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:5px;")
        icon1 = QIcon()
        icon1.addFile(u"../recursos/iconos/ic_agregar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.agregarSitio.setIcon(icon1)
        self.frame_sitio = QFrame(self.frame)
        self.frame_sitio.setObjectName(u"frame_sitio")
        self.frame_sitio.setGeometry(QRect(30, 170, 791, 531))
        self.frame_sitio.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:5px;")
        self.frame_sitio.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_sitio.setFrameShadow(QFrame.Shadow.Raised)
        self.editarSitio = QPushButton(self.frame_sitio)
        self.editarSitio.setObjectName(u"editarSitio")
        self.editarSitio.setGeometry(QRect(580, 20, 97, 31))
        font3 = QFont()
        font3.setBold(True)
        self.editarSitio.setFont(font3)
        self.editarSitio.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 170, 255);")
        icon2 = QIcon()
        icon2.addFile(u"../recursos/iconos/ic_editar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editarSitio.setIcon(icon2)
        self.eliminarSitio = QPushButton(self.frame_sitio)
        self.eliminarSitio.setObjectName(u"eliminarSitio")
        self.eliminarSitio.setGeometry(QRect(690, 20, 97, 31))
        self.eliminarSitio.setFont(font3)
        self.eliminarSitio.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 170, 255);")
        icon3 = QIcon()
        icon3.addFile(u"../recursos/iconos/ic_eliminar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.eliminarSitio.setIcon(icon3)
        self.img_Sitio = QLabel(self.frame_sitio)
        self.img_Sitio.setObjectName(u"img_Sitio")
        self.img_Sitio.setGeometry(QRect(10, 20, 241, 181))
        self.img_Sitio.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border: 5px solid qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"border-radius:0px;")
        self.frame_3 = QFrame(self.frame_sitio)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 300, 731, 211))
        self.frame_3.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(0, 170, 255);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.desc_Sitio = QPlainTextEdit(self.frame_3)
        self.desc_Sitio.setObjectName(u"desc_Sitio")
        self.desc_Sitio.setGeometry(QRect(10, 10, 711, 191))
        font4 = QFont()
        font4.setPointSize(9)
        self.desc_Sitio.setFont(font4)
        self.desc_Sitio.setStyleSheet(u"background-color: rgb(54, 54, 54);color:white;border-radius:0px;")
        self.desc_Sitio.setReadOnly(True)
        self.nombreSitio = QLineEdit(self.frame_sitio)
        self.nombreSitio.setObjectName(u"nombreSitio")
        self.nombreSitio.setGeometry(QRect(10, 210, 241, 31))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        self.nombreSitio.setFont(font5)
        self.nombreSitio.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"color: rgb(255, 255, 255);\n"
"border:0px")
        self.nombreSitio.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nombreSitio.setReadOnly(True)
        self.label_2 = QLabel(self.frame_sitio)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 259, 711, 41))
        font6 = QFont()
        font6.setPointSize(15)
        font6.setBold(True)
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"color: white;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.guardarCambios = QPushButton(self.frame_sitio)
        self.guardarCambios.setObjectName(u"guardarCambios")
        self.guardarCambios.setGeometry(QRect(640, 220, 141, 31))
        self.guardarCambios.setFont(font3)
        self.guardarCambios.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 170, 255);")
        icon4 = QIcon()
        icon4.addFile(u"../recursos/iconos/ic_guardar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.guardarCambios.setIcon(icon4)
        self.seleccionarImagen = QPushButton(self.frame_sitio)
        self.seleccionarImagen.setObjectName(u"seleccionarImagen")
        self.seleccionarImagen.setGeometry(QRect(270, 30, 171, 41))
        self.seleccionarImagen.setFont(font3)
        self.seleccionarImagen.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 170, 255);")
        icon5 = QIcon()
        icon5.addFile(u"../recursos/iconos/ic_imagen.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.seleccionarImagen.setIcon(icon5)
        self.seleccionarImagen.setIconSize(QSize(24, 24))
        self.formLayoutWidget_2 = QWidget(self.frame_sitio)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(270, 140, 221, 56))
        self.verticalLayout_Editar = QVBoxLayout(self.formLayoutWidget_2)
        self.verticalLayout_Editar.setObjectName(u"verticalLayout_Editar")
        self.verticalLayout_Editar.setContentsMargins(0, 0, 0, 0)
        self.ciudadLabel_2 = QLabel(self.formLayoutWidget_2)
        self.ciudadLabel_2.setObjectName(u"ciudadLabel_2")
        font7 = QFont()
        font7.setPointSize(11)
        self.ciudadLabel_2.setFont(font7)

        self.verticalLayout_Editar.addWidget(self.ciudadLabel_2)

        self.ciudadComboBox_Editar = QComboBox(self.formLayoutWidget_2)
        self.ciudadComboBox_Editar.setObjectName(u"ciudadComboBox_Editar")
        sizePolicy.setHeightForWidth(self.ciudadComboBox_Editar.sizePolicy().hasHeightForWidth())
        self.ciudadComboBox_Editar.setSizePolicy(sizePolicy)
        self.ciudadComboBox_Editar.setMinimumSize(QSize(0, 28))
        self.ciudadComboBox_Editar.setFont(font1)
        self.ciudadComboBox_Editar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom: 2px solid rgb(0, 170, 255);\n"
"border-left:none;\n"
"border-right:none;\n"
"border-top:none;\n"
"background-color: rgb(45, 45, 45);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"border-radius:0px;")

        self.verticalLayout_Editar.addWidget(self.ciudadComboBox_Editar)

        self.aviso_ciudadNoSeleccionada = QLabel(self.frame)
        self.aviso_ciudadNoSeleccionada.setObjectName(u"aviso_ciudadNoSeleccionada")
        self.aviso_ciudadNoSeleccionada.setGeometry(QRect(320, 90, 211, 31))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.aviso_ciudadNoSeleccionada.sizePolicy().hasHeightForWidth())
        self.aviso_ciudadNoSeleccionada.setSizePolicy(sizePolicy1)
        self.aviso_ciudadNoSeleccionada.setFont(font3)
        self.aviso_ciudadNoSeleccionada.setStyleSheet(u"color: rgb(255, 255, 0);")
        self.aviso_sitio = QLabel(self.frame)
        self.aviso_sitio.setObjectName(u"aviso_sitio")
        self.aviso_sitio.setGeometry(QRect(320, 130, 381, 31))
        sizePolicy1.setHeightForWidth(self.aviso_sitio.sizePolicy().hasHeightForWidth())
        self.aviso_sitio.setSizePolicy(sizePolicy1)
        self.aviso_sitio.setFont(font3)
        self.aviso_sitio.setStyleSheet(u"color: rgb(255, 255, 0);")

        self.retranslateUi(manejarSitios)

        QMetaObject.connectSlotsByName(manejarSitios)
    # setupUi

    def retranslateUi(self, manejarSitios):
        manejarSitios.setWindowTitle(QCoreApplication.translate("manejarSitios", u"Sitios", None))
        self.label.setText(QCoreApplication.translate("manejarSitios", u"ADMINISTRACI\u00d3N DE SITIOS", None))
        self.ciudadLabel.setText(QCoreApplication.translate("manejarSitios", u"Ciudad", None))
        self.sitioLabel.setText(QCoreApplication.translate("manejarSitios", u"Sitio", None))
        self.agregarSitio.setText(QCoreApplication.translate("manejarSitios", u"  A\u00f1adir", None))
        self.editarSitio.setText(QCoreApplication.translate("manejarSitios", u" Editar", None))
        self.eliminarSitio.setText(QCoreApplication.translate("manejarSitios", u" Eliminar", None))
        self.img_Sitio.setText("")
        self.desc_Sitio.setPlainText("")
        self.nombreSitio.setText(QCoreApplication.translate("manejarSitios", u"Nombre del sitio seleccionado", None))
        self.label_2.setText(QCoreApplication.translate("manejarSitios", u"DESCRIPCI\u00d3N", None))
        self.guardarCambios.setText(QCoreApplication.translate("manejarSitios", u"  Guardar cambios", None))
        self.seleccionarImagen.setText(QCoreApplication.translate("manejarSitios", u" Seleccionar imagen...", None))
        self.ciudadLabel_2.setText(QCoreApplication.translate("manejarSitios", u"Ciudad", None))
        self.aviso_ciudadNoSeleccionada.setText(QCoreApplication.translate("manejarSitios", u"SELECCIONE UNA CIUDAD", None))
        self.aviso_sitio.setText(QCoreApplication.translate("manejarSitios", u"SELECCIONE UN SITIO", None))
    # retranslateUi

