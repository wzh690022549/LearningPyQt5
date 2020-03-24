# This is my first QMainWindow
# Import the necessary library

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


# Custom my class
class FirstMainWin(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWin, self).__init__(parent)
        # set window title
        self.setWindowTitle('My first MainWindow application')
        # set window size
        self.resize(400, 300)
        # set statusBar message
        self.status = self.statusBar()
        self.status.showMessage('This message only exits for 5 seconds', 5000)


# Setup program entry
if __name__ == "__main__":
    # creat an application called app
    app = QApplication(sys.argv)
    # instantiate the class named main
    main = FirstMainWin()
    # use the show() method to display main
    main.show()
    # enter program mainloop
    sys.exit(app.exec_())
