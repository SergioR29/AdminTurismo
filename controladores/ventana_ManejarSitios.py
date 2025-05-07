import sys, os, sqlite3, shutil
from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QBuffer, QIODevice, Signal
from vistas.manejarSitios_ui import Ui_manejarSitios
from modelos.InitialisationError import InitialisationError
from controladores.ventana_AgregarSitio import AgregarSitios

class ManejarSitios(QWidget, Ui_manejarSitios):
    closing = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Variables auxiliares
        self.ventana = 0
        self.eliminarSt = False
        self.imagen = None
        self.edicion = False
        self.edicion2 = False
        self.sitioEditado = False
        self.IDSitio = 0
        self.IDCiudad = 0
        self.vecesRegistrar = 0
        self.imagenSel = 0

        # Configuraciones menores
        self.nombreSitio.setStyleSheet("color:white;background-color: rgb(30, 30, 30);border:none;")
        self.ciudadComboBox.setCurrentIndex(-1)
        self.sitioComboBox.setCurrentIndex(-1)
        self.seleccionarImagen.hide()
        self.guardarCambios.hide()
        self.ciudadLabel_2.hide()
        self.ciudadComboBox_Editar.hide()
        self.aviso_sitio.hide()

        # Añadir los iconos
        self.agregarSitio.setIcon(QIcon(os.getcwd() + "/recursos/iconos/ic_agregar.png"))
        self.editarSitio.setIcon(QIcon(os.getcwd() + "/recursos/iconos/ic_editar.png"))
        self.eliminarSitio.setIcon(QIcon(os.getcwd() + "/recursos/iconos/ic_eliminar.png"))
        self.guardarCambios.setIcon(QIcon(os.getcwd() + "/recursos/iconos/ic_guardar.png"))
        self.seleccionarImagen.setIcon(QIcon(os.getcwd() + "/recursos/iconos/ic_imagen.png"))
        self.setWindowIcon(QIcon(os.getcwd() + "/recursos/iconos/ic_Sitios.png"))

        # Copiar la BD a la carpeta del usuario (para que no sea de sólo lectura)
        rutaBD = os.getcwd() + "/modelos/datos.db"
        userDir = Path.home()

        new_dirBD = os.path.join(userDir, "AdminTurismo")
        new_rutaBD = os.path.join(new_dirBD, "datos.db")
        os.makedirs(new_dirBD, exist_ok=True)

        if not os.path.exists(new_rutaBD):
            shutil.copy(rutaBD, new_rutaBD)

        # Conexión a la BD
        self.conexion = False
        try:
            self.conexion = sqlite3.connect(new_rutaBD)
        except sqlite3.Error as e:
            print(e.sqlite_errorcode)
            print(e.sqlite_errorname)

        # Configuraciones importantes
        self.frame_sitio.hide()
        self.ciudades = self.cargarCiudades()

        # Acciones
        self.ciudadComboBox.currentTextChanged.connect(self.cargarSitiosCiudad)
        self.sitioComboBox.currentTextChanged.connect(self.ocultarMensaje)
        self.agregarSitio.clicked.connect(self.registrarSitio)
        self.editarSitio.clicked.connect(self.editar)
        self.eliminarSitio.clicked.connect(self.eliminar)

        # Acciones (Editar sitio)
        self.seleccionarImagen.clicked.connect(self.imagenSitio)
        self.guardarCambios.clicked.connect(self.guardar)
        self.ciudadComboBox_Editar.currentTextChanged.connect(self.controlarImagen)

    def controlarImagen(self):
        # Función que controla la integridad del uso de imágenes entre sitios
        if self.imagenSel == 0:
            self.imagen = None

    def guardar(self):
        # Función para guardar los cambios en los datos de un sitio al editarlos
        self.nombreSitio.setStyleSheet("color:white;background-color: rgb(30, 30, 30);border:none;")
        self.nombreSitio.setReadOnly(True)
        self.seleccionarImagen.hide()
        self.guardarCambios.hide()
        self.desc_Sitio.setReadOnly(True)
        self.ciudadLabel_2.hide()
        self.ciudadComboBox_Editar.hide()

        self.edicion = False
        if self.IDSitio > 0 and len(self.nombreSitio.text()) > 0 and self.ciudadComboBox_Editar.currentIndex() != -1:
            idC = self.conexion.execute("SELECT c.ID FROM Ciudades c WHERE c.Nombre = ?", (self.ciudadComboBox_Editar.currentText(),)).fetchone()
            idCiudad = int(idC[0])
            try:
                self.conexion.execute("UPDATE Sitios SET Nombre = ?, Descripcion = ?, Imagen = ?, Ciudad = ? WHERE ID = ?", (self.nombreSitio.text(), self.desc_Sitio.toPlainText(), self.imagen, idCiudad, self.IDSitio))
                self.conexion.commit()

                QMessageBox.information(self, "Resultado", "Datos del sitio actualizados")
                self.frame_sitio.show()

                if self.imagenSel == 0:
                    self.imagen = None

                self.imagenSel = 0

                sitioEditado = self.nombreSitio.text()
                self.cargarSitiosCiudad()

                indice = self.sitioComboBox.findText(sitioEditado)
                self.sitioComboBox.setCurrentIndex(indice)
                self.ocultarMensaje()

                # Poner la nueva versión de la BD
                verBD = self.conexion.execute("SELECT MAX(Ver) FROM VersionTurismo").fetchone()
                nuevaVerBD = 0

                if verBD[0] != None:
                    nuevaVerBD = verBD[0] + 1

                    self.conexion.execute("UPDATE VersionTurismo SET Ver = ? WHERE Ver = ?", (nuevaVerBD, verBD[0],))
                    self.conexion.commit()
                else:
                    nuevaVerBD = 1

                    self.conexion.execute("INSERT INTO VersionTurismo VALUES (?)", (nuevaVerBD,))
                    self.conexion.commit()

            except sqlite3.Error as e:
                print(e.sqlite_errorcode)
                print(e.sqlite_errorname)
                self.conexion.rollback()

                QMessageBox.warning(self, "Resultado", "No se pudieron actualizar los datos del sitio")
        else:
            if self.ciudadComboBox_Editar.currentIndex() == -1:
                QMessageBox.warning(self, "Aviso", "Ciudad del sitio no seleccionada")

            elif len(self.nombreSitio.text()) <= 0:
                QMessageBox.warning(self, "Aviso", "Nombre del sitio vacío")
            
            self.nombreSitio.setText(self.sitioComboBox.currentText())
            self.edicion = True
            self.editar()
            self.ocultarMensaje()

    def imagenSitio(self):
        # Función que permite al usuario seleccionar una imagen para añadir un sitio
        ruta_imagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen sitio", "", "Archivos de Imagen (*.png *.jpg *.jpeg *.bmp)")
        if ruta_imagen:
            pixmap = QPixmap(ruta_imagen)
            self.img_Sitio.setPixmap(pixmap)
            self.img_Sitio.setScaledContents(True)

            # Convertimos la imagen para que sea insertable en la BD
            buffer = QBuffer()
            abrir = buffer.open(QIODevice.WriteOnly)
            if abrir:
                guardado = pixmap.save(buffer, "PNG")
                if not guardado:
                    buffer.close()
                else:
                    byte_array = buffer.data()
                    buffer.close()
                    self.imagen = bytes(byte_array)

                    self.imagenSel += 1

    def editar(self):
        # Función que permite al usuario editar los datos del sitio de una ciudad
        if not self.edicion:
            self.edicion = True

            self.nombreSitio.setStyleSheet("background-color: rgb(53, 53, 53);\ncolor: rgb(255, 255, 255);\nborder:none")
            self.nombreSitio.setReadOnly(False)
            self.seleccionarImagen.show()
            self.guardarCambios.show()
            self.desc_Sitio.setReadOnly(False)
            self.ciudadLabel_2.show()
            self.ciudadComboBox_Editar.show()

            indice = self.ciudadComboBox_Editar.findText(self.ciudadComboBox.currentText())
            self.ciudadComboBox_Editar.setCurrentIndex(indice)

            try:
                idS = self.conexion.execute("SELECT s.ID FROM Sitios s WHERE s.Nombre = ?", (self.nombreSitio.text(),)).fetchone()
                if idS:
                    self.IDSitio = int(idS[0])

            except sqlite3.Error as e:
                print(e.sqlite_errorcode)
                print(e.sqlite_errorname)
        else:
            self.edicion = False

            self.nombreSitio.setStyleSheet("background-color: rgb(30, 30, 30);\ncolor: rgb(255, 255, 255);\nborder:none")
            self.nombreSitio.setReadOnly(True)
            self.seleccionarImagen.hide()
            self.guardarCambios.hide()
            self.desc_Sitio.setReadOnly(True)
            self.ciudadLabel_2.hide()
            self.ciudadComboBox_Editar.hide()

            self.ocultarMensaje()
            self.edicion2 = True

    def eliminar(self):
        # Función que permite al usuario eliminar el sitio de una ciudad
        try:
            idS = self.conexion.execute("SELECT ID FROM Sitios WHERE Nombre = ?", (self.sitioComboBox.currentText(),)).fetchone()
            if idS != None:
                self.conexion.execute("DELETE FROM Sitios WHERE ID = ?", (int(idS[0]),))
                self.conexion.commit()
                
                self.frame_sitio.hide()
                self.sitioComboBox.clear()
                self.nombreSitio.setText("")
                self.desc_Sitio.setPlainText("")
                self.img_Sitio.setPixmap(QPixmap())
                self.cargarSitiosCiudad()

                self.eliminarSt = True
                QMessageBox.information(self, "Resultado", "Sitio seleccionado de la ciudad " + self.ciudadComboBox.currentText() + " eliminado")

                # Poner la nueva versión de la BD
                verBD = self.conexion.execute("SELECT MAX(Ver) FROM VersionTurismo").fetchone()
                nuevaVerBD = 0

                if verBD[0] != None:
                    nuevaVerBD = verBD[0] + 1

                    self.conexion.execute("UPDATE VersionTurismo SET Ver = ? WHERE Ver = ?", (nuevaVerBD, verBD[0],))
                    self.conexion.commit()
                else:
                    nuevaVerBD = 1

                    self.conexion.execute("INSERT INTO VersionTurismo VALUES (?)", (nuevaVerBD,))
                    self.conexion.commit()
            else:
                QMessageBox.warning(self, "Resultado", "Error al eliminar el sitio seleccionado")

        except sqlite3.Error as e:
            print(e.sqlite_errorcode)
            print(e.sqlite_errorname)
            self.conexion.rollback()

            QMessageBox.warning(self, "Resultado", "Error al eliminar el sitio seleccionado")

    def cargarCiudades(self):
        # Función que carga las ciudades registradas en la BD
        if self.conexion:
            ciudades = self.conexion.execute("SELECT Nombre FROM Ciudades ORDER BY Nombre")
            for ciudad in ciudades.fetchall():
                self.ciudadComboBox.addItem(ciudad[0])
                self.ciudadComboBox_Editar.addItem(ciudad[0])

            if self.ciudadComboBox.count() <= 0:
                self.frame_sitio.hide()

                QMessageBox.warning(self, "Aviso", "No hay datos de ciudades guardadas")
                raise InitialisationError("No hay datos de ciudades guardadas en la base de datos.")
            
            elif self.ciudadComboBox.count() > 0:
               self.ciudadComboBox.setCurrentIndex(-1)
               self.sitioComboBox.setCurrentIndex(-1)
               self.ciudadComboBox_Editar.setCurrentIndex(-1)

               self.aviso_ciudadNoSeleccionada.show()
               return self.ciudadComboBox.count()
        else:
            QMessageBox.warning(self, "Aviso", "Error de conexión a la BD")
            raise InitialisationError("Error de conexión a la BD.")

    def cargarSitiosCiudad(self):
        # Función que carga los sitios de la ciudad elegida
        if self.ciudades > 0:
            self.sitioComboBox.clear()
            self.img_Sitio.setPixmap(QPixmap())
            self.desc_Sitio.setPlainText("")
            self.frame_sitio.hide()
            self.aviso_ciudadNoSeleccionada.hide()
            self.aviso_sitio.show()

            cID = self.conexion.execute("SELECT c.ID FROM Ciudades c WHERE c.Nombre = ?", (self.ciudadComboBox.currentText(),))
            ciudadID = cID.fetchone()

            if ciudadID:
                self.IDCiudad = int(ciudadID[0])

                sitios = self.conexion.execute("SELECT s.Nombre FROM Sitios s WHERE s.Ciudad = ? ORDER BY s.Nombre", (int(ciudadID[0]),)).fetchall()
                for sitio in sitios:
                    self.sitioComboBox.addItem(sitio[0])
                    self.sitioComboBox.setCurrentIndex(-1)
                    self.frame_sitio.hide()

                if self.sitioComboBox.count() <= 0:
                    self.aviso_ciudadNoSeleccionada.hide()

                    self.aviso_sitio.setText(self.ciudadComboBox.currentText() + " NO TIENE SITIOS ASOCIADOS")
                    self.aviso_sitio.show()
                    self.frame_sitio.hide()
                else:
                    self.aviso_ciudadNoSeleccionada.hide()
                    if self.edicion2:
                        self.frame_sitio.show()
                        self.edicion2 = False

                    if self.sitioComboBox.currentIndex() == -1:
                        self.aviso_sitio.setText("SELECCIONE UN SITIO")
                        self.aviso_sitio.show()
            else:
                self.aviso_sitio.setText(self.ciudadComboBox.currentText() + " NO TIENE SITIOS ASOCIADOS")
                self.aviso_sitio.show()

    def ocultarMensaje(self):
        # Función que oculta el mensaje de ciudad no seleccionada cuando el usuario selecciona un sitio
        self.aviso_ciudadNoSeleccionada.hide()
        self.img_Sitio.setPixmap(QPixmap())
        self.desc_Sitio.setPlainText("")

        if self.sitioComboBox.currentIndex() != -1:
            self.aviso_sitio.hide()
            self.nombreSitio.setText(self.sitioComboBox.currentText())

            sitio = self.conexion.execute("SELECT s.Descripcion, s.Imagen FROM Sitios s WHERE s.Nombre = ?", (self.sitioComboBox.currentText(),)).fetchone()
            if sitio:
                desc = sitio[0]
                imagen = sitio[1]

                # Sacar imagen de la BD
                pixmap = QPixmap()
                pixmap.loadFromData(imagen, "PNG")

                if not pixmap.isNull():
                    self.img_Sitio.setPixmap(pixmap)
                    self.img_Sitio.setScaledContents(True)
                    self.imagen = imagen

                self.desc_Sitio.setPlainText(str(desc))
                self.frame_sitio.show()

    def registrarSitio(self):
        # Función que permite a los usuarios acceder al formulario de sitios
        idC = self.conexion.execute("SELECT c.ID FROM Ciudades c WHERE c.Nombre = ?", (self.ciudadComboBox.currentText(),)).fetchone()
        ID = 0
        if idC != None:
            ID = int(idC[0])
            self.close()

            self.ventana = AgregarSitios(ID)
            self.ventana.closing.connect(self.cerrarVentana)
            self.ventana.guardarSitio.clicked.connect(self.cargarSitiosCiudad)
            self.ventana.guardarSitio.clicked.connect(self.mostrarIndicativo)
            self.ventana.show()

        elif self.ciudadComboBox.currentIndex() == -1:
            QMessageBox.warning(self, "Aviso", "No se ha seleccionado ninguna ciudad")

    def mostrarIndicativo(self):
        # Función que muestra un mensaje indicando al usuario que hay nuevos sitios disponibles
        self.vecesRegistrar +=1
        
        if self.vecesRegistrar == 1:
            self.aviso_sitio.setText("¡NUEVO SITIO REGISTRADO!" + ((" (en " + self.ventana.ciudadComboBox.currentText() + ")") if self.ciudadComboBox.currentText() != self.ventana.ciudadComboBox.currentText() else ""))
        elif self.vecesRegistrar > 1:
            self.aviso_sitio.setText("¡NUEVOS SITIOS REGISTRADOS!" + ((" (en diferentes ciudades)") if self.ciudadComboBox.currentText() != self.ventana.ciudadComboBox.currentText() else ""))

    def closeEvent(self, event):
        # Función que el usuario al cerrar la ventana se le vuelve a la ventana de inicio
        self.closing.emit()
        super().closeEvent(event)

    def cerrarVentana(self):
        self.vecesRegistrar = 0
        self.imagenSel = 0

        self.ventana.close()
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    manejarSitios = ManejarSitios()
    manejarSitios.show()
    sys.exit(app.exec())