import PyPDF2

print("------Welcome to PDF merger------")
n = int(input("Enter the number of pdf files you want to merge"))
pdfiles = []
i = 1
while i <= n:
    pdfiles.append(input(f"Enter the path of file {i}"))
    i = i + 1

merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile = open(filename, "rb")
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
saved = input("Enter the name by which the merged pdf will be saved:")
merger.write(saved+".pdf")
