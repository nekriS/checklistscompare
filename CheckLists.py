# -*- coding: utf-8 -*-
import openpyxl



def read_cell_range(sheet, start_row, end_row, start_col, end_col):
    """
    Считывает данные из указанного диапазона ячеек на листе Excel.

    :param sheet: Объект листа (openpyxl worksheet)
    :param start_row: Начальная строка (целое число)
    :param end_row: Конечная строка (целое число)
    :param start_col: Начальный столбец (целое число, A=1, B=2, ...)
    :param end_col: Конечный столбец (целое число)
    :return: Двумерный массив (список списков) с данными из ячеек
    """
    data = []
    for row in range(start_row, end_row + 1):
        row_data = []
        for col in range(start_col, end_col + 1):
            cell_value = sheet.cell(row=row, column=col).value
            row_data.append(cell_value)
        data.append(row_data)
    return data

def mas_no_mas(massive):
    out_massive = []
    for el in massive:
        if el[0] != None:
            out_massive.append(el[0])
    return out_massive


def findrow(sheet, number, start_row, end_row):
    row = -1
    for row in range(start_row, end_row):
        if sheet.cell(row=row, column=3).value == number:
            return row
    return row

def compare(path_1, path_2, path_3, checker, output_file_path, sch_allow, db_allow, pcb_allow, find_allow):

    no = 0
    yes = 0

    workbook = openpyxl.load_workbook(path_1)
    workbook_middle = openpyxl.load_workbook(path_2)
    workbook_end = openpyxl.load_workbook(path_3)

    sheet_names = workbook.sheetnames

    main_sheet = workbook.worksheets[0]

    PNs = mas_no_mas(read_cell_range(main_sheet, 8, 50, 2, 2))
    CHs = mas_no_mas(read_cell_range(main_sheet, 8, 50, 6, 6))

    # определяем компоненты которые нужно проверить по параметру "кто проверяет"
    if checker != "all":
        for ch_n in reversed(range(len(CHs))):
            if CHs[ch_n] != checker:
                PNs.pop(ch_n)

    #print(PNs)
    #print(CHs)

    for sheet_name in sheet_names:
        if (" DB" in sheet_name) and db_allow:
            #print(sheet_name)
            sheet = workbook[sheet_name]  # Получение объекта листа по имени
            sheet_middle = workbook_middle[sheet_name]

            try:
                sheet_end = workbook_end[sheet_name]  # Получение объекта листа по имени
            except:
                print("Листа " + sheet_name + " не обнаружено!")
                continue

            part_number = sheet["B1"].value

            if part_number in PNs:

                #data = read_cell_range(sheet, 8, 54, 1, 4)
                sheet_end.cell(row=7, column=5).value = "1. Значение"
                sheet_end.cell(row=7, column=6).value = "2. Комментарий"

                for row in range(8, 60):

                    cell_value = sheet.cell(row=row, column=1).value

                    if cell_value != None:

                        if cell_value == "Да":
                            value_first = sheet.cell(row=row, column=4).value
                            value_end = sheet_end.cell(row=row, column=4).value
                            if value_first == value_end:
                                sheet_end.cell(row=row, column=1).value = "Да"
                            else:
                                sheet_end.cell(row=row, column=1).value = "Нет"
                                sheet_end.cell(row=row, column=5).value = sheet.cell(row=row, column=4).value
                                sheet_end.cell(row=row, column=6).value = sheet_middle.cell(row=row, column=2).value
                        elif cell_value == "Нет":
                            value_first = sheet.cell(row=row, column=4).value
                            value_end = sheet_end.cell(row=row, column=4).value
                            if value_first == value_end:
                                sheet_end.cell(row=row, column=1).value = "Нет"
                                sheet_end.cell(row=row, column=5).value = sheet.cell(row=row, column=4).value
                                sheet_end.cell(row=row, column=6).value = sheet_middle.cell(row=row, column=2).value
                            else:
                                #sheet_end.cell(row=row, column=1).value = "Не проверено"
                                sheet_end.cell(row=row, column=5).value = sheet.cell(row=row, column=4).value
                                sheet_end.cell(row=row, column=6).value = sheet_middle.cell(row=row, column=2).value


        if (" Sch" in sheet_name) and sch_allow:
            #print(sheet_name)
            sheet = workbook[sheet_name]  # Получение объекта листа по имени
            sheet_middle = workbook_middle[sheet_name]

            try:
                sheet_end = workbook_end[sheet_name]  # Получение объекта листа по имени
            except:
                print("Листа " + sheet_name + " не обнаружено!")
                continue

            part_number = sheet["B1"].value

            if part_number in PNs:

                # проверка шапки
                sheet_end.cell(row=7, column=5).value = "1. Значение"
                sheet_end.cell(row=7, column=6).value = "1. Комментарий"
                for row in range(8, 12):

                    cell_value = sheet.cell(row=row, column=1).value

                    if cell_value != None:
                        if cell_value == "Да":
                            value_first = sheet.cell(row=row, column=4).value
                            value_end = sheet_end.cell(row=row, column=4).value
                            if value_first == value_end:
                                sheet_end.cell(row=row, column=1).value = "Да"
                            else:
                                sheet_end.cell(row=row, column=1).value = "Нет"
                                sheet_end.cell(row=row, column=5).value = sheet.cell(row=row, column=4).value

                                if "Проверяется соответствие " in sheet.cell(row=row, column=2).value:
                                    sheet_end.cell(row=row, column=6).value = sheet.cell(row=row, column=5).value
                                else:
                                    sheet_end.cell(row=row, column=6).value = str(sheet.cell(row=row, column=2).value) + " " + str(sheet.cell(row=row, column=5).value)

                        elif cell_value == "Нет":
                            value_first = sheet.cell(row=row, column=4).value
                            value_end = sheet_end.cell(row=row, column=4).value
                            if value_first == value_end:
                                sheet_end.cell(row=row, column=1).value = "Нет"
                                sheet_end.cell(row=row, column=5).value = sheet.cell(row=row, column=4).value

                                if "Проверяется соответствие " in sheet.cell(row=row, column=2).value:
                                    sheet_end.cell(row=row, column=6).value = sheet.cell(row=row, column=5).value
                                else:
                                    sheet_end.cell(row=row, column=6).value = str(sheet.cell(row=row, column=2).value) + " " + str(sheet.cell(row=row, column=5).value)

                            else:
                                sheet_end.cell(row=row, column=1).value = "Не проверено"
                                sheet_end.cell(row=row, column=5).value = sheet.cell(row=row, column=4).value

                                if "Проверяется соответствие " in sheet.cell(row=row, column=2).value:
                                    sheet_end.cell(row=row, column=6).value = sheet.cell(row=row, column=5).value
                                else:
                                    sheet_end.cell(row=row, column=6).value = str(sheet.cell(row=row, column=2).value) + " " + str(sheet.cell(row=row, column=5).value)



                # проверка распиновки, максимум 500 строк
                max_strings = 500
                sheet_end.cell(row=16, column=7).value = "1. Name"
                sheet_end.cell(row=16, column=8).value = "1. Type"
                sheet_end.cell(row=16, column=9).value = "2. Комментарий"

                for row in range(17, max_strings):

                    cell_value = sheet.cell(row=row, column=1).value

                    if cell_value != None:

                        if find_allow:
                            row_3 = findrow(sheet_end, sheet.cell(row=row, column=3).value, 17, max_strings)
                        else:
                            row_3 = row
                        #print(row);
                        #print(row_3);
                        if cell_value == "Да":
                            value_name_first = sheet.cell(row=row, column=4).value
                            value_name_end = sheet_end.cell(row=row_3, column=4).value

                            value_type_first = sheet.cell(row=row, column=5).value
                            value_type_end = sheet_end.cell(row=row_3, column=5).value

                            if (value_name_first == value_name_end) and (value_type_first == value_type_end):
                                sheet_end.cell(row=row_3, column=1).value = "Да"
                                yes += 1
                            else:
                                sheet_end.cell(row=row_3, column=1).value = "Нет"
                                sheet_end.cell(row=row_3, column=7).value = sheet.cell(row=row, column=4).value
                                sheet_end.cell(row=row_3, column=8).value = sheet_middle.cell(row=row, column=5).value
                                sheet_end.cell(row=row_3, column=9).value = sheet_middle.cell(row=row, column=2).value
                                no += 1
                        elif cell_value == "Нет":
                            value_name_first = sheet.cell(row=row, column=4).value
                            value_name_end = sheet_end.cell(row=row_3, column=4).value

                            value_type_first = sheet.cell(row=row, column=5).value
                            value_type_end = sheet_end.cell(row=row_3, column=5).value

                            if (value_name_first == value_name_end) and (value_type_first == value_type_end):
                                sheet_end.cell(row=row_3, column=1).value = "Нет"
                                sheet_end.cell(row=row_3, column=7).value = sheet.cell(row=row, column=4).value
                                sheet_end.cell(row=row_3, column=8).value = sheet_middle.cell(row=row, column=5).value
                                sheet_end.cell(row=row_3, column=9).value = sheet_middle.cell(row=row, column=2).value
                                no += 1
                            else:
                                #sheet_end.cell(row=row, column=1).value = "Не проверено"
                                sheet_end.cell(row=row_3, column=7).value = sheet.cell(row=row, column=4).value
                                sheet_end.cell(row=row_3, column=8).value = sheet_middle.cell(row=row, column=5).value
                                sheet_end.cell(row=row_3, column=9).value = sheet_middle.cell(row=row, column=2).value

    #output_file_path = 'example_updated.xlsx'
    workbook_end.save(output_file_path)

    return [no, yes]

if __name__ == "__main__":

    path_1 = ""
    path_2 = ""
    path_3 = ""

    checker = ""

    compare(path_1, path_2, path_3, checker, 'example_updated.xlsx', True, True, False, False)
