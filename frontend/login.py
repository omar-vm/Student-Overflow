from PyQt6 import QtWidgets

from .dashboard import DashboardWindow


from .signup import SignUpWindow
from templates.StudenOverf.ui_login import Ui_Widget
import requests
from PyQt6.QtWidgets import QMessageBox


class LoginWindow(QtWidgets.QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.botonIniciarsesion.clicked.connect(self.login)
        self.botonRegistrarse.clicked.connect(self.open_signup_window)

    def login(self):
        email = self.inputCorreo.text().strip()
        password = self.inputContrasenia.text().strip()

        if not email or not password:
            QMessageBox.warning(self, "Error", "Correo y contraseña son requeridos")
            return

        try:
            response = requests.post('http://127.0.0.1:5001/login', json={"email": email, "password": password})

            if response.status_code == 200:
                data = response.json()
                self.hide()
                self.dashboard_window = DashboardWindow(data["access_token"])
                self.dashboard_window.show()
            else:
                QMessageBox.warning(self, "Error", f"Error al iniciar sesión: {response.status_code} - {response.text}")

        except requests.exceptions.ConnectionError:
            QMessageBox.critical(self, "Error", "No se pudo conectar con el servidor")

    def open_signup_window(self):
        self.signup_window = SignUpWindow()
        self.signup_window.show()
