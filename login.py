# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets

#importar a classe da tela que deseja abrir
from menu import Ui_TelaMenu

class Ui_TelaLogin(object):
    def setupUi(self, TelaLogin):
        TelaLogin.setObjectName("TelaLogin")
        TelaLogin.resize(297, 116)
        self.centralwidget = QtWidgets.QWidget(TelaLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_usuario = QtWidgets.QLabel(self.centralwidget)
        self.label_usuario.setObjectName("label_usuario")
        self.gridLayout.addWidget(self.label_usuario, 0, 0, 1, 1)
        self.lineEdit_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.gridLayout.addWidget(self.lineEdit_usuario, 0, 1, 1, 1)
        self.label_senha = QtWidgets.QLabel(self.centralwidget)
        self.label_senha.setObjectName("label_senha")
        self.gridLayout.addWidget(self.label_senha, 1, 0, 1, 1)
        self.lineEdit_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.gridLayout.addWidget(self.lineEdit_senha, 1, 1, 1, 1)
        self.pushButton_entrar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_entrar.setObjectName("pushButton_entrar")
        
        self.pushButton_entrar.clicked.connect(self.efetuar_login)
        
        self.gridLayout.addWidget(self.pushButton_entrar, 2, 1, 1, 1)
        TelaLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaLogin)
        QtCore.QMetaObject.connectSlotsByName(TelaLogin)

    def retranslateUi(self, TelaLogin):
        _translate = QtCore.QCoreApplication.translate
        TelaLogin.setWindowTitle(_translate("TelaLogin", "ACESSO AO SISTEMA"))
        self.label_usuario.setText(_translate("TelaLogin", "Usuário:"))
        self.label_senha.setText(_translate("TelaLogin", "Senha:"))
        self.pushButton_entrar.setText(_translate("TelaLogin", "ENTRAR"))


    def efetuar_login(self):
        usuario = self.lineEdit_usuario.text()
        senha   = self.lineEdit_senha.text()
        
        if usuario == "gerente" and senha == "9876" :
            
            # criar uma tela vazia
            self.tela = QtWidgets.QMainWindow()
            # criar um objeto da tela que deseja exibir
            self.menu = Ui_TelaMenu()
            # associar a tela vazia com o código da tela a exibir
            self.menu.setupUi(self.tela)
            # exibir a nova tela
            self.tela.show()
            # fechar a tela de login
            TelaLogin.close()
            
        else:
            from PyQt5.QtWidgets import QMessageBox
            msg = QMessageBox()
            msg.setText("USUÁRIO OU SENHA INCORRETOS")
            msg.exec_()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaLogin = QtWidgets.QMainWindow()
    ui = Ui_TelaLogin()
    ui.setupUi(TelaLogin)
    TelaLogin.show()
    sys.exit(app.exec_())
