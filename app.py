import sys
import os
import shutil
from src import System, Web, FileSystem
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, qApp, QHBoxLayout, QVBoxLayout, QProgressBar, \
    QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont


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
            """NBwar 플러그인을 위한 모드를 설치하는 프로그램 입니다.
            .시작하시려면 시작하기를 종료하시려면 종료하기를 눌러주세요!!
            .시작하시기 전에 마인크래프트와 런처는 종료해 주세요!
            .기존의 모드는 삭제 된다는 점 주의해 주세요""".replace("            .", ""),
            self)
        label_desc.setFont(QFont("Helvetica", pointSize=15))
        label_desc.setStyleSheet("Color: gray")
        label_os = QLabel("시스템: " + System.check_os(), self)
        label_os.setFont(QFont("Helvetica", pointSize=15))
        label_os.setStyleSheet("Color: blue")
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
        # print(vbtn.text() + " is clicked")
        vbtn.setEnabled(False)
        # 설치 과정 시작
        self.pbar.setMaximum(5)
        self.pbar.setValue(0)
        # OS 정보에 따른 minecraft 폴더 불러오기
        label_log.setText(
            '[INFO] Getting OS infomation and minecraft directory')
        dirMinecraft = FileSystem.getMinecraftDir()
        self.pbar.setValue(self.pbar.value() + 1)
        # 모드 파일 다운로드
        label_log.setText('[INFO] Downloading mods files')
        Web.webFileDownload(
            'http://nanobyte.iptime.org/download/NBwar-setup/mods.zip',
            os.path.expanduser('~') + '/mods.zip')
        self.pbar.setValue(self.pbar.value() + 1)
        # 모드 압축 풀기
        label_log.setText('[INFO] Unzipping mods files')
        FileSystem.unzip(os.path.expanduser('~') + '/mods.zip')
        self.pbar.setValue(self.pbar.value() + 1)
        # 모드를 minecraft 디렉터리에 복사
        exists = FileSystem.existMinecraftDir()
        # 마인크래프트 폴더 존재 여부
        if exists[0] == False:
            label_log.setText('[ERROR] Error: Minecraft does not exist')
            reply = QMessageBox.warning(self, 'MinecraftNotFound',
                                        '마인크래프트를 인식하지 못했습니다.\n마인크래프트를 설치하고 다시 시도해 주십쇼',
                                        QMessageBox.Yes, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                qApp.quit()
        # 모드 폴더 존재 여부
        elif exists[1] == False:
            label_log.setText('[ERROR] Error: Mods does not exist')
            reply = QMessageBox.warning(self, 'ModsNotFound', '포지를 인식하지 못했습니다.\n포지를 설치하고 다시 시도해 주십쇼',
                                        QMessageBox.Yes, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                qApp.quit()
        else:
            label_log.setText('[INFO] Copying mods...')
            FileSystem.rmrmods()
            shutil.copytree(os.path.expanduser('~') + '/mods',
                            FileSystem.getMinecraftDir() + '/mods')
            self.pbar.setValue(self.pbar.value() + 1)
            # 다운 받은 파일들 삭제
            label_log.setText('[INFO] Remove Cache')
            FileSystem.rmr(os.path.expanduser('~') + '/mods')
            os.remove(os.path.expanduser('~') + '/mods.zip')
            # 완료
            label_log.setText('[INFO] 완료되었습니다. 종료를 눌러주십시오')
            self.pbar.setValue(self.pbar.value() + 1)
            reply = QMessageBox.warning(self, 'Done', '세팅을 완료 했습니다.\n종료 하시겠습니까?',
                                        QMessageBox.Yes, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                qApp.quit()

    def btn_exit_fun(self):
        return QCoreApplication.instance().quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    app.exec_()
