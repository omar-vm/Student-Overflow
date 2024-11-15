from backend import conf_app
from frontend.login import LoginWindow
from PyQt6.QtWidgets import QApplication
import threading
import sys

def run_flask_app():
    app = conf_app()
    app.run(port=5001, use_reloader=False)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.daemon = True
    flask_thread.start()

    qt_app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(qt_app.exec())
