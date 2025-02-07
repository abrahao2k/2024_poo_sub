# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CadProduto(object):
    def setupUi(self, CadProduto):
        CadProduto.setObjectName("CadProduto")
        CadProduto.resize(290, 122)
        self.centralwidget = QtWidgets.QWidget(CadProduto)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_nome)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_nome)
        self.label_fabricante = QtWidgets.QLabel(self.centralwidget)
        self.label_fabricante.setObjectName("label_fabricante")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_fabricante)
        self.lineEdit_fabricante = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_fabricante.setObjectName("lineEdit_fabricante")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fabricante)
        self.label_preco = QtWidgets.QLabel(self.centralwidget)
        self.label_preco.setObjectName("label_preco")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_preco)
        self.lineEdit_preco = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_preco.setObjectName("lineEdit_preco")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_preco)
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        
        self.pushButton_salvar.clicked.connect(self.salvar)
        
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_salvar)
        CadProduto.setCentralWidget(self.centralwidget)

        self.retranslateUi(CadProduto)
        QtCore.QMetaObject.connectSlotsByName(CadProduto)

    def retranslateUi(self, CadProduto):
        _translate = QtCore.QCoreApplication.translate
        CadProduto.setWindowTitle(_translate("CadProduto", "Cadastro de Produtos"))
        self.label_nome.setText(_translate("CadProduto", "Nome:"))
        self.label_fabricante.setText(_translate("CadProduto", "Fabricante:"))
        self.label_preco.setText(_translate("CadProduto", "Preço:"))
        self.pushButton_salvar.setText(_translate("CadProduto", "SALVAR"))


    def salvar(self):
        nome = self.lineEdit_nome.text()
        fabr = self.lineEdit_fabricante.text()
        pre  = self.lineEdit_preco.text()       #  30,90    30.90
        pre  = pre.replace("," , ".")
        
        import csv
        arq = open("dados.csv", "a", newline="")
        gravador = csv.writer(arq)
        gravador.writerow([nome, fabr, pre])
        arq.close()
        
        from PyQt5.QtWidgets import QMessageBox
        msg = QMessageBox()
        msg.setText("Gravado com sucesso.")
        msg.exec_()
        
        self.lineEdit_nome.setText("")
        self.lineEdit_fabricante.setText("")
        self.lineEdit_preco.setText("")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CadProduto = QtWidgets.QMainWindow()
    ui = Ui_CadProduto()
    ui.setupUi(CadProduto)
    CadProduto.show()
    sys.exit(app.exec_())
