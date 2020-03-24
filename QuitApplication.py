# How to quit the application
# Import the necessary library

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QPushButton


# Custom my own class
class QuitApplication(QMainWindow):
    def __init__(self, parent=None):
        super(QuitApplication, self).__init__(parent)
        # set window title
        self.setWindowTitle("Quit Application")
        # set window size
        self.resize(300, 120)

        # add a Button
        self.button1 = QPushButton('Quit Application')
        # associate signal with slot
        self.button1.clicked.connect(self.onClickButton)

        # create horizontal layout
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        # create root widget
        mainFrame = QWidget()
        # use the horizontal layout
        mainFrame.setLayout(layout)

        # put the root widget on the window
        self.setCentralWidget(mainFrame)

    # onClickButton method
    def onClickButton(self):
        # get the sender
        sender = self.sender()
        print(sender.text() + ' Button has been Clicked')
        # get the application's instance
        app = QApplication.instance()
        # use quit() method to quit application
        app.quit()


# setup program entry
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())
