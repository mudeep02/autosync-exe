import sys
import os
import shutil
import psutil
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLabel, QListWidget, QMessageBox
)

class DriveSyncApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drive Sync Utility")
        self.setGeometry(100, 100, 500, 400)
        self.layout = QVBoxLayout()
        
        self.label = QLabel("Connected Removable Drives:")
        self.layout.addWidget(self.label)
        
        self.driveList = QListWidget()
        self.layout.addWidget(self.driveList)

        self.fileList = QListWidget()
        self.layout.addWidget(self.fileList)

        self.syncButton = QPushButton("Sync")
        self.syncButton.clicked.connect(self.sync_data)
        self.layout.addWidget(self.syncButton)

        self.setLayout(self.layout)
        self.detect_removable_drives()

        self.driveList.currentItemChanged.connect(self.show_drive_files)

    def detect_removable_drives(self):
        self.removable_drives = []
        partitions = psutil.disk_partitions()
        for p in partitions:
            if 'removable' in p.opts or 'cdrom' in p.opts or 'rw' in p.opts:
                self.removable_drives.append(p.device)
                self.driveList.addItem(p.device)

    def show_drive_files(self):
        self.fileList.clear()
        selected_drive = self.driveList.currentItem()
        if selected_drive:
            root = selected_drive.text()
            try:
                for root_dir, dirs, files in os.walk(root):
                    for file in files:
                        full_path = os.path.join(root_dir, file)
                        self.fileList.addItem(full_path)
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))

    def sync_data(self):
        selected_drive = self.driveList.currentItem()
        if not selected_drive:
            QMessageBox.warning(self, "Warning", "No drive selected.")
            return
        
        source = selected_drive.text()
        target = os.path.join(os.getcwd(), "SyncedFiles")
        os.makedirs(target, exist_ok=True)

        try:
            for root_dir, dirs, files in os.walk(source):
                for file in files:
                    src_file = os.path.join(root_dir, file)
                    relative_path = os.path.relpath(root_dir, source)
                    target_dir = os.path.join(target, relative_path)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.copy2(src_file, os.path.join(target_dir, file))
            QMessageBox.information(self, "Success", "Data synced successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DriveSyncApp()
    window.show()
    sys.exit(app.exec_())
