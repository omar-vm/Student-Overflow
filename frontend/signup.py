from PyQt6 import QtWidgets
from templates.StudenOverf.ui_signup import Ui_SignUpForm
import requests
from PyQt6.QtWidgets import QMessageBox

class SignUpWindow(QtWidgets.QMainWindow, Ui_SignUpForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.botonRegistrar.clicked.connect(self.register)

    def register(self):
        name = self.inputNombre.text().strip()
        username = self.inputUsername.text().strip()
        email = self.inputCorreo.text().strip()
        phone = self.inputTelefono.text().strip()
        password = self.inputContrasenia.text().strip()
        confirm_password = self.inputConfirmarContrasenia.text().strip()

        if not all([name, username, email, password, confirm_password]):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden")
            return
        try:
            response = requests.post(
                'http://127.0.0.1:5001/signup',
                json={
                    "name": name,
                    "username": username,
                    "email": email,
                    "phone": phone,
                    "password": password,
                    "confirm_password": confirm_password
                }
            )


            if response.status_code == 201:
                QMessageBox.information(self, "Éxito", "Usuario registrado con éxito")
                self.close()
            else:
                QMessageBox.warning(self, "Error", f"Error al registrar usuario: {response.status_code} - {response.text}")

        except requests.exceptions.ConnectionError:
            QMessageBox.critical(self, "Error", "No se pudo conectar con el servidor")
