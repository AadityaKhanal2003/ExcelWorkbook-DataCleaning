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
print(lines)
