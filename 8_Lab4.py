import openpyxl
import xlrd

path = "Lab4Data.xlsx"
wb = openpyxl.Workbook(path)
ws = wb.active
print(ws)