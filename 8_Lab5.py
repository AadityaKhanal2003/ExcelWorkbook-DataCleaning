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
        if not content:  # Skip empty lines
            continue
        outer_list.append(content)  # add from pdf_file to temp_list

lines = []

for sublist in outer_list:
    item_lines = sublist.split('\n')[12:]  # split the data based on "\n" and start from 12 to remove TABLE9 in the output.
    item_lines = [line for line in item_lines if line]  # a list called item_lines and filter out any empty line
    lines.append(item_lines)  # add item_lines to lines list

temp_list2 = []
outer_list2 = []
previous_line = ""

for data in lines:
    skip_next = 0  # Counter to skip the next 41 items after encountering "CHILD PROTECTION"
    for index, each_item in enumerate(data):
        each_item = each_item.strip()

        # Check if the line starts with a space (continuation of the previous line)
        if each_item.startswith(" "):
            # Join it with the previous line
            if temp_list2:
                temp_list2[-1] += " " + each_item.strip()
            continue

        if skip_next > 0:
            skip_next -= 1
            continue  # Skip the next 41 items after "CHILD PROTECTION"
        if "CHILD PROTECTION" in each_item:
            skip_next = 36
            continue
        if "SUMMARY INDICATORS" in each_item:
            break
        temp_list2.append(each_item)
        if (index + 1) % 15 == 0:
            outer_list2.append(temp_list2)
            temp_list2 = []

# Display the output
for item in outer_list2:
    print(item)
