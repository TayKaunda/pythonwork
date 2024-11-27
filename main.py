#import necessary modules
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase
import pytz
from datetime import datetime

#create a constructor for the clock
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        # add timezone functionality
        self.timezone_selector = QComboBox(self)
        self.current_timezone = pytz.timezone("UTC")
        self.initUI()

          #set the dimensions of your clock
    def initUI(self):
        self.setWindowTitle("DigitalClock")
        self.setGeometry(500, 300, 200, 100)
        
        # Create vbox FIRST
        vbox = QVBoxLayout()
        
        # Add timezones selector
        self.populate_timezones()
        self.timezone_selector.currentTextChanged.connect(self.change_timezone)
        vbox.addWidget(self.timezone_selector)
        
        # Add time label
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        
        
        # Add popular timezones
    def populate_timezones(self):
        common_timezones = [
            "UTC",
            "US/Pacific",
            "US/Eastern",
            "Europe/Paris",
            "Europe/London",
            "Asia/Tokyo",
            "Australia/Sydney",
        ]
        self.timezone_selector.addItems(common_timezones)
        
    def change_timezone(self, timezone_str):
        self.current_timezone = pytz.timezone(timezone_str)
        self.update_time
        
        
        #alignment
        self.time_label.setAlignment(Qt.AlignCenter)
        
        #font
        self.time_label.setStyleSheet("font-size: 160px;" "color:hsl(312, 100%, 50%);")
        self.setStyleSheet("background-color:white;")
        
        # Timer setup
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        self.update_time()
        
    #format time
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        #get current timezone
        utc_time = datetime.now(pytz.UTC)
        local_time = utc_time.astimezone(self.current_timezone)
        current_time = local_time.strftime("%I:%M:%S %p")
        self.time_label.setText(current_time)
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())