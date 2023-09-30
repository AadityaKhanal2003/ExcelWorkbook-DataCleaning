import openpyxl

path = "Lab4Data.xlsx"
wb = openpyxl.load_workbook(path, read_only=False)
ws = wb.worksheets[1]
countries_range = ws["B15:B211"]
clabour_range = ws["E15:E211"]
bregistration_range = ws["O15:O211"]
bregistration_range = ws["O15:O211"]
cmarraige_rangeo = ws["K15:K211"]
cmarraige_ranget = ws["L15:L211"]
# Iterate through country values
for cell in countries_range:
    country_value = cell[0].value 
    #print(country_value)

# Iterate through child labour values
for cell2 in clabour_range:
    clabour_value = cell2[0].value 
    #print(clabour_value)

# Iterate through birth registration values
for cell3 in bregistration_range:
    bregistration_value = cell3[0].value 
    #print(bregistration_value)

# Iterate through child marriage values
for cell4 in cmarraige_rangeo:
    cmarraigeo_value = cell4[0].value 
for cell5 in cmarraige_ranget:
    cmarraiget_value = cell5[0].value

print(type(cmarraigeo_value))




wb.close()
