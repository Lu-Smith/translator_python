import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

class Translator(QWidget):
  def __init__(self):
    super().__init__()

def main():
  app = QApplication(sys.argv)
  translator = Translator()
  translator.show()
  sys.exit(app.exec_())
  
if __name__ == "__main__":
  main()