import os
import sys
import socket
import threading
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QIcon
from datetime import datetime

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nickname = ""
target_user = None

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diskort Giriş")
        self.setWindowIcon(QIcon("login.ico"))
        self.setGeometry(100, 100, 350, 200)
        self.center()

        # Kullanıcı adı alma alanı
        self.nickname_input = QtWidgets.QLineEdit(self)
        self.nickname_input.setPlaceholderText("Takma adınızı girin...")
        self.nickname_input.setStyleSheet("""
            QLineEdit {
                padding: 2px;
                font-size: 14px;
                border: 2px solid #4CAF50;
                border-radius: 5px;
            }
        """)

        # Giriş butonu
        self.login_button = QtWidgets.QPushButton("Giriş", self)
        self.login_button.clicked.connect(self.login)
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                border: none;
                border-radius: 5px;
                padding: 5px 20px;
                font-size: 14px;                        
                                        
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        # Bileşenlerin boyutlandırılması
        self.layout_components()

    def center(self):
        """Pencereyi ekranın ortasına yerleştir."""
        frame = self.frameGeometry()
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center_point)
        self.move(frame.topLeft())

    def layout_components(self):
        """Bileşenlerin boyut ve konumlarını ayarla."""
        width = self.size().width()
        height = self.size().height()

        self.nickname_input.setGeometry(50, 80, 250, 30)
        self.login_button.setGeometry(50, 150, 240, 30)

    def resizeEvent(self, event):
        """Pencere boyutu değiştiğinde bileşenlerin boyutunu ayarla."""
        self.layout_components()

    def login(self):
        global nickname
        nickname = self.nickname_input.text()
        if nickname:
            self.close()
            self.chat_window = ChatWindow()
            receive_thread = threading.Thread(target=receive_messages, args=(self.chat_window,))
            receive_thread.start()
            self.chat_window.message_input.setFocus()
            self.chat_window.show()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.login()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class ChatWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        global nickname
        screen = QDesktopWidget().screenGeometry()
        window_width = int(screen.width() / 2)
        window_height = int(screen.height() / 2)

        # Pencere ayarları
        self.setWindowTitle("Diskort")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(100, 100, window_width, window_height)
        self.center()

        # Sohbet başlığı etiketi
        self.chat_label = QtWidgets.QLabel("Sohbet", self)
        self.chat_label.setAlignment(QtCore.Qt.AlignCenter)

        # Sohbet Alanı
        self.chat_area = QtWidgets.QTextEdit(self)
        self.chat_area.setReadOnly(True)
        self.chat_area.setStyleSheet("background-color: #F0F0F0; padding: 10px; font-size: 14px;")

        # Online kullanıcı başlığı etiketi
        self.user_label = QtWidgets.QLabel("Online Kullanıcılar", self)
        self.user_label.setAlignment(QtCore.Qt.AlignCenter)

        # Kullanıcı Listesi
        self.user_list = QtWidgets.QListWidget(self)
        self.user_list.setStyleSheet("background-color: #E8E8E8; padding: 10px; font-size: 12px;")
        self.user_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.user_list.customContextMenuRequested.connect(self.show_context_menu)

        # Mesaj yazma alanı
        self.message_input = QtWidgets.QLineEdit(self)
        self.message_input.setPlaceholderText("Mesajınızı yazın...")
        self.message_input.setStyleSheet("background-color: #FFFFFF; padding: 5px; font-size: 14px;")

        # Gönder butonu
        self.send_button = QtWidgets.QPushButton("Gönder", self)
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;")

        # Mesaj durumu etiketi
        self.message_label = QtWidgets.QLabel("", self)

        # Bileşenlerin boyutlandırılması
        self.layout_components(window_width, window_height)

    def center(self):
        """Pencereyi ekranın ortasına yerleştir."""
        frame = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center_point)
        self.move(frame.topLeft())

    def layout_components(self, width, height):
        """Bileşenlerin boyut ve konumlarını ayarla."""
        self.chat_label.setGeometry(10, 0, width - 220, 20)
        self.chat_area.setGeometry(10, 30, width - 220, height - 180)
        self.user_label.setGeometry(width - 210, 0, 200, 20)
        self.user_list.setGeometry(width - 210, 30, 200, height - 180)
        self.message_label.setGeometry(10, height - 140, width - 220, 20)
        self.message_input.setGeometry(10, height - 110, width - 240, 30)
        self.send_button.setGeometry(width - 160, height - 110, 100, 30)

    def resizeEvent(self, event):
        """Pencere boyutu değiştiğinde bileşenlerin boyutunu ayarla."""
        width = event.size().width()
        height = event.size().height()
        self.layout_components(width, height)

    def show_context_menu(self,pos):
        menu = QtWidgets.QMenu(self)
        menu.setStyleSheet("QMenu {background-color: #333; color: white;}")
        private_msg_action = menu.addAction("Özel Mesaj Gönder")
        view_profile_action = menu.addAction("Kullanıcı Profilini Görüntüle")
        action = menu.exec_(self.user_list.mapToGlobal(pos))
        if action==private_msg_action:
            self.set_private_message_target()
        elif action==view_profile_action:
            self.view_user_profile()

    def view_user_profile(self):
        selected_user = self.user_list.currentItem()
        if selected_user:
            user_profile = f'Kullanıcı: {selected_user.text()}\n'
            QtWidgets.QMessageBox.information(self,"Kullanıcı Profili",user_profile)

    def clear_target(self):
        global target_user
        target_user = None
        self.message_label.setText("")
        self.clear_target_button.hide()

    def set_private_message_target(self):
        global target_user
        selected_user = self.user_list.currentItem()
        if selected_user:
            target_user = selected_user.text()
            if target_user == nickname:
                QtWidgets.QMessageBox.warning(self,"Hata","Kendinize mesaj gönderemezsiniz.")
                target_user=None
                return
            else:
                self.message_label.setText(f"{target_user} adlı kişiye özel mesaj gönderiyorsunuz.")
                self.clear_target_button.show()

    def update_user_list(self,message):
        users = message.split(":")[1].split(",")
        self.user_list.clear()
        self.user_list.addItems(users)

    def receive_message(self,message):
        if message.startswith('USER_LIST'):
            self.update_user_list(message)
        elif message.startswith('PRIVATE'):
            parts = message.split(":")
            target_user = parts[1]
            private_message = ":".join(parts[2:])
            if target_user == nickname:
                self.chat_area.append(f"<span style='color:red;'>Özel Mesaj: </span> {private_message}")
        else:
            self.chat_area.append(message)

    def closeEvent(self, event):
        client.close()
        event.accept()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.send_message()

    def send_message(self):
        global target_user
        message = self.message_input.text()
        if message.strip():
            timestamp = datetime.now().strftime('%H:%M:%S')
            if target_user:
                full_message = f"<span style='color:gray;'>[{timestamp}]</span> [Özel] <span style='color:blue;'>{nickname}</span> -> {target_user}: {message}"
                client.send(f'PRIVATE:{target_user}:{full_message}'.encode('utf-8'))
                self.chat_area.append(f"<span style='color:blue;'>[{target_user}]</span> : {message}")
            else:
                full_message = f"<span style='color:gray;'>[{timestamp}]</span> <span style='color:blue;'>{nickname}:</span> {message}"
                self.chat_area.append(full_message)
                client.send(full_message.encode('utf-8'))
            self.message_input.clear()

def receive_messages(chat_window):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message=='NICK':
                client.send(nickname.encode('utf-8'))
            else:
                messages = message.split("!")
                for msg in messages:
                    if msg:
                        chat_window.receive_message(msg)
        except:
            print("Sunucuyla bağlantı koptu!")
            client.close()
            break

def main():
    try:
        client.connect(('localhost',54321))
    except:
        print("Sunucuya bağlanılmadı!")
        sys.exit()

    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

main()