# == IMPORTATIONS == #

try:
    #- Librairies
    from PyQt5.QtWidgets import QMainWindow, QApplication
    import sys 

    #- Files
    #from .controllers.get_text import get_text
except Exception as e:
    raise e


class Root(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.title = 'test'
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.initWindow()

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

App = QApplication(sys.argv)
window = Root()
sys.exit(App.exec())