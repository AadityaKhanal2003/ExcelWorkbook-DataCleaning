import slate3k

filename = "Table9.pdf"
n = 14
outer_list = []

with open(filename, 'rb') as fpointer:
    pdf = slate3k.PDF(fpointer)
    
    temp_list = []
    for content in pdf:
        # Remove unwanted line breaks and spaces
        content = content.strip()
        
        # Skip empty lines
        if not content:
            continue

        temp_list.append(content)

        if len(temp_list) == n:
            outer_list.append(temp_list)
            temp_list = []

    # Append any remaining content as the last sublist
    if temp_list:
        outer_list.append(temp_list)
    fpointer.close()
lines = []
for sublist in outer_list:
    sublist_lines = []
    for item in sublist:
        item_lines = item.split('\n')[12:]
        item_lines = [line for line in item_lines if line]
        sublist_lines.extend(item_lines)
    lines.append(sublist_lines)
temp_list2 = []
outer_list2 = []
for data in lines:
    skip_next = 0  # Counter to skip the next 41 items after encountering "CHILD PROTECTION"
    for index, each_item in enumerate(data):
        each_item = each_item.strip()
        if skip_next > 0:
            skip_next -= 1
            continue  # Skip the next 41 items after "CHILD PROTECTION"

        if "CHILD PROTECTION" in each_item:
            skip_next = 36
            continue  # Skip the "CHILD PROTECTION" item itself
        if "SUMMARY INDICATORS" in each_item:
            break
        temp_list2.append(each_item)

        if (index + 1) % 15 == 0:
            outer_list2.append(temp_list2)
            temp_list2 = []

for item in outer_list2:
    print(item)
