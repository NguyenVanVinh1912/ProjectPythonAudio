import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QPushButton
# from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtCore import QUrl
from Danh_Sach_Nhac import Ui_MainWindow as Danh_Sach_Nhac_Ui_MainWindow
# from main import MainWindow
from main import *

class Main_List_Music_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic= Danh_Sach_Nhac_Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.tro_ve.clicked.connect(self.ve_main)

    def ve_main(self):
        # Khởi tạo QStackedWidget
        self.stacked_widget = QStackedWidget(self)
        
        # Tạo hai trang con cho QStackedWidget
        self.main_widget = Main_List_Music_MainWindow()
        # self.main_widget.setObjectName("MainWidget")
        # self.main_widget.setStyleSheet("#MainWidget { background-color: #000; }")
        self.thu_vien = QPushButton("Hãy click tôi để chuyển vào thư viện nhé !!!", self.main_widget)
        self.thu_vien.setGeometry(50, 50, 250, 50)
        self.thu_vien.clicked.connect(self.show_main)
        
        self.list_music_widget = MainWindow()
        self.stacked_widget.addWidget(self.main_widget)
        self.stacked_widget.addWidget(self.list_music_widget)
        
        self.setCentralWidget(self.stacked_widget)
        
    def show_main(self):
        self.stacked_widget.setCurrentWidget(self.list_music_widget)
    
    pygame
# Kết thúc game
pygame.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win=Main_List_Music_MainWindow()
    main_win.show()
    sys.exit(app.exec())