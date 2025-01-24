# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Janela(object):
    def setupUi(self, Janela):
        Janela.setObjectName("Janela")
        Janela.resize(346, 228)
        self.centralwidget = QtWidgets.QWidget(Janela)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 0, 0, 1, 1)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.gridLayout.addWidget(self.lineEdit_nome, 0, 1, 1, 1)
        self.label_curso = QtWidgets.QLabel(self.centralwidget)
        self.label_curso.setObjectName("label_curso")
        self.gridLayout.addWidget(self.label_curso, 1, 0, 1, 1)
        self.comboBox_curso = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_curso.setCurrentText("")
        self.comboBox_curso.setObjectName("comboBox_curso")
        self.comboBox_curso.addItem("")
        self.comboBox_curso.addItem("")
        self.comboBox_curso.addItem("")
        self.comboBox_curso.addItem("")
        self.gridLayout.addWidget(self.comboBox_curso, 1, 1, 1, 1)
        self.label_turno = QtWidgets.QLabel(self.centralwidget)
        self.label_turno.setObjectName("label_turno")
        self.gridLayout.addWidget(self.label_turno, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_manha = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_manha.setCheckable(True)
        self.radioButton_manha.setChecked(False)
        self.radioButton_manha.setObjectName("radioButton_manha")
        self.horizontalLayout.addWidget(self.radioButton_manha)
        self.radioButton_tarde = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_tarde.setObjectName("radioButton_tarde")
        self.horizontalLayout.addWidget(self.radioButton_tarde)
        self.radioButton_noite = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_noite.setObjectName("radioButton_noite")
        self.horizontalLayout.addWidget(self.radioButton_noite)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.label_extra = QtWidgets.QLabel(self.centralwidget)
        self.label_extra.setObjectName("label_extra")
        self.gridLayout.addWidget(self.label_extra, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_atleta = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_atleta.setObjectName("checkBox_atleta")
        self.horizontalLayout_2.addWidget(self.checkBox_atleta)
        self.checkBox_bolsista = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_bolsista.setObjectName("checkBox_bolsista")
        self.horizontalLayout_2.addWidget(self.checkBox_bolsista)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.label_observacao = QtWidgets.QLabel(self.centralwidget)
        self.label_observacao.setObjectName("label_observacao")
        self.gridLayout.addWidget(self.label_observacao, 4, 0, 1, 1)
        self.plainTextEdit_observacao = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_observacao.setObjectName("plainTextEdit_observacao")
        self.gridLayout.addWidget(self.plainTextEdit_observacao, 4, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_limpar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_limpar.setObjectName("pushButton_limpar")
        
        self.pushButton_limpar.clicked.connect(self.limpar)
        
        self.horizontalLayout_3.addWidget(self.pushButton_limpar)
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        
        self.pushButton_salvar.clicked.connect(self.salvar) #liga na função
        
        self.horizontalLayout_3.addWidget(self.pushButton_salvar)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 1, 1, 1)
        Janela.setCentralWidget(self.centralwidget)

        self.retranslateUi(Janela)
        self.comboBox_curso.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Janela)

    def retranslateUi(self, Janela):
        _translate = QtCore.QCoreApplication.translate
        Janela.setWindowTitle(_translate("Janela", "Cadastro"))
        self.label_nome.setText(_translate("Janela", "Nome:"))
        self.label_curso.setText(_translate("Janela", "Curso:"))
        self.comboBox_curso.setItemText(0, _translate("Janela", "Desenhista"))
        self.comboBox_curso.setItemText(1, _translate("Janela", "Eletricista"))
        self.comboBox_curso.setItemText(2, _translate("Janela", "Mecânico"))
        self.comboBox_curso.setItemText(3, _translate("Janela", "Técnico em Informática"))
        self.label_turno.setText(_translate("Janela", "Turno:"))
        self.radioButton_manha.setText(_translate("Janela", "Manhã"))
        self.radioButton_tarde.setText(_translate("Janela", "Tarde"))
        self.radioButton_noite.setText(_translate("Janela", "Noite"))
        self.label_extra.setText(_translate("Janela", "Extra:"))
        self.checkBox_atleta.setText(_translate("Janela", "Atleta"))
        self.checkBox_bolsista.setText(_translate("Janela", "Bolsista"))
        self.label_observacao.setText(_translate("Janela", "Observação:"))
        self.pushButton_limpar.setText(_translate("Janela", "LIMPAR"))
        self.pushButton_salvar.setText(_translate("Janela", "SALVAR"))
        
        
    def salvar(self):
        nome = self.lineEdit_nome.text()  # capturar o nome
        curso = self.comboBox_curso.currentText() # captura o curso
        
        turno = "Indefinido"
        if self.radioButton_manha.isChecked(): turno = "Manhã"
        elif self.radioButton_tarde.isChecked(): turno = "Tarde"
        elif self.radioButton_noite.isChecked(): turno = "Noite"
        
        atleta = "Não"
        if self.checkBox_atleta.isChecked(): atleta = "Sim"
        
        bolsista = "Não"
        if self.checkBox_bolsista.isChecked(): bolsista = "Sim"
        
        observacao = self.plainTextEdit_observacao.toPlainText()
        dados = [nome, curso, turno, atleta, bolsista, observacao]
        
        import csv
        arq = open("alunos.csv","a",newline="")
        grav = csv.writer(arq)
        grav.writerow(dados)
        arq.close()
        print("GRAVADO COM SUCESSO!")
    
    def limpar(self):
        self.lineEdit_nome.setText("")
        self.comboBox_curso.setCurrentIndex(-1)
        self.radioButton_manha.setChecked(False)
        self.radioButton_tarde.setChecked(False)
        self.radioButton_noite.setChecked(False)
        self.checkBox_atleta.setChecked(False)
        self.checkBox_bolsista.setChecked(False)
        self.plainTextEdit_observacao.setPlainText("")
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Janela = QtWidgets.QMainWindow()
    ui = Ui_Janela()
    ui.setupUi(Janela)
    Janela.show()
    sys.exit(app.exec_())
