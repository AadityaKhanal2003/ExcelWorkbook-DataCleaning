import slate3k as sl
# #filename = input("Enter the filename: ")
# with open(filename, "rb") as pdf_ptr:
#     pdf_file_object = sl.PDF(pdf_ptr)
#     for page in pdf_file_object:
#         print(page)

filename = "/data/StudentStatsDocument.pdf"

with open(filename,"rb") as file_ptr:
    pdf = sl.PDF(file_ptr)

    for page in pdf:
        print(page.split("/n"))
