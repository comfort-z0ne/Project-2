from PySide6.QtWidgets import QMainWindow
from csv import DictReader
from window import Ui_MainWindow

class mainWindow(Ui_MainWindow):
    def __init__(self):
        # Init the window using the Ui_MainWindow class inherited from window.py
        self.main_window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)

        # Read the recent TV settings from the settings.csv file and store them in a list of dictionaries
        with open("settings.csv", 'r') as file:
            lines = DictReader(file)
            self.settings = list(lines)[0]

        self.setupSettings()
        self.setupButtons()

    def setupSettings(self):
        if self.settings["Power"] == "On":
            self.ui.lcdNumber.display(self.settings["Channel"])
            self.ui.channelWidget.setCurrentIndex(int(self.settings["Channel"]))
        else:
            self.ui.channelWidget.setCurrentWidget(self.ui.off)
        if self.settings["Muted"] == "True":
            self.ui.label_muted.setText("Muted")
            self.ui.volumeBar.setValue(0)
        else:
            self.ui.label_muted.setText("")
            self.ui.volumeBar.setValue(int(self.settings["Volume"]))
        self.ui.label_error.setText("")
        self.ui.guideWidget.setCurrentWidget(self.ui.hidden)

    def setupButtons(self):
        # Connect the buttons to their respective functions
        self.ui.pushButton_power.clicked.connect(lambda: self.togglePower())

        self.ui.pushButton_zero.clicked.connect(lambda: self.addText("0"))
        self.ui.pushButton_one.clicked.connect(lambda: self.addText("1"))
        self.ui.pushButton_two.clicked.connect(lambda: self.addText("2"))
        self.ui.pushButton_three.clicked.connect(lambda: self.addText("3"))
        self.ui.pushButton_four.clicked.connect(lambda: self.addText("4"))
        self.ui.pushButton_five.clicked.connect(lambda: self.addText("5"))
        self.ui.pushButton_six.clicked.connect(lambda: self.addText("6"))
        self.ui.pushButton_seven.clicked.connect(lambda: self.addText("7"))
        self.ui.pushButton_eight.clicked.connect(lambda: self.addText("8"))
        self.ui.pushButton_nine.clicked.connect(lambda: self.addText("9"))
        self.ui.pushButton_backspace.clicked.connect(lambda: self.subText())
        self.ui.pushButton_confirm.clicked.connect(lambda: self.confirm())

        self.ui.pushButton_volUp.clicked.connect(lambda: self.volumeUp())
        self.ui.pushButton_volDown.clicked.connect(lambda: self.volumeDown())
        self.ui.pushButton_mute.clicked.connect(lambda: self.toggleMute())

        self.ui.pushButton_chUp.clicked.connect(lambda: self.channelUp())
        self.ui.pushButton_chDown.clicked.connect(lambda: self.channelDown())
        self.ui.pushButton_guide.clicked.connect(lambda: self.toggleGuide())

    def togglePower(self):
        # Toggle the power state of the TV and show the appropriate screen
        if self.settings["Power"] == "On":
            self.settings["Power"] = "Off"
            self.ui.channelWidget.setCurrentWidget(self.ui.off)
        else:
            self.settings["Power"] = "On"
            self.ui.channelWidget.setCurrentIndex(int(self.settings["Channel"]))
        self.ui.label_error.setText("")
        self.updateSettings()

    def addText(self, text):
        # Add text to the line edit field
        current_text = str(self.ui.inputLine.text())
        new_text = current_text + text
        self.ui.inputLine.setText(new_text)
    def subText(self):
        # Delete one character from the text in the line edit field
        current_text = str(self.ui.inputLine.text())
        new_text = current_text[:-1]
        self.ui.inputLine.setText(new_text)
    def confirm(self):
        # See if input matched any of the accounts in the accounts.csv file
        input_text = int(self.ui.inputLine.text())
        if input_text in range(1, 6) and self.settings["Power"] == "On":
            self.settings["Channel"] = str(input_text)
            self.ui.lcdNumber.display(input_text)
            self.ui.label_error.setText("")
            self.ui.channelWidget.setCurrentIndex(input_text)
        else:
            if self.settings["Power"] == "Off":
                self.ui.label_error.setText("The TV is off.")
            else:
                self.ui.label_error.setText("Invalid channel #.")
        self.updateSettings()

    def volumeUp(self):
        # Increase the volume by 1, up to a maximum of 10
        if int(self.settings["Volume"]) < 10 and self.settings["Muted"] == "False" and self.settings["Power"] == "On":
            self.settings["Volume"] = str(int(self.settings["Volume"]) + 1)
            self.ui.volumeBar.setValue(int(self.settings["Volume"]))
        elif self.settings["Power"] == "Off":
            self.ui.label_error.setText("The TV is off.")
        self.updateSettings()
    def volumeDown(self):
        # Decrease the volume by 1, down to a minimum of 0
        if int(self.settings["Volume"]) > 0 and self.settings["Muted"] == "False" and self.settings["Power"] == "On":
            self.settings["Volume"] = str(int(self.settings["Volume"]) - 1)
            self.ui.volumeBar.setValue(int(self.settings["Volume"]))
        elif self.settings["Power"] == "Off":
            self.ui.label_error.setText("The TV is off.")
        self.updateSettings()

    def toggleMute(self):
        # Toggle the mute state of the TV
        if self.settings["Muted"] == "False" and self.settings["Power"] == "On":
            self.settings["Muted"] = "True"
            self.ui.label_muted.setText("Muted")
            self.ui.volumeBar.setValue(0)
        elif self.settings["Muted"] == "True" and self.settings["Power"] == "On":
            self.settings["Muted"] = "False"
            self.ui.label_muted.setText("")
            self.ui.volumeBar.setValue(int(self.settings["Volume"]))
        elif self.settings["Power"] == "Off":
            self.ui.label_error.setText("The TV is off.")
        self.updateSettings()

    def channelUp(self):
        # Increase the channel by 1, up to a maximum of 5
        if int(self.settings["Channel"]) < 5 and self.settings["Power"] == "On":
            self.settings["Channel"] = str(int(self.settings["Channel"]) + 1)
            self.ui.lcdNumber.display(int(self.settings["Channel"]))
            self.ui.channelWidget.setCurrentIndex(int(self.settings["Channel"]))
        elif self.settings["Power"] == "Off":
            self.ui.label_error.setText("The TV is off.")
        self.updateSettings()
    def channelDown(self):
        # Decrease the channel by 1, down to a minimum of 1
        if int(self.settings["Channel"]) > 1 and self.settings["Power"] == "On":
            self.settings["Channel"] = str(int(self.settings["Channel"]) - 1)
            self.ui.lcdNumber.display(int(self.settings["Channel"]))
            self.ui.channelWidget.setCurrentIndex(int(self.settings["Channel"]))
        elif self.settings["Power"] == "Off":
            self.ui.label_error.setText("The TV is off.")
        self.updateSettings()
    
    def toggleGuide(self):
        # Toggle the guide screen on and off
        if self.ui.guideWidget.currentWidget() == self.ui.visible and self.settings["Power"] == "On":
            self.ui.guideWidget.setCurrentWidget(self.ui.hidden)
        elif self.settings["Power"] == "On":
            self.ui.guideWidget.setCurrentWidget(self.ui.visible)
        else:
            self.ui.label_error.setText("The TV is off.")

    def updateSettings(self):
        # Update the settings.csv file with the current settings
        with open("settings.csv", 'w') as file:
            file.write("Power,Channel,Volume,Muted\n")
            file.write(f"{self.settings['Power']},{self.settings['Channel']},{self.settings['Volume']},{self.settings['Muted']}")

    # Show the window (called initially in main.py)
    def show(self):
        self.main_window.show()