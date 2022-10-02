from PyQt5.QtWidgets import QApplication, QMainWindow
import ui_main, sys, requests, pyperclip


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = ui_main.Ui_MainWindow()
        self.main.setupUi(self)
        self.main.generateButton.clicked.connect(lambda: self.generateFakeName())
        self.generateFakeName()

    def generateFakeName(self):
        data = requests.get("https://api.namefake.com/english-united-states/male")
        fakeName = data.json()
        self.main.fakeNameOutput.setText(fakeName["name"])
        self.main.fakeNameOutput.selectAll()
        pyperclip.copy(fakeName["name"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
