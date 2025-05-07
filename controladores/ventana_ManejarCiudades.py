import sys, os, pathlib, sqlite3, shutil
from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QBuffer, QIODevice, Signal
from vistas.manejarCiudades_ui import Ui_manejarCiudades
from modelos.InitialisationError import InitialisationError
from controladores.ventana_AgregarCiudad import AgregarCiudades

class ManejarCiudades(QWidget, Ui_manejarCiudades):
    closing = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Variables auxiliares
        self.ventana = 0
        self.imagen = None
        self.eliminarCty = False
        self.editarCty = False
        self.cityEditada = False
        self.IDCiudad = 0
        self.vecesRegistrar = 0

        # Configuraciones menores
        self.nombreCiudad.setStyleSheet("color:white;background-color: rgb(30, 30, 30);border:none;")
        self.ciudadComboBox.setCurrentIndex(-1)
        self.seleccionarImagen.hide()
        self.guardarCambios.hide()
        self.aviso.hide()

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

        # Añadir los iconos
        self.agregarCiudad.setIcon(QIcon(os.getcwd() + "/recursos/iconos/ic_agregar.png"))
        self.editarCiudad.setIcon(QIcon(os.getcwd() + "/recursos/iconos/ic_editar.png"))
        self.eliminarCiudad.setIcon(QIcon(os.getcwd() + "/recursos/iconos/ic_eliminar.png"))
        self.guardarCambios.setIcon(QIcon(os.getcwd() + "/recursos/iconos/ic_guardar.png"))
        self.seleccionarImagen.setIcon(QIcon(os.getcwd() + "/recursos/iconos/ic_imagen.png"))
        self.setWindowIcon(QIcon(os.getcwd() + "/recursos/iconos/ic_Sitios.png"))
    
        # Configuraciones importantes
        self.frame_ciudad.hide()
        self.cargarCiudades()

        # Acciones
        self.agregarCiudad.clicked.connect(self.registrarCiudad)
        self.ciudadComboBox.currentTextChanged.connect(self.cargarInfoCiudadSeleccionada)
        self.editarCiudad.clicked.connect(self.editar)
        self.eliminarCiudad.clicked.connect(self.eliminar)

        # Acciones (Editar ciudad)
        self.seleccionarImagen.clicked.connect(self.imagenCiudad)
        self.guardarCambios.clicked.connect(self.guardar)

    def guardar(self):
        # Función que permite al usuario guardar los datos nuevos de una ciudad y eliminar los antiguos
        self.nombreCiudad.setStyleSheet("color:white;background-color: rgb(30, 30, 30);border:none;")
        self.seleccionarImagen.hide()
        self.guardarCambios.hide()
        self.nombreCiudad.setReadOnly(True)
        self.desc_ciudad.setReadOnly(True)

        self.editarCty = False
        if self.IDCiudad > 0 and len(self.nombreCiudad.text()) > 0:
            try:
                self.conexion.execute("UPDATE Ciudades SET Nombre = ?, Imagen = ?, Descripcion = ? WHERE ID = ?", (self.nombreCiudad.text(), self.imagen, self.desc_ciudad.toPlainText(), self.IDCiudad))
                self.conexion.commit()

                QMessageBox.information(self, "Resultado", "Datos de la ciudad actualizados")
                self.frame_ciudad.show()

                ciudadEditada = self.nombreCiudad.text()
                self.cargarCiudades()

                indice = self.ciudadComboBox.findText(ciudadEditada)
                self.cityEditada = True

                self.ciudadComboBox.setCurrentIndex(indice)
                self.cargarInfoCiudadSeleccionada()

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

                QMessageBox.warning(self, "Resultado", "No se pudieron actualizar los datos de la ciudad")
        else:
            QMessageBox.warning(self, "Aviso", "Nombre de la ciudad vacío")
            self.nombreCiudad.setText(self.ciudadComboBox.currentText())

            self.editarCty = True
            self.editar()
            self.cargarInfoCiudadSeleccionada()

    def imagenCiudad(self):
        # Función que permite al usuario seleccionar una imagen para añadir un sitio
        ruta_imagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen ciudad", "", "Archivos de Imagen (*.png *.jpg *.jpeg *.bmp)")
        if ruta_imagen:
            pixmap = QPixmap(ruta_imagen)
            self.img_ciudad.setPixmap(pixmap)
            self.img_ciudad.setScaledContents(True)

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

    def editar(self):
        # Función que permite al usuario editar los datos de una ciudad
        if not self.editarCty:
            if self.ciudadComboBox.currentIndex() == -1:
                QMessageBox.warning(None, "Aviso", "No se ha seleccionado ninguna ciudad")
            else:
                self.nombreCiudad.setStyleSheet("color:white;background-color: rgb(53, 53, 53);border:none;")
                self.seleccionarImagen.show()
                self.guardarCambios.show()
                self.nombreCiudad.setReadOnly(False)
                self.desc_ciudad.setReadOnly(False)

                self.editarCty = True
                try:
                    idC = self.conexion.execute("SELECT c.ID FROM Ciudades c WHERE c.Nombre = ?", (self.nombreCiudad.text(),)).fetchone()
                    if idC:
                        self.IDCiudad = int(idC[0])

                except sqlite3.Error as e:
                    print(e.sqlite_errorcode)
                    print(e.sqlite_errorname)

        else:
            self.nombreCiudad.setStyleSheet("color:white;background-color: rgb(30, 30, 30);border:none;")
            self.seleccionarImagen.hide()
            self.guardarCambios.hide()
            self.nombreCiudad.setReadOnly(True)
            self.desc_ciudad.setReadOnly(True)

            self.editarCty = False
            self.cargarInfoCiudadSeleccionada()

            if self.ciudadComboBox.currentIndex() == -1:
                QMessageBox.warning(self, "Aviso", "No se ha seleccionado ninguna ciudad")

    def eliminar(self):
        # Función que permite al usuario eliminar una ciudad y sus sitios a la vez
        if not self.ciudadComboBox.currentIndex() == -1:
            try:
                idC = self.conexion.execute("SELECT c.ID FROM Ciudades c WHERE c.Nombre = ?", (self.ciudadComboBox.currentText(),)).fetchone()
                if idC != None:
                    self.conexion.execute("DELETE FROM Ciudades WHERE ID = ?", (int(idC[0]),))
                    self.conexion.execute("DELETE FROM Sitios WHERE Ciudad = ?", (int(idC[0]),))
                    self.conexion.commit()

                    self.ciudadComboBox.clear()
                    self.nombreCiudad.setText("")
                    self.desc_ciudad.setPlainText("")
                    self.img_ciudad.setPixmap(QPixmap())
                    
                    QMessageBox.information(self, "Resultado", "Ciudad seleccionada eliminada correctamente")
                    self.cargarCiudades()
                    
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
                    QMessageBox.warning(self, "Resultado", "Error al eliminar la ciudad seleccionada")

            except sqlite3.Error as e:
                print(e.sqlite_errorcode)
                print(e.sqlite_errorname)
                self.conexion.rollback()

                QMessageBox.warning(self, "Resultado", "Error al eliminar la ciudad seleccionada")
        else:
            QMessageBox.warning(self, "Aviso", "No se ha seleccionado ninguna ciudad")

    def cargarCiudades(self):
        # Función que carga las ciudades guardadas en la BD
        if self.conexion:
            self.ciudadComboBox.clear()
            self.aviso.hide()

            ciudades = self.conexion.execute("SELECT Nombre FROM Ciudades ORDER BY Nombre")
            for ciudad in ciudades.fetchall():
                self.ciudadComboBox.addItem(ciudad[0])
                self.ciudadComboBox.setCurrentIndex(-1)
                self.frame_ciudad.hide()

            if self.ciudadComboBox.count() <= 0:
                QMessageBox.warning(self, "Aviso", "No hay datos de ciudades guardadas, añade una pulsando al botón correspondiente")
                self.ciudadLabel.hide()
                self.ciudadComboBox.hide()
                self.frame_ciudad.hide()

            elif self.ciudadComboBox.count() > 0:
                self.ciudadLabel.show()
                self.ciudadComboBox.show()

                if self.cityEditada:
                    self.frame_ciudad.show()
                    self.cityEditada = False
                else:
                    self.aviso.setText("SELECCIONE UNA CIUDAD")
                    self.aviso.show()
        else:
            QMessageBox.warning(self, "Aviso", "Error de conexión a la BD")
            raise InitialisationError("Error de conexión a la BD.")
        
    def registrarCiudad(self):
        # Función que permite al usuario registrar una nueva ciudad
        self.close()

        self.ventana = AgregarCiudades()
        self.ventana.closing.connect(self.cerrarVentana)

        self.ventana.guardarCiudad.clicked.connect(self.cargarCiudades)
        self.ventana.guardarCiudad.clicked.connect(self.ciudadLabel.show)
        self.ventana.guardarCiudad.clicked.connect(self.ciudadComboBox.show)
        self.ventana.guardarCiudad.clicked.connect(self.mostrarIndicativo)

        self.ventana.show()

    def mostrarIndicativo(self):
        # Función que muestra un mensaje indicando al usuario que hay nuevas ciudades disponibles
        self.vecesRegistrar += 1

        if self.vecesRegistrar == 1:
            self.aviso.setText("¡NUEVA CIUDAD REGISTRADA!")
        elif self.vecesRegistrar > 1:
            self.aviso.setText("¡NUEVAS CIUDADES REGISTRADAS!")

        self.aviso.show()

    def cargarInfoCiudadSeleccionada(self):
        # Función que carga la información completa de la ciudad seleccionada
        ciudad = self.conexion.execute("SELECT c.Imagen, c.Descripcion FROM Ciudades c WHERE c.Nombre = ?", (self.ciudadComboBox.currentText(),)).fetchone()
        if ciudad:
            self.aviso.hide()

            imagen = ciudad[0]
            desc = ciudad[1]

            # Sacar imagen de la BD
            pixmap = QPixmap()
            pixmap.loadFromData(imagen, "PNG")

            if not pixmap.isNull():
                self.img_ciudad.setPixmap(pixmap)
                self.img_ciudad.setScaledContents(True)
                self.imagen = imagen
            else:
                self.img_ciudad.setPixmap(QPixmap())

            self.desc_ciudad.setPlainText(str(desc))
            self.frame_ciudad.show()
            self.nombreCiudad.setText(self.ciudadComboBox.currentText())

    def closeEvent(self, event):
        # Función que el usuario al cerrar la ventana se le vuelve a la ventana de inicio
        self.closing.emit()
        super().closeEvent(event)

    def cerrarVentana(self):
        self.vecesRegistrar = 0

        self.ventana.close()
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    manejarCiudades = ManejarCiudades()
    manejarCiudades.show()
    sys.exit(app.exec())