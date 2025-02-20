# This Python file uses the following encoding: utf-8
VERSION = "1.0.2"

import sys
import ui_form
import CheckLists

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

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
        self.ui.action.triggered.connect(self.show_about_dialog)

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
        print("starting comparing...")
        path_1 = self.ui.linePass1.text()
        path_2 = self.ui.linePass2.text()
        path_3 = self.ui.linePass3.text()

        checker_options = CheckLists.options();

        checker = self.ui.comboBox.currentText()
        if checker == "Все":
            checker = "all"

        checker_options.output_file_path = self.ui.filename_line.text() + ".xlsx"
        checker_options.sch_allow = self.ui.checkBox_2.isChecked()
        checker_options.pcb_allow = self.ui.checkBox.isChecked()
        checker_options.db_allow = self.ui.checkBox_3.isChecked()
        checker_options.find_allow = self.ui.find_row.isChecked()
        checker_options.checker_flow = self.ui.checker_flow.isChecked()
        #print(pcb_allow);

        no, yes = CheckLists.compare(path_1, path_2, path_3, checker, checker_options)

        self.ui.no_label.setText('Количество "Нет": ' + str(no))
        self.ui.yes_label.setText('Количество "Да": ' + str(yes))

        pass

    def show_about_dialog(self):
            """Показывает диалог 'О программе'"""
            QMessageBox.about(
                self,
                "О программе",
                "Название программы: CheckListsCompare    \n"
                "Версия: " + VERSION + "\n"
                "Автор: Лев Кириллов\n"
                "Год: 2025\n"
                "\n"
                "Программа для сравнения чеклистов."
            )



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
