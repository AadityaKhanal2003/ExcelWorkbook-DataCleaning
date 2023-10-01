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
country_names = [cell[0].value for cell in countries_range]

# Calculate values for each category
total_marriage_values = calctotalmarriage()
total_wife_beating_values = calctotaljow()
total_female_genital_values = calctotalfgm()

# Creating a dictionary to store the data
data_dict = {
    "Country": [],
    "Child Marriage": [],
    "Justification of Wife Beating": [],
    "Female Genital Cutting": [],
}

for i in range(len(country_names)):
    if (
        total_marriage_values[i] != 0
        and total_wife_beating_values[i] != 0
        and total_female_genital_values[i] != 0
    ):
        data_dict["Country"].append(country_names[i])
        data_dict["Child Marriage"].append(total_marriage_values[i])
        data_dict["Justification of Wife Beating"].append(total_wife_beating_values[i])
        data_dict["Female Genital Cutting"].append(total_female_genital_values[i])

# Write the data to a CSV file
output_file = "Lab4_CleanData.csv"
with open(output_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=data_dict.keys())
    writer.writeheader()
    for i in range(len(data_dict["Country"])):
        row = {
            "Country": data_dict["Country"][i],
            "Child Marriage": data_dict["Child Marriage"][i],
            "Justification of Wife Beating": data_dict["Justification of Wife Beating"][i],
            "Female Genital Cutting": data_dict["Female Genital Cutting"][i],
        }
        writer.writerow(row)

# Closing the workbook finally
wb.close()
#7columns including country_values
country_values = [cell[0].value for cell in countries_range] #197
clabour_values = [cell[0].value for cell in clabour_range] #197
bregistration_values = [cell[0].value for cell in bregistration_range] #197
vdiscpline_values = [cell[0].value for cell in vdiscpline_range]#197
total_marriage_value = calctotalmarriage() #197
total_wife_beating_value = calctotaljow()#197
total_female_genital_Value = calctotalfgm()#197


wb.close()


