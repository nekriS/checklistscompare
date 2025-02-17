# This Python file uses the following encoding: utf-8
VERSION = "1.0.0"

import sys
import ui_form
import CheckLists

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

from pathlib import Path
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.pushButton_clicked)
        self.ui.pushButton_2.clicked.connect(self.pushButton_2_clicked)
        self.ui.pushButton_3.clicked.connect(self.pushButton_3_clicked)

        self.ui.Compare.clicked.connect(self.compare_function)

        self.setWindowTitle("CheckListCompare " + VERSION)

    def get_time_modification(self, file_path_str):
        file_path = Path(file_path_str)
        modification_time = file_path.stat().st_mtime
        modification_date = datetime.fromtimestamp(modification_time)
        return modification_date.strftime("%Y-%m-%d %H:%M:%S")

    def pushButton_clicked(self):
        file_path = self.open_file_dialog()
        temp_time = self.get_time_modification(file_path);
        self.ui.linePass1.setText(f"{file_path}")
        self.ui.datePass1.setText(f"{temp_time}")

    def pushButton_2_clicked(self):
        file_path = self.open_file_dialog()
        temp_time = self.get_time_modification(file_path);
        self.ui.linePass2.setText(f"{file_path}")
        self.ui.datePass2.setText(f"{temp_time}")

    def pushButton_3_clicked(self):
        file_path = self.open_file_dialog()
        temp_time = self.get_time_modification(file_path);
        self.ui.linePass3.setText(f"{file_path}")
        self.ui.datePass3.setText(f"{temp_time}")

    def open_file_dialog(self):
            """Открывает диалоговое окно для выбора файла"""
            options = QFileDialog.Options()  # Опции диалогового окна
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Выберите файл",
                "",  # Начальная директория (пустая строка означает текущую директорию)
                "Все файлы (*);;Текстовые файлы (*.txt)",  # Фильтр типов файлов
                options=options
            )
            return file_path


    def compare_function(self):
        print("1")
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
