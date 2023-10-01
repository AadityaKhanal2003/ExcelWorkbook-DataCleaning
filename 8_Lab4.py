import csv
import openpyxl
import xlrd

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

#7columns including country_values
country_values = [cell[0].value for cell in countries_range] #197
clabour_values = [cell[0].value for cell in clabour_range] #197
bregistration_values = [cell[0].value for cell in bregistration_range] #197
vdiscpline_values = [cell[0].value for cell in vdiscpline_range]#197
total_marriage_value = calctotalmarriage() #197
total_wife_beating_value = calctotaljow()#197
total_female_genital_Value = calctotalfgm()#197

def cleancell(cell_value):
    return cell_value.value.replace('\n', ' ')
title = ["Countries",cleancell(ws.cell(row=5, column=5)),cleancell(ws.cell(row=5, column=11)),cleancell(ws.cell(row=5, column=15)),cleancell(ws.cell(row=5, column=17)),cleancell(ws.cell(row=5, column=23)),cleancell(ws.cell(row=5, column=27))]


# Creating a dictionary to store the data
data_dict = {
    title[0]: [], #Countries
    title[1]:[], #Child Labor
    title[2]: [], #Child Marraige
    title[3]: [], #Birth Registration
    title[4]: [], #Female genital cutting
    title[5]: [], #Justification of wife beating
    title[6]:[], #Violent Discpline
}

#Store everything in a dictionary
for i in range(len(country_values)):
    if (
        total_marriage_value[i] != "–"
        and total_wife_beating_value[i] != "–"
        and total_female_genital_Value[i] != "–"
        and vdiscpline_values[i] != "–"
        and bregistration_values[i] != "–"
        and clabour_values[i] !="–"
    ):
        data_dict[title[0]].append(country_values[i])
        data_dict[title[1]].append(clabour_values[i])
        data_dict[title[2]].append(total_marriage_value[i])
        data_dict[title[3]].append(bregistration_values[i])
        data_dict[title[4]].append(total_female_genital_Value[i])
        data_dict[title[5]].append(total_wife_beating_value[i])
        data_dict[title[6]].append(vdiscpline_values[i])
        



 #Write the data to a CSV file
output_file = "8_Lab4.csv"
with open(output_file, "w", newline="") as csvfile:
    count = 0
    writer = csv.DictWriter(csvfile, fieldnames=data_dict.keys())
    writer.writeheader()
    for i in range(len(data_dict[title[0]])):
        row = {
            title[0]: data_dict[title[0]][i],
            title[1]: data_dict[title[1]][i],
            title[2]: data_dict[title[2]][i],
            title[3]: data_dict[title[3]][i],
            title[4]: data_dict[title[4]][i],
            title[5]: data_dict[title[5]][i],
            title[6]: data_dict[title[6]][i],
        }
        count +=1
        writer.writerow(row)

print("No of rows is:", count)
#Closing the workbook finally
wb.close()



