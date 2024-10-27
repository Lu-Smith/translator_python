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
    self.setGeometry(100, 100, 400, 300)
    
    # layout
    layout = QVBoxLayout()
    
    # input
    self.inputText = QTextEdit(self)
    self.inputText.setPlaceholderText("Enter text to translate...")
    layout.addWidget(QLabel("Input Text:"))
    layout.addWidget(self.inputText)
    
    # language selection
    self.languageComboBox = QComboBox(self)
    self.languageComboBox.addItems(["en", "es", "fr", "de", "it"])  
    layout.addWidget(QLabel("Select Language:"))
    layout.addWidget(self.languageComboBox)
    
    # button
    self.translateButton = QPushButton("Translate", self)
    self.translateButton.clicked.connect(self.translate_text)
    layout.addWidget(self.translateButton)
    
    # Output text
    self.outputText = QTextEdit(self)
    self.outputText.setReadOnly(True)
    layout.addWidget(QLabel("Translated Text:"))
    layout.addWidget(self.outputText)


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