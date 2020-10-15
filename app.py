import sys
import os
import shutil
import platform
from src import System, Web, FileSystem
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QToolTip, QAction, QMainWindow, qApp, QHBoxLayout, QVBoxLayout, QProgressBar
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont


class MyApp(QWidget):
    def __init__(self):
        # 국룰
        super().__init__()

        # UI 호출
        self.UIinit()

    def UIinit(self):
        # 각 요소들 호출

        # 창 제목
        self.setWindowTitle("NBwar Setup")

        # 창 크기
        self.resize(800, 600)

        # 메뉴바
        # exitAction = QAction('Exit', self)
        # exitAction.setShortcut('Ctrl+Q')
        # exitAction.setStatusTip('Exit application')
        # exitAction.triggered.connect(qApp.quit)

        # menubar = self.menuBar()
        # menubar.setNativeMenuBar(False)
        # Filemenu1 = menubar.addMenu("File")
        # # Filemenu2 = menubar.addMenu("Edit")
        # # Filemenu3 = menubar.addMenu("Prop")
        # Filemenu1.addAction(exitAction)

        # 레이블
        label_title = QLabel("NBwar Setup 에 오신걸 환영합니다.", self)
        label_title.setFont(QFont("Helvetica", pointSize=30))
        # font_title = label_title.font()
        # font_title.setPointSize(20)
        # font_title.setBold(True)
        # label_title.setFont(font_title)
        # label_title.move(10, 20)
        label_desc = QLabel(
            "NBwar 플러그인을 위한 모드를 설치하는 프로그램 입니다.\n시작하시려면 시작하기를 종료하시려면 종료하기를 눌러주세요!!", self)
        label_desc.setFont(QFont("Helvetica", pointSize=15))
        label_os = QLabel("시스템: "+System.check_os(), self)
        label_os.setFont(QFont("Helvetica", pointSize=15))
        label_log = QLabel("", self)
        label_log.setFont(QFont("Helvetica", pointSize=15))

        # 버튼
        btn_start = QPushButton('시작하기', self)
        btn_start.pressed.connect(
            lambda: self.btn_start_fun(btn_start, label_log))
        # btn_start.move(10, 50)

        btn_exit = QPushButton("종료하기", self)
        btn_exit.pressed.connect(self.btn_exit_fun)
        # btn_exit.move(10, 80)

        # 진행바
        self.pbar = QProgressBar(self)
        # self.pbar.setGeometry(30, 40, 200, 25)
        self.pbar.setMinimum(0)
        # self.pbar.setMaximum(0)

        # 레이아웃 구성
        wid = QWidget(self)
        vbox_main = QVBoxLayout()
        hbox_mainButtons = QHBoxLayout()

        vbox_main.addWidget(label_title)
        vbox_main.addWidget(label_desc)
        vbox_main.addWidget(label_os)
        vbox_main.addWidget(label_log)
        vbox_main.addWidget(self.pbar)
        vbox_main.addLayout(hbox_mainButtons)

        hbox_mainButtons.addWidget(btn_start)
        hbox_mainButtons.addWidget(btn_exit)
        self.setLayout(vbox_main)

        # 실행
        self.show()

    def btn_start_fun(self, vbtn, label_log):
        print(vbtn.text() + " is clicked")
        self.pbar.setMaximum(4)
        self.pbar.setValue(0)
        label_log.setText(
            '[INFO] Getting OS infomation and minecraft directory')
        dirMinecraft = FileSystem.getMinecraftDir()
        self.pbar.setValue(self.pbar.value() + 1)
        label_log.setText('[INFO] Downloading mods files')
        Web.webFileDownload(
            'http://nanobyte.iptime.org/download/NBwar-setup/mods.zip', os.path.expanduser('~')+'/mods.zip')
        self.pbar.setValue(self.pbar.value() + 1)
        label_log.setText('[INFO] Unzipping mods files')
        FileSystem.unzip(os.path.expanduser('~')+'/mods.zip')
        self.pbar.setValue(self.pbar.value() + 1)
        label_log.setText('[INFO] Copying mods...')
        FileSystem.rmrmods()
        shutil.copytree(os.path.expanduser('~')+'/mods',
                        FileSystem.getMinecraftDir()+'/mods')
        label_log.setText('[INFO] 완료되었습니다. 종료를 눌러주십시오')
        self.pbar.setValue(self.pbar.value() + 1)

    def btn_exit_fun(self):
        return QCoreApplication.instance().quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    app.exec_()
