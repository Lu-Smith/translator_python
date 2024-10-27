import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout, QTextEdit,
                             QLabel, QComboBox, QPushButton)
from deep_translator import GoogleTranslator

class Translator(QWidget):
  def __init__(self):
    super().__init__()
    
    self.initUI()
    
  def initUI(self):
    self.setWindowTitle("Translator App")
    self.setGeometry(100, 100, 400, 500)
    
    self.setStyleSheet("background-color: rgb(54, 15, 99);")
    
    # layout
    layout = QVBoxLayout()
    
    # input
    self.inputText = QTextEdit(self)
    self.inputText.setPlaceholderText("Enter text to translate...")
    inputLabel = QLabel("Input Text:")
    inputLabel.setStyleSheet("""
        QLabel {
            color: #f4f4f4;
            font-size: 18px;
            font-weight: bold;
        }
    """)
    layout.addWidget(inputLabel)
    layout.addWidget(self.inputText)
    
    self.inputText.setStyleSheet("""
      QTextEdit {
        background-color: #f4f4f4;
        color: #333333;
        font-size: 24px;
        padding: 10px;
        border: 1px solid #d9d9d9;
        border-radius: 5px;
      }
    """)
    
    # language selection
    self.languageComboBox = QComboBox(self)
    self.languageComboBox.addItems(["en", "es", "fr", "de", "it"])  
    languageLabel = QLabel("Select Language:")
    languageLabel.setStyleSheet("""
        QLabel {
            color: #f4f4f4;
            font-size: 14px;
            font-weight: semi-bold;
        }
    """)
    layout.addWidget(languageLabel)
    layout.addWidget(self.languageComboBox)
    
    self.languageComboBox.setStyleSheet("""
      QComboBox {
        background-color: #f4f4f4;
        color: #333333;
        font-size: 18px;
        padding: 10px;
        border: 1px solid #d9d9d9;
        border-radius: 5px;
      }
    """)

    # button
    self.translateButton = QPushButton("Translate", self)
    self.translateButton.clicked.connect(self.translate_text)
    layout.addWidget(self.translateButton)
    
    self.translateButton.setStyleSheet("""
      QPushButton {
        background-color: rgb(17, 150, 28);
        color: #f4f4f4;
        font-size: 24px;
        font-weight: bold;
        padding: 10px;
        border: 1px solid rgb(9, 79, 15);
        border-radius: 25px;
      }
      QPushButton:hover {
        background-color: rgb(3, 46, 7);
        border-radius: 15px;
      }
    """)
    
    # Output text
    self.outputText = QTextEdit(self)
    self.outputText.setReadOnly(True)
    outputLabel = QLabel("Translated Text:")
    outputLabel.setStyleSheet("""
        QLabel {
            color: #f4f4f4;
            font-size: 18px;
            font-weight: bold;
        }
    """)
    layout.addWidget(outputLabel)
    layout.addWidget(self.outputText)
    
    self.outputText.setStyleSheet("""
      QTextEdit {
        background-color: #f4f4f4;
        color: #333333;
        font-size: 18px;
        padding: 10px;
        border: 1px solid #d9d9d9;
        border-radius: 5px;
      }
    """)


    self.setLayout(layout)
    
  def translate_text(self):
    text = self.inputText.toPlainText()
    target_language = self.languageComboBox.currentText()
    
    try:
      translated_text = GoogleTranslator(target=target_language).translate(text)
      self.outputText.setPlainText(translated_text)
    except Exception as error:
      self.outputText.setPlainText("Error in translation: " + str(error))
    
def main():
  app = QApplication(sys.argv)
  translator = Translator()
  translator.show()
  sys.exit(app.exec_())
  
if __name__ == "__main__":
  main()