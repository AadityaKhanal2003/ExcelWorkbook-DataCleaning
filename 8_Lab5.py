import slate3k
filename = "Table9.pdf"
with open(filename, 'rb') as fpointer:
    n = 15
    pdf = slate3k.PDF(fpointer)
    for page in pdf:
        page1_new = page[6:]
        print(page1_new)
    fpointer.close()