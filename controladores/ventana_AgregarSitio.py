import sys, os, sqlite3, shutil
from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QBuffer, QIODevice, Signal
from modelos.InitialisationError import InitialisationError
from vistas.agregarSitios_ui import Ui_agregarSitios

class AgregarSitios(QWidget, Ui_agregarSitios):
    closing = Signal()

    def __init__(self, IDCiudad=None):
        super().__init__()
        self.setupUi(self)

        # Variables auxiliares
        self.ventana = 0
        self.imagen = None
        self.ciudad = IDCiudad

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
        self.setWindowIcon(QIcon(os.getcwd() + "/recursos/img/sitios.png"))
        self.seleccionarImagen.setIcon(QIcon(os.getcwd() + "/recursos/iconos/ic_imagen.png"))
        self.cerrar.setIcon(QIcon(os.getcwd() + "/recursos/iconos/cerrar.png"))
        self.guardarSitio.setIcon(QIcon(os.getcwd() + "/recursos/iconos/ic_guardar.png"))

        # Configuraciones importantes
        self.cargarCiudades()

        # Acciones
        self.seleccionarImagen.clicked.connect(self.imagenSitio)
        self.cerrar.clicked.connect(self.retroceder)
        self.guardarSitio.clicked.connect(self.guardarCambios)

    def guardarCambios(self):
        # Función que permite al usuario guardar el sitio introducido
        if len(self.nombreLineEdit.text()) > 0 and self.ciudadComboBox.currentIndex() != -1:
            idS = self.conexion.execute("SELECT MAX(ID) FROM Sitios").fetchone()
            nuevoID = 0
            if idS[0] != None:
                nuevoID = idS[0] + 1
            else:
                nuevoID = 1

            idC = self.conexion.execute("SELECT c.ID FROM Ciudades c WHERE c.Nombre = ?", (self.ciudadComboBox.currentText(),)).fetchone()
            idCiudad = int(idC[0])
            try:
                self.conexion.execute("INSERT INTO Sitios VALUES (?, ?, ?, ?, ?)", (nuevoID, self.nombreLineEdit.text(), self.desc_sitio.toPlainText(), self.imagen, idCiudad,))
                self.conexion.commit()

                QMessageBox.information(self, "Resultado", "Sitio registrado correctamente")

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

                QMessageBox.warning(self, "Aviso", "Esa sitio existe, utiliza otro nombre diferente")

            except sqlite3.Error as e:
                print(e.sqlite_errorcode)
                print(e.sqlite_errorname)
                self.conexion.rollback()

                QMessageBox.warning(self, "Resultado", "Error al registrar el sitio")
        else:
            if len(self.nombreLineEdit.text()) <= 0:
                QMessageBox.warning(self, "Resultado", "No se ha introducido el nombre del sitio")

            if self.ciudadComboBox.currentIndex() == -1:
                QMessageBox.warning(self, "Resultado", "No se ha introducido la ciudad del sitio")

    def retroceder(self):
        # Función que permite al usuario cancelar el guardado del sitio introducido
        self.close()

    def imagenSitio(self):
        # Función que permite al usuario seleccionar una imagen para añadir un sitio
        ruta_imagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen sitio", "", "Archivos de Imagen (*.png *.jpg *.jpeg *.bmp)")
        if ruta_imagen:
            pixmap = QPixmap(ruta_imagen)
            self.img_sitio.setPixmap(pixmap)
            self.img_sitio.setScaledContents(True)

            # Convertimos la imagen para que sea insertable en la BD
            buffer = QBuffer()
            abrir = buffer.open(QIODevice.WriteOnly)
            if abrir:
                guardado = pixmap.save(buffer, "JPG")
                if not guardado:
                    buffer.close()
                else:
                    byte_array = buffer.data()
                    buffer.close()
                    self.imagen = bytes(byte_array)

    def cargarCiudades(self):
        # Función que carga las ciudades guardadas en la BD
        if self.conexion:
            ciudades = self.conexion.execute("SELECT Nombre FROM Ciudades ORDER BY Nombre")
            for ciudad in ciudades.fetchall():
                self.ciudadComboBox.addItem(ciudad[0])
                self.ciudadComboBox.setCurrentIndex(-1)

            if self.ciudadComboBox.count() <= 0:
                QMessageBox.warning(self, "Aviso", "No hay datos de ciudades guardadas, añade una pulsando al botón correspondiente")
        else:
            QMessageBox.warning(self, "Aviso", "Error de conexión a la BD")
            raise InitialisationError("Error de conexión a la BD.")

    def closeEvent(self, event):
        # Función que el usuario al cerrar la ventana se le vuelve a la ventana de anterior
        self.closing.emit()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    agregarSitios = AgregarSitios()
    agregarSitios.show()
    sys.exit(app.exec())