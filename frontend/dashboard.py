from PyQt6 import QtWidgets, QtGui
from templates.StudenOverf.ui_dashboard import Ui_MainWindow
import requests
from PyQt6.QtWidgets import QMessageBox, QInputDialog

class DashboardWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, access_token):
        super().__init__()
        self.setupUi(self)
        self.access_token = access_token
        self.pushButton_create_question.clicked.connect(self.create_new_question)
        self.pushButton_refresh.clicked.connect(self.load_questions)
        self.pushButton_logout.clicked.connect(self.logout)
        self.listView_questions.clicked.connect(self.open_question)

    def create_new_question(self):
        title, ok = QtWidgets.QInputDialog.getText(self, "Crear Pregunta", "Título de la pregunta:")
        if not ok or not title:
            return

        content, ok = QtWidgets.QInputDialog.getMultiLineText(self, "Crear Pregunta", "Contenido de la pregunta:")
        if not ok or not content:
            return

        try:
            response = requests.post(
                'http://127.0.0.1:5001/dashboard/questions',
                json={"title": title, "content": content},
                headers={"Authorization": f"Bearer {self.access_token}"}
            )
            
            print(f"Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")

            if response.status_code == 201:
                try:
                    json_data = response.json()
                    QMessageBox.information(self, "Éxito", "Pregunta creada con éxito")
                    self.load_questions()
                except requests.exceptions.JSONDecodeError:
                    QMessageBox.warning(self, "Error", "La respuesta del servidor no es un JSON válido")
            else:
                QMessageBox.warning(self, "Error", response.text)
        except requests.exceptions.ConnectionError:
            QMessageBox.critical(self, "Error", "No se pudo conectar con el servidor")




    def load_questions(self):
        try:
            response = requests.get(
                'http://127.0.0.1:5001/dashboard/questions',
                headers={"Authorization": f"Bearer {self.access_token}"}
            )
            if response.status_code == 200:
                questions = response.json()
                self.questions = questions 
                model = QtGui.QStandardItemModel()
                for question in questions:
                    item = QtGui.QStandardItem(question['title'])
                    item.setData(question['id']) 
                    model.appendRow(item)
                self.listView_questions.setModel(model)
            else:
                QMessageBox.warning(self, "Error", response.json().get("error", "Error al obtener preguntas"))
        except requests.exceptions.ConnectionError:
            QMessageBox.critical(self, "Error", "No se pudo conectar con el servidor")

    def open_question(self, index):
        question_id = self.listView_questions.model().itemFromIndex(index).data()
        try:
            response = requests.get(
                f'http://127.0.0.1:5001/dashboard/questions/{question_id}',
                headers={"Authorization": f"Bearer {self.access_token}"}
            )
            if response.status_code == 200:
                question = response.json()
                self.show_question_details(question)
            else:
                QMessageBox.warning(self, "Error", response.json().get("error", "Error al obtener la pregunta"))
        except requests.exceptions.ConnectionError:
            QMessageBox.critical(self, "Error", "No se pudo conectar con el servidor")

    def show_question_details(self, question):
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle("Detalles de la Pregunta")
        msg_box.setText(f"Título: {question['title']}\n\nContenido: {question['content']}\n\nUsuario: {question['user']}\n\nComentarios:")
        for comment in question['comments']:
            msg_box.setInformativeText(msg_box.informativeText() + f"\n- {comment['user']}: {comment['content']}")


        add_comment_btn = msg_box.addButton("Agregar Comentario", QtWidgets.QMessageBox.ButtonRole.ActionRole)
        add_tag_btn = msg_box.addButton("Agregar Tag", QtWidgets.QMessageBox.ButtonRole.ActionRole)
        msg_box.addButton(QtWidgets.QMessageBox.StandardButton.Close)

        msg_box.exec()

        if msg_box.clickedButton() == add_comment_btn:
            self.add_comment_to_question(question['id'])
        elif msg_box.clickedButton() == add_tag_btn:
            self.add_tag_to_question(question['id'])

    def add_comment_to_question(self, question_id):
        comment, ok = QInputDialog.getText(self, "Agregar Comentario", "Escribe tu comentario:")
        if ok and comment:
            try:
                response = requests.post(
                    f'http://127.0.0.1:5001/dashboard/questions/{question_id}/comments',
                    json={"content": comment},
                    headers={"Authorization": f"Bearer {self.access_token}"}
                )
                if response.status_code == 201:
                    QMessageBox.information(self, "Éxito", "Comentario agregado exitosamente")
                    self.load_questions()
                else:
                    QMessageBox.warning(self, "Error", response.json().get("error", "Error al agregar comentario"))
            except requests.exceptions.ConnectionError:
                QMessageBox.critical(self, "Error", "No se pudo conectar con el servidor")

    def add_tag_to_question(self, question_id):
        tag, ok = QInputDialog.getText(self, "Agregar Tag", "Escribe el nombre del tag:")
        if ok and tag:
            try:
                response = requests.post(
                    f'http://127.0.0.1:5001/dashboard/questions/{question_id}/tags',
                    json={"tag": tag},
                    headers={"Authorization": f"Bearer {self.access_token}"}
                )
                if response.status_code == 201:
                    QMessageBox.information(self, "Éxito", "Tag agregado exitosamente")
                    self.load_questions()
                else:
                    QMessageBox.warning(self, "Error", response.json().get("error", "Error al agregar tag"))
            except requests.exceptions.ConnectionError:
                QMessageBox.critical(self, "Error", "No se pudo conectar con el servidor")

    def logout(self):
        self.close()
