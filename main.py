import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap
from vistas.main_ui import Ui_Inicio
from modelos.InitialisationError import InitialisationError

from controladores.ventana_ManejarSitios import ManejarSitios
from controladores.ventana_ManejarCiudades import ManejarCiudades

class Main(QMainWindow, Ui_Inicio):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Variables auxiliares
        self.ventana = 0

        # Establecer las imágenes
        self.img_sitios.setPixmap(QPixmap(os.getcwd() + "/recursos/img/sitios.png"))
        self.img_ciudades.setPixmap(QPixmap(os.getcwd() + "/recursos/img/ciudades.png"))

        # Señales (Acciones)
        self.manejarSitios.clicked.connect(self.manejar_sitios)
        self.manejarCiudades.clicked.connect(self.manejar_ciudades)

    def manejar_sitios(self):
        # Función para manejar sitios
        try:
            self.ventana = ManejarSitios()
            self.ventana.closing.connect(self.cerrarVentana)
            self.ventana.show()

        except InitialisationError as e:
            pass
        
        except Exception as e:
            pass

    def manejar_ciudades(self):
        # Función para manejar ciudades
        self.close()
        
        self.ventana = ManejarCiudades()
        self.ventana.closing.connect(self.cerrarVentana)
        self.ventana.show()

    def cerrarVentana(self):
        self.ventana.close()
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())