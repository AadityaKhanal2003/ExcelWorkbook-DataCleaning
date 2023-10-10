# Gaurab Baral, Aditya Khanal, Lab 5, Group 8
import slate3k
import csv

filename = "Table9.pdf"
n = 14  # gap between two countries and their data
outer_list = []

with open(filename, 'rb') as fpointer:
    pdf = slate3k.PDF(fpointer)
    temp_list = []
    for content in pdf:
        content = content.strip()  # Remove unwanted line breaks and spaces
        if not content:  
            continue
        outer_list.append(content)  # add from pdf_file to temp_list

lines = []

for sublist in outer_list:
    item_lines = sublist.split('\n')[12:]  # split the data based on "\n" and start from 12 to remove TABLE9 in the output.
    item_lines = [line for line in item_lines if line]  # a list called item_lines and filter out any empty line

    # New code to modify the list
    for index, each_item in enumerate(item_lines):
        if "Bolivia" in each_item:
            item_lines[index] = "Bolivia (Plurinational State of)"  #remove as two lined
            del(item_lines[index+1])
        elif "Democratic People’s" in each_item:
            item_lines[index] = "Democratic People’s Republic of Korea" #remove as two lined
            del(item_lines[index+1])
        elif "Democratic Republic" in each_item:
            item_lines[index] = "Democratic Republic of the Congo" #remove as two lined
            del(item_lines[index+1])
        elif "Lao Peop" in each_item:
            item_lines[index] = "Lao People’s Democratic Republic" #remove as two lined
            del(item_lines[index+1])
        elif "Micronesia" in each_item:
            item_lines[index] = "Micronesia (Federated States of)" #remove as two lined
            del(item_lines[index+1])
        elif "Saint Vincent and" in each_item:
            item_lines[index] = "Saint Vincent and the Grenadines" #remove as two lined
            del(item_lines[index+1])
        elif "The former Yugoslav" in each_item:
            item_lines[index] = "The former Yugoslav Republic of Macedonia" #remove as two lined
            del(item_lines[index+1])
        elif "United Republic" in each_item:
            item_lines[index] = "United Republic of Tanzania" #remove as two lined
            del(item_lines[index+1])
        elif "Venezuela" in each_item:
            item_lines[index] = "Venezuela (Bolivarian Republic of)" #remove as two lined
            del(item_lines[index+1])
            del(item_lines[index-1])                                    #remove the 9 from table9
        elif "Cook Islands" in each_item:
            del(item_lines[index-1])
        elif "Iceland" in each_item:                                    #remove the 9 from table9
            del(item_lines[index-1])
        elif "Montenegro" in each_item:                                     #remove the 9 from table9
            del(item_lines[index-1])
        elif "Seychelles" in each_item:                                     #remove the 9 from table9
            del(item_lines[index-1])
        elif each_item == "B":                                              #remove B from TABLE
            del(item_lines[index])
        elif each_item == "L":                                              #remove L from TABLE
            del(item_lines[index])
        elif each_item == "E":                                               #remove E from TABLE
            del(item_lines[index])
        elif each_item == "T":                                              #remove T from TABLE
            del(item_lines[index])
        elif each_item == "A":                                              #remove A from TABLE
            del(item_lines[index])

        
        
        

    # Append the modified item_lines to lines
    lines.append(item_lines)
                    
temp_list2 = []
outer_list2 = []
previous_line = ""

for data in lines:
    skip_next = 0  # Counter to skip the next 41 items after encountering "CHILD PROTECTION"
    for index, each_item in enumerate(data):
        each_item = each_item.strip()

        if skip_next > 0:
            skip_next -= 1
            continue  # Skip the next 41 items after "CHILD PROTECTION"
        if "CHILD PROTECTION" in each_item:
            skip_next = 36
            continue
        if "SUMMARY INDICATORS" in each_item: #remove all the data sfter summary indicators as we donot need that.
            break
        temp_list2.append(each_item)
        if (index + 1) % 15 == 0:    #keep 15 files in one line.
            outer_list2.append(temp_list2)
            temp_list2 = []

# Display the output
for item in outer_list2:
    if item[0] == "9":
        item.pop(0)                     #remove the magical 9 that appeared out of nowhere
    
    for i in range(1, len(item)):
        item[i] = item[i].replace("x", "")
        item[i] = item[i].replace("y", "")
        item[i] = item[i].replace("v", "")
#at this point item is fully cleaned and ready to be put into csv file.   #the same code as lab4.
def get_column_values(lst_of_lists, column_index):
    column_values = []
    for row in lst_of_lists:
        # Check if the row has enough elements to access the specified column
        if column_index < len(row):
            column_values.append(row[column_index])
    return column_values

country_values = get_column_values(outer_list2, 0)
clabour_values = get_column_values(outer_list2, 1)
clabourM_values = get_column_values(outer_list2, 2)
clabourW_values = get_column_values(outer_list2, 3)
cmarraigeb15_values = get_column_values(outer_list2, 4)
cmarraigeb18_values = get_column_values(outer_list2, 5)
bregistration_values = get_column_values(outer_list2, 6)
total_fgmW_values = get_column_values(outer_list2, 7)
total_fgmG_values = get_column_values(outer_list2, 8)
total_fgmSGM_values = get_column_values(outer_list2, 9)
total_jowM_values = get_column_values(outer_list2, 10)
total_jowF_values = get_column_values(outer_list2, 11)
vdiscpline_values = get_column_values(outer_list2, 12)
vdiscpline_valuesM = get_column_values(outer_list2, 13)
vdiscpline_valuesF = get_column_values(outer_list2, 14)

catagories_list = [clabour_values,clabourM_values,clabourW_values,cmarraigeb15_values,cmarraigeb18_values,bregistration_values,
                   total_fgmW_values,total_fgmG_values,total_fgmSGM_values,total_jowM_values,total_jowF_values,vdiscpline_values,
                   vdiscpline_valuesM,vdiscpline_valuesF]
title = ['Child_labour_total', 'Child_labour_male', 'Child_labour_female', 'Children married by 15', 
         'Children married by 18', 'Birth registration total', 'FGM prevelance in women', 'FGM prevalance in girls','FGM prevelance in support groups', 
         'Justify wife beating male', 'Justify wife beating female', 'Violent discipline total', 'Violent discipline male', 
         'Violent discipline female']

header1 = ["CountryName", "CategoryName", "CategoryTotal"]
#dict for csv file
data_dict = {
    header1[0] : [],
    header1[1] :[],
    header1[2] :[]
}
#count to count the number of rows
count = 0
rows = []
#write the contents of a csv file into a dictionary
for i in range(len(country_values)):
    for j in range(14):  # As there are 14 categories
        if "–" in str(catagories_list[j][i]) or catagories_list[j][i] == "0": #Remove all 0 and all "-
            continue
        row = {
            header1[0]: country_values[i],          #Country Name
            header1[1]: title[j],                   #Category Name
            header1[2]: catagories_list[j][i]       #Category Total
        }
        count+=1
        rows.append(row)
#Writing it in a csv file
output_file = "8_Lab5.csv"
with open(output_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header1) #write title as header1
    writer.writeheader()
    for row in rows:
        writer.writerow(row)                              #add each row in a new row in csv file

print("The total number of rows in the csv file is ",count)
