import openpyxl
import xlrd

path = "Lab4Data.xlsx"
wb = openpyxl.load_workbook(path, read_only=False)
worksheet_names = wb.sheetnames
print(worksheet_names)
sheet_index = worksheet_names.index('Table 9 ')
wb.active = sheet_index
ws = wb.active
print(ws)