import openpyxl

path = "Lab4Data.xlsx"
wb = openpyxl.load_workbook(path, read_only=False)
ws = wb.worksheets[1]
countries_range = ws["B15:B211"]
clabour_range = ws["E15:E211"]
bregistration_range = ws["O15:O211"]
vdiscpline_range = ws["AA15:AA211"]

def calctotalmarriage():
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
            cmarraigeb15_value = round(float(cmarraigeb15_value), 1)
            cmarraigeb18_value = round(float(cmarraigeb18_value), 1)
            toaddd = int(cmarraigeb15_value + cmarraigeb18_value)
            total_marriage_value.append(toaddd)
    return total_marriage_value

def calctotaljow():
    total_jow_output = []
    total_jow_rangeM= ws["W15:W211"]
    total_jow_rangeF= ws["Y15:Y211"]
    total_jow  = ws["W15:Y211"]

    # Iterate through Justification of Wife Beating
    for i in range(0, len(total_jow_rangeM)):
        jowM_value = total_jow_rangeM[i][0].value
        jowF_value= total_jow_rangeF[i][0].value
        if "–" in str(jowM_value) or "–" in str(jowF_value):
            total_jow_output.append("–")
        else:
            jowM_value = round(float(jowM_value), 1)
            jowF_value = round(float(jowF_value), 1)
            toadd = int(jowM_value + jowF_value)
            total_jow_output.append(toadd)
    return total_jow_output

country_values = [cell[0].value for cell in countries_range] #197
clabour_values = [cell[0].value for cell in clabour_range] #197
bregistration_values = [cell[0].value for cell in bregistration_range] #197
vdiscpline_values = [cell[0].value for cell in vdiscpline_range]#197
total_marriage_value = calctotalmarriage()
total_wife_beating_value = calctotaljow()
print(total_wife_beating_value)
wb.close()


