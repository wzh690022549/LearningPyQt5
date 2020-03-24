# How to center the window
# Import the necessary library

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget


# Custom my class
class CenterForm(QMainWindow):
    # init method
    def __init__(self, parent=None):
        super(CenterForm, self).__init__(parent)
        # set window title
        self.setWindowTitle('Center Window')
        # set window size
        self.resize(400, 300)

    # Center Window
    def center(self):
        # calculate screen size
        screen = QDesktopWidget().screenGeometry()
        # calculate window size
        size = self.geometry()
        # calculate left and top distances
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        # move the window to new coordinate
        self.move(newLeft, newTop)


# Setup program entry
if __name__ == "__main__":
    # creat an application called app
    app = QApplication(sys.argv)
    # instantiate the class named main
    main = CenterForm()
    # use the show() method to display main
    main.show()
    # use the center() method to center the window
    main.center()
    # enter program mainloop
    sys.exit(app.exec_())
