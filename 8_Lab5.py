import slate3k
filename = "Table9.pdf"
with open(filename, 'rb') as fpointer:
    pdf = slate3k.PDF(fpointer)
    print(pdf)
    fpointer.close()