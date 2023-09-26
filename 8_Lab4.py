import openpyxl
import xlrd

path = "Lab4Data.xlsx"
wb = openpyxl.load_workbook(path)
ws = wb.active
print(ws)