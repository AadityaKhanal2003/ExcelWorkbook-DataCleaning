import csv
import openpyxl
import xlrd

path = "Lab4Data.xlsx"
wb = openpyxl.load_workbook(path, read_only=False)
ws = wb.worksheets[1]



countries_range = ws["B15:B211"]
clabour_range = ws["E15:E211"]
clabourM_range = ws["G15:G211"]
clabourW_range = ws["I15:I211"]
cmarraigeb15_range= ws["K15:K211"]
cmarraigeb18_range= ws["M15:M211"]
bregistration_range = ws["O15:O211"]
total_fgm__rangeW= ws["Q15:Q211"]
total_fgm__rangeG= ws["S15:S211"]
total_jow_rangeM= ws["W15:W211"]
total_jow_rangeF= ws["Y15:Y211"]
vdiscpline_rangeM = ws["AC15:AC211"]
vdiscpline_rangeF = ws["AA15:AA211"]
vdiscpline_range = ws["AE15:AE211"]

#7columns including country_values
country_values = [cell[0].value for cell in countries_range] #197
clabour_values = [cell[0].value for cell in clabour_range]#197
clabourM_values = [cell[0].value for cell in clabourM_range]#197
clabourW_values = [cell[0].value for cell in clabourW_range] #197
cmarraigeb15_values = [cell[0].value for cell in cmarraigeb15_range]#197
cmarraigeb18_values = [cell[0].value for cell in cmarraigeb18_range]#197
bregistration_values = [cell[0].value for cell in bregistration_range] #197
total_fgmW_values = [cell[0].value for cell in total_fgm__rangeW] #197
total_fgmG_values = [cell[0].value for cell in total_fgm__rangeG] #197
total_jowM_values = [cell[0].value for cell in total_jow_rangeM] #197
total_jowF_values = [cell[0].value for cell in total_jow_rangeF] #197
vdiscpline_valuesM = [cell[0].value for cell in vdiscpline_rangeM]#197
vdiscpline_valuesF = [cell[0].value for cell in vdiscpline_rangeF]#197
vdiscpline_values = [cell[0].value for cell in vdiscpline_range]#197


catagories_list = [clabour_values,clabourM_values,clabourW_values,cmarraigeb15_values,cmarraigeb18_values,bregistration_values,
                   total_fgmW_values,total_fgmG_values,total_jowM_values,total_jowF_values,vdiscpline_values,
                   vdiscpline_valuesM,vdiscpline_valuesF]
title = ['Child_labour_total', 'Child_labour_male', 'Child_labour_female', 'Children married by 15', 
         'Children married by 18', 'Birth registration total', 'FGM prevelance in women', 'FGM prevalance in girls', 
         'Justify wife beating male', 'Justify wife beating female', 'Violent discipline total', 'Violent discipline male', 
         'Violent discipline female']

header1 = ["CountryName", "CategoryName", "CategoryTotal"]

data_dict = {
    header1[0] : [],
    header1[1] :[],
    header1[2] :[]
}
#Store everything in a dictionary
rows = []
for i in range(len(country_values)):
    for j in range(13):  # Assuming there are 5 categories
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