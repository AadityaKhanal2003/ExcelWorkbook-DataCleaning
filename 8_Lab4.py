import openpyxl

path = "Lab4Data.xlsx"
wb = openpyxl.load_workbook(path, read_only=False)
ws = wb.worksheets[1]
countries_range = ws["B15:B211"]
clabour_range = ws["E15:E211"]
bregistration_range = ws["O15:O211"]

country_values = [cell[0].value for cell in countries_range]
clabour_values = [cell[0].value for cell in clabour_range]
bregistration_values = [cell[0].value for cell in bregistration_range]
print(country_values)

total_marriage_value = []
cmarraigeb15_range= ws["K15:K211"]
cmarraigeb18_range= ws["M15:M211"]
cmarraige_range = ws["K15:L211"]

# Iterate through child marriage values
for i in range(0, len(cmarraige_range)):
    cmarraigeb15_value = cmarraigeb15_range[i][0].value
    cmarraigeb18_value= cmarraigeb18_range[i][0].value
    if("–" in str(cmarraigeb15_value) or "–" in str(cmarraigeb18_value)):
        total_marriage_value.append("–")
    else:
        cmarraigeb15_value = int(cmarraigeb15_value)
        cmarraigeb18_value = int(cmarraigeb18_value)
        total_marriage_value.append(cmarraigeb15_value + cmarraigeb18_value)
#print(total_marriage_value)
wb.close()
