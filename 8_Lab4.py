import csv
import openpyxl
import xlrd

path = "Lab4Data.xlsx"
wb = openpyxl.load_workbook(path, read_only=False)
ws = wb.worksheets[1]


def calctotalmarriage():
    total_marriage_value = []
    cmarraigeb15_range= ws["K15:K211"]
    cmarraigeb18_range= ws["M15:M211"]

    # Iterate through child marriage values
    for i in range(0, len(cmarraigeb15_range)):
        cmarraigeb15_value = cmarraigeb15_range[i][0].value
        cmarraigeb18_value= cmarraigeb18_range[i][0].value
        if("–" in str(cmarraigeb15_value) or "–" in str(cmarraigeb18_value)):
            total_marriage_value.append("–")
        else:
            cmarraigeb15_value = float(cmarraigeb15_value)
            cmarraigeb18_value = float(cmarraigeb18_value)
            toaddd = (cmarraigeb15_value + cmarraigeb18_value)/2
            to_add_roundedd = round(toaddd)
            total_marriage_value.append(to_add_roundedd)
    return total_marriage_value

def calctotaljow():
    total_jow_output = []
    total_jow_rangeM= ws["W15:W211"]
    total_jow_rangeF= ws["Y15:Y211"]

    # Iterate through Justification of Wife Beating
    for i in range(0, len(total_jow_rangeM)):
        jowM_value = total_jow_rangeM[i][0].value
        jowF_value= total_jow_rangeF[i][0].value
        if "–" in str(jowM_value) or "–" in str(jowF_value):
            total_jow_output.append("–")
        else:
            jowM_value = float(jowM_value)
            jowF_value = float(jowF_value)
            to_add = (jowM_value + jowF_value)/2
            to_add_roundedd = round(to_add)
            total_jow_output.append(to_add_roundedd)
    return total_jow_output

def calctotalfgm():
    total_fgm_output = []
    total_fgm__rangeW= ws["Q15:Q211"]
    total_fgm__rangeG= ws["S15:S211"]
    total_fgm__rangeSFTP= ws["U15:U211"]

    # Iterate through Justification of Female genital cutting
    for i in range(0, len(total_fgm__rangeW)):
        fgmW_value = total_fgm__rangeW[i][0].value
        fgmG_value= total_fgm__rangeG[i][0].value
        fgmSFTP_value= total_fgm__rangeSFTP[i][0].value
        if "–" in str(fgmW_value) or "–" in str(fgmG_value) or "–" in str(fgmSFTP_value):
            total_fgm_output.append("–")
        else:
            fgmW_value = float(fgmW_value)
            fgmG_value = float(fgmG_value)
            fgmSFTP_value = float(fgmSFTP_value)
            toadd = (fgmW_value + fgmG_value+ fgmSFTP_value)/3
            to_add_rounded = round(toadd)
            total_fgm_output.append(to_add_rounded)
    return total_fgm_output


countries_range = ws["B15:B211"]
clabour_range = ws["E15:E211"]
clabourM_range = ws["G15:G211"]
clabourW_range = ws["I15:I211"]
cmarraigeb15_range= ws["K15:K211"]
cmarraigeb18_range= ws["M15:M211"]
bregistration_range = ws["O15:O211"]
total_fgm__rangeW= ws["Q15:Q211"]
total_fgm__rangeG= ws["S15:S211"]
total_fgm__rangeSFTP= ws["U15:U211"]
total_jow_rangeM= ws["W15:W211"]
total_jow_rangeF= ws["Y15:Y211"]
vdiscpline_rangeM = ws["AC15:AC211"]
vdiscpline_rangeF = ws["AA15:AA211"]
vdiscpline_range = ws["AE15:AE211"]

#7columns including country_values
country_values = [cell[0].value for cell in countries_range] #197
clabour_values = [cell[0].value for cell in clabour_range] #197
bregistration_values = [cell[0].value for cell in bregistration_range] #197
vdiscpline_values = [cell[0].value for cell in vdiscpline_range]#197
total_marriage_value = calctotalmarriage() #197
total_wife_beating_value = calctotaljow()#197
total_female_genital_Value = calctotalfgm()#197

catagories_list = [clabour_values,total_marriage_value,bregistration_values,total_female_genital_Value,total_wife_beating_value,vdiscpline_values]

def cleancell(cell_value):
    return cell_value.value.replace('\n', ' ')
title = [cleancell(ws.cell(row=5, column=5)),cleancell(ws.cell(row=5, column=11)),cleancell(ws.cell(row=5, column=15)),cleancell(ws.cell(row=5, column=17)),cleancell(ws.cell(row=5, column=23)),cleancell(ws.cell(row=5, column=27))]

#title[0]#Child Labor
#title[1]#Child Marraige
#title[2]#Birth Registration
#title[3]#Female genital cutting
#title[4]#Justification of wife beating
#title[5]#Violent Discpline

header1 = ["CountryName", "CategoryName", "CategoryTotal"]

data_dict = {
    header1[0] : [],
    header1[1] :[],
    header1[2] :[]
}
#Store everything in a dictionary
rows = []
for i in range(len(country_values)):
    for j in range(6):  # Assuming there are 5 categories
        if "–" in str(catagories_list[j][i]):
            continue
        row = {
            header1[0]: country_values[i],
            header1[1]: title[j],
            header1[2]: catagories_list[j][i]
        }
        rows.append(row)

output_file = "8_Lab4.csv"
with open(output_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header1)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)