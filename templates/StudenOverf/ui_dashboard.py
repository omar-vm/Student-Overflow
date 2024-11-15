from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, -10, 781, 41))
        self.widget_2.setObjectName("widget_2")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.label_welcome = QtWidgets.QLabel(self.widget_2)
        self.label_welcome.setObjectName("label_welcome")
        self.horizontalLayout.addWidget(self.label_welcome)
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        
        self.label_title = QtWidgets.QLabel(self.widget_2)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout.addWidget(self.label_title)
        
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        
        self.pushButton_logout = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_logout.setFont(font)
        self.pushButton_logout.setStyleSheet("background-color: rgb(192, 0, 0);")
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.horizontalLayout.addWidget(self.pushButton_logout)
        
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(0, 30, 781, 41))
        self.widget_3.setObjectName("widget_3")
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.pushButton_create_question = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_create_question.setFont(font)
        self.pushButton_create_question.setObjectName("pushButton_create_question")
        self.horizontalLayout_2.addWidget(self.pushButton_create_question)
        
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        
        self.pushButton_refresh = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_refresh.setFont(font)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.horizontalLayout_2.addWidget(self.pushButton_refresh)
        
        self.pushButton_view_question = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_view_question.setFont(font)
        self.pushButton_view_question.setObjectName("pushButton_view_question")
        self.horizontalLayout_2.addWidget(self.pushButton_view_question)
        
        self.listView_questions = QtWidgets.QListView(self.widget)
        self.listView_questions.setGeometry(QtCore.QRect(10, 80, 771, 321))
        self.listView_questions.setObjectName("listView_questions")
        
        self.textEdit_question_details = QtWidgets.QTextEdit(self.widget)
        self.textEdit_question_details.setGeometry(QtCore.QRect(10, 410, 771, 81))
        self.textEdit_question_details.setReadOnly(True)
        self.textEdit_question_details.setObjectName("textEdit_question_details")
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.lineEdit_tag = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_tag.setObjectName("lineEdit_tag")
        self.horizontalLayout_3.addWidget(self.lineEdit_tag)
        
        self.pushButton_add_tag = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_add_tag.setFont(font)
        self.pushButton_add_tag.setObjectName("pushButton_add_tag")
        self.horizontalLayout_3.addWidget(self.pushButton_add_tag)
        
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        
        self.lineEdit_comment = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_comment.setGeometry(QtCore.QRect(10, 500, 661, 31))
        self.lineEdit_comment.setObjectName("lineEdit_comment")
        
        self.pushButton_add_comment = QtWidgets.QPushButton(self.widget)
        self.pushButton_add_comment.setGeometry(QtCore.QRect(680, 500, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_add_comment.setFont(font)
        self.pushButton_add_comment.setObjectName("pushButton_add_comment")
        
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_welcome.setText(_translate("MainWindow", "Bienvenido, Usuario"))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">Student</span><span style=\" font-weight:700;\">Overflow</span></p></body></html>"))
        self.pushButton_logout.setText(_translate("MainWindow", "Cerrar sesión"))
        self.pushButton_create_question.setText(_translate("MainWindow", "Crear nueva pregunta"))
        self.pushButton_refresh.setText(_translate("MainWindow", "Actualizar"))
        self.pushButton_view_question.setText(_translate("MainWindow", "Ver pregunta"))
        self.pushButton_add_tag.setText(_translate("MainWindow", "Agregar etiqueta"))
        self.lineEdit_tag.setPlaceholderText(_translate("MainWindow", "Agregar etiqueta de temática"))
        self.pushButton_add_comment.setText(_translate("MainWindow", "Agregar comentario"))
        self.lineEdit_comment.setPlaceholderText(_translate("MainWindow", "Escribir comentario"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
