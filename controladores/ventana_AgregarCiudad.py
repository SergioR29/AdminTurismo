import sys, os, sqlite3, shutil
from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QBuffer, QIODevice, Signal
from vistas.agregarCiudades_ui import Ui_agregarCiudades

class AgregarCiudades(QWidget, Ui_agregarCiudades):
    closing = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Variables auxiliares
        self.ventana = 0
        self.imagen = None

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
        self.seleccionarImagen.setIcon(QIcon(os.getcwd() + "/recursos/iconos/ic_imagen.png"))
        self.descartar.setIcon(QIcon(os.getcwd() + "/recursos/iconos/ic_descartar.png"))
        self.guardarCiudad.setIcon(QIcon(os.getcwd() + "/recursos/iconos/ic_guardar.png"))

        # Acciones
        self.seleccionarImagen.clicked.connect(self.imagenCiudad)
        self.descartar.clicked.connect(self.retroceder)
        self.guardarCiudad.clicked.connect(self.guardarCambios)

    def guardarCambios(self):
        # Función que guarda la ciudad registrada por el usuario
        if len(self.nombreLineEdit.text()) > 0:
            idC = self.conexion.execute("SELECT MAX(ID) FROM Ciudades").fetchone()
            nuevoID = 0

            if idC[0] != None:
                nuevoID = idC[0] + 1
            else:
                nuevoID = 1

            try:
                self.conexion.execute("INSERT INTO Ciudades VALUES (?, ?, ?, ?)", (nuevoID, self.nombreLineEdit.text(), self.imagen, self.desc_ciudad.toPlainText()))
                self.conexion.commit()

                QMessageBox.information(self, "Resultado", "Ciudad registrada correctamente")

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

            except sqlite3.IntegrityError as e:
                print(e.sqlite_errorcode)
                print(e.sqlite_errorname)
                self.conexion.rollback()

                QMessageBox.warning(self, "Aviso", "Esa ciudad existe, utiliza otro nombre diferente")

            except sqlite3.Error as e:
                print(e.sqlite_errorcode)
                print(e.sqlite_errorname)
                self.conexion.rollback()

                QMessageBox.warning(self, "Resultado", "Error al registrar la ciudad")
        else:
            QMessageBox.warning(self, "Resultado", "No se ha intorducido el nombre de la ciudad")
    
    def retroceder(self):
        # Función que permite al usuario cancelar el guardado del sitio introducido
        self.close()

    def imagenCiudad(self):
        # Función que permite al usuario seleccionar una imagen para añadir una ciudad
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

    def closeEvent(self, event):
        # Función que el usuario al cerrar la ventana se le vuelve a la ventana de anterior
        self.closing.emit()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    agregarCiudades = AgregarCiudades()
    agregarCiudades.show()
    sys.exit(app.exec())