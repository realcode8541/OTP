import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from random import *
import os

def encrypt_otp(filename):
    to_encrypt = open(filename, "rb").read()
    size = len(to_encrypt)
    key = os.urandom(size)
    with open(filename + ".key", "wb") as key_out:
        key_out.write(key)
        encrypted = bytes(a ^ b for (a, b) in zip(to_encrypt, key))
        with open(filename, "wb") as encrypted_out:
            encrypted_out.write(encrypted)

def decrypt_otp(filename, key):
    file = open(filename, "rb").read()
    key = open(key, "rb").read()
    decrypted = bytes(a ^ b for (a, b) in zip(file, key))
    with open(filename, "wb") as decrypted_out:
        decrypted_out.write(decrypted)

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):

        #Window
        
        self.setGeometry(750, 350, 350, 190)
        self.setWindowTitle("SIMPLE OTP")

        #Headline

        self.headline = QLabel("SIMPLE OTP", self)
        self.headline.setFont(QFont("Arial", 20))
        self.headline.adjustSize()
        self.headline.move(90, 50)

        #Buttons

        encrypt_function = QPushButton("Verschlüsseln", self)
        encrypt_function.move(60, 150)
        encrypt_function.clicked.connect(self.encrypt_function)

        decrypt_function = QPushButton("Entschlüsseln", self)
        decrypt_function.clicked.connect(self.decrypt_function)
        decrypt_function.move(200, 150)

        self.show()
    
    def console(self, text):
        print("console wurde aufgerufen")
        if text == "console.quit":
            quit()
        if text == "console.file":
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
            if fileName:
                print(fileName)

    def encrypt_function(self):
        print("encrypt_function wurde aufgerufen")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        encrypt_otp(fileName)

    def decrypt_function(self):
        file = self.QLine1.text()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        decrypt_otp(fileName, fileName+".key")


app = QApplication(sys.argv)
w = Fenster()
w.show()
sys.exit(app.exec_())
