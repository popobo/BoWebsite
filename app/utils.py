import os
import openpyxl
from datetime import datetime

def create_excel_file(menu, month):
    # Create a workbook and add a worksheet
    wb = openpyxl.Workbook()
    ws = wb.active

    # Write the menu data to the worksheet
    menu_data = menu.split('\n')
    for row, line in enumerate(menu_data, start=1):
        ws.cell(row=row, column=1, value=line)

    # Save the workbook to a file
    filename = f'menu_{month}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
    file_path = os.path.join('app', 'generated_files', filename)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    wb.save(file_path)

    return filename
