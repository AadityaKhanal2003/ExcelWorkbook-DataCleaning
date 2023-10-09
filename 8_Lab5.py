# Gaurab Baral, Aditya Khanal, Lab 5, Group 8
import slate3k

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
        if (index + 1) % 15 == 0:
            outer_list2.append(temp_list2)
            temp_list2 = []

# Display the output
for item in outer_list2:
    if item[0] == "9":                              #REMOVE THE MAGICAL 9 THAT APPEARRED OUT OF NOWHERE IN ICELAND.
        del[item[0]]
    print(item)