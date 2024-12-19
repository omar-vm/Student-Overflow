from backend import create_app  # Usa la instancia configurada en __init__.py
from frontend.login import LoginWindow
from PyQt6.QtWidgets import QApplication
import threading
import sys
from dotenv import load_dotenv

load_dotenv()

def run_flask_app():
    app = create_app()  # Crea la instancia de Flask
    app.run(port=5001, use_reloader=False)  # Corre Flask en el puerto 5001

if __name__ == "__main__":
    # Inicia el hilo de Flask
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.daemon = True
    flask_thread.start()

    # Inicia la interfaz gráfica con PyQt6
    qt_app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(qt_app.exec())
